"""Generate NSD eye-tracking teaching figures.

This script intentionally uses the small cached overlay table generated during
the feasibility check. The key coordinate check is:

    x_plot = (x + 2) / 4
    y_plot = (2 - y) / 4

That means the gaze coordinates match a 4.0 x 4.0 degree target-image square,
not the larger 8.4 x 8.4 fMRI stimulus-frame assumption.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle
from PIL import Image


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
ASSET_DIR = REPO_ROOT / "assets" / "img" / "projects"
TARGET_IMAGE = (
    REPO_ROOT
    / "data"
    / "nsd_eyetracking"
    / "nsddata"
    / "experiments"
    / "nsdimagery"
    / "rawtargetimages"
    / "setB"
    / "shared0385_nsd28752.png"
)

CACHED_POINTS = SCRIPT_DIR / "nsd_eye_overlay_points.csv"
TMP_POINTS = REPO_ROOT / "tmp" / "nsd_eye_overlay_points.csv"


def load_points() -> pd.DataFrame:
    """Load the cached overlay points and verify the 4-degree mapping."""
    source = CACHED_POINTS if CACHED_POINTS.exists() else TMP_POINTS
    if not source.exists():
        raise FileNotFoundError(
            "Expected nsd_eye_overlay_points.csv in "
            f"{CACHED_POINTS} or {TMP_POINTS}"
        )

    points = pd.read_csv(source)
    required = {
        "window_id",
        "seconds_in_image_window",
        "x",
        "y",
        "velocity",
        "fixation_candidate",
        "x_plot",
        "y_plot",
    }
    missing = required.difference(points.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    x_error = np.nanmax(np.abs(((points["x"] + 2) / 4) - points["x_plot"]))
    y_error = np.nanmax(np.abs(((2 - points["y"]) / 4) - points["y_plot"]))
    if x_error > 1e-9 or y_error > 1e-9:
        raise ValueError(
            "Overlay points do not match the 4.0-degree image-square mapping: "
            f"x_error={x_error:.3g}, y_error={y_error:.3g}"
        )

    return points.sort_values(["window_id", "seconds_in_image_window"])


def add_time_colored_trace(ax, data: pd.DataFrame, cmap, norm, linewidth: float = 1.8):
    """Draw one gaze trace colored by seconds after image onset."""
    xy = data[["x", "y"]].to_numpy()
    if len(xy) < 2:
        return

    segments = np.stack([xy[:-1], xy[1:]], axis=1)
    lines = LineCollection(segments, cmap=cmap, norm=norm, linewidth=linewidth, alpha=0.82)
    lines.set_array(data["seconds_in_image_window"].iloc[1:].to_numpy())
    ax.add_collection(lines)

    ax.scatter(
        data["x"].iloc[0],
        data["y"].iloc[0],
        s=24,
        color="white",
        edgecolor="black",
        linewidth=0.7,
        zorder=5,
    )
    ax.scatter(
        data["x"].iloc[-1],
        data["y"].iloc[-1],
        s=24,
        color="black",
        edgecolor="white",
        linewidth=0.7,
        zorder=5,
    )


def format_image_axis(ax):
    """Use the verified 4.0 x 4.0 degree image square on an axis."""
    ax.add_patch(Rectangle((-2, -2), 4, 4, fill=False, edgecolor="black", linewidth=0.9))
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-2.05, 2.05)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(color="white", linewidth=0.35, alpha=0.25)


def save_repetition_trace_check(points: pd.DataFrame, image: Image.Image, output: Path) -> None:
    """Save the six-panel repeated-presentation trace check."""
    window_ids = sorted(points["window_id"].unique())
    cmap = plt.get_cmap("viridis")
    norm = plt.Normalize(0, 3)

    fig, axes = plt.subplots(2, 3, figsize=(12.5, 8.2), dpi=180, sharex=True, sharey=True)
    fig.subplots_adjust(left=0.06, right=0.84, top=0.87, bottom=0.12, wspace=0.16, hspace=0.20)
    fig.suptitle(
        "NSD repeated target-image presentations: trace check by window",
        fontsize=14,
        fontweight="bold",
        y=0.965,
    )

    for ax, window_id in zip(axes.flat, window_ids):
        data = points[points["window_id"] == window_id].reset_index(drop=True)
        ax.imshow(image, extent=(-2, 2, -2, 2), origin="upper", alpha=0.92)
        add_time_colored_trace(ax, data, cmap, norm)
        format_image_axis(ax)
        ax.set_title(f"Window {window_id}: {len(data)} samples", fontsize=10, pad=7)

    for ax in axes[-1, :]:
        ax.set_xlabel("Horizontal gaze coordinate (degrees)", fontsize=9)
    for ax in axes[:, 0]:
        ax.set_ylabel("Vertical gaze coordinate (degrees)", fontsize=9)

    colorbar_axis = fig.add_axes([0.875, 0.22, 0.025, 0.52])
    colorbar = fig.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=colorbar_axis)
    colorbar.set_label("Seconds after image onset", fontsize=9)
    fig.text(
        0.45,
        0.055,
        "White dot = first usable sample; black dot = last usable sample. "
        "This uses the 4.0-degree helper mapping.",
        ha="center",
        fontsize=9,
        color="#333333",
    )
    fig.savefig(output, bbox_inches="tight")
    plt.close(fig)


def save_dimension_compare(points: pd.DataFrame, image: Image.Image, output: Path) -> None:
    """Save a two-panel check comparing 4.0-degree and 8.4-degree assumptions."""
    window_ids = sorted(points["window_id"].unique())
    colors = plt.get_cmap("tab10")
    window_color = {window_id: colors(i % 10) for i, window_id in enumerate(window_ids)}

    fig, axes = plt.subplots(1, 2, figsize=(12.5, 6.2), dpi=180)
    fig.suptitle(
        "NSD eye-tracking dimension check: same traces, different image-size assumptions",
        fontsize=14,
        fontweight="bold",
        y=0.98,
    )

    panels = [
        (
            axes[0],
            2.0,
            "Image treated as 4.0 deg wide\n(matches the helper x_plot/y_plot columns)",
        ),
        (
            axes[1],
            4.2,
            "Image treated as 8.4 deg wide\n(full NSD fMRI stimulus-frame assumption)",
        ),
    ]
    for ax, half_width, title in panels:
        ax.imshow(image, extent=(-half_width, half_width, -half_width, half_width), origin="upper", alpha=0.96)
        ax.add_patch(
            Rectangle(
                (-half_width, -half_width),
                2 * half_width,
                2 * half_width,
                fill=False,
                edgecolor="black",
                linewidth=1.2,
            )
        )
        for window_id in window_ids:
            data = points[points["window_id"] == window_id]
            ax.plot(
                data["x"],
                data["y"],
                color=window_color[window_id],
                linewidth=1.25,
                alpha=0.78,
                label=f"window {window_id}",
            )
            ax.scatter(
                data["x"].iloc[0],
                data["y"].iloc[0],
                s=18,
                color=window_color[window_id],
                edgecolor="white",
                linewidth=0.5,
                zorder=4,
            )
        pad = half_width * 0.04
        ax.set_xlim(-half_width - pad, half_width + pad)
        ax.set_ylim(-half_width - pad, half_width + pad)
        ax.set_aspect("equal", adjustable="box")
        ax.set_title(title, fontsize=10.5)
        ax.set_xlabel("Horizontal gaze coordinate (degrees from center)")
        ax.set_ylabel("Vertical gaze coordinate (degrees from center)")
        ax.grid(color="white", linewidth=0.4, alpha=0.28)

    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=len(window_ids), frameon=False, fontsize=9)
    fig.text(
        0.5,
        0.055,
        f"Target PNG: {image.width} x {image.height} px. "
        f"Trace range: x {points.x.min():.2f} to {points.x.max():.2f} deg, "
        f"y {points.y.min():.2f} to {points.y.max():.2f} deg.",
        ha="center",
        fontsize=9,
        color="#333333",
    )
    fig.tight_layout(rect=(0, 0.09, 1, 0.94))
    fig.savefig(output, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    points = load_points()
    image = Image.open(TARGET_IMAGE).convert("RGB")

    repetition_output = ASSET_DIR / "nsd_eye_tracking_repetition_trace_check.png"
    dimension_output = ASSET_DIR / "nsd_eye_tracking_overlay_dimension_compare.png"
    legacy_output = ASSET_DIR / "nsd_eye_tracking_fixation_candidates.png"

    save_repetition_trace_check(points, image, repetition_output)
    save_repetition_trace_check(points, image, legacy_output)
    save_dimension_compare(points, image, dimension_output)

    print(f"Wrote {repetition_output}")
    print(f"Wrote {legacy_output}")
    print(f"Wrote {dimension_output}")
    print("Verified mapping: x_plot = (x + 2) / 4 and y_plot = (2 - y) / 4")


if __name__ == "__main__":
    main()
