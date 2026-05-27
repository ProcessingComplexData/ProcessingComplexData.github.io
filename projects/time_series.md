# Time Series Project: Scientific Data Standards and Temporal Signals

- Project name: `scientific_time_series`
- Research question (example): __How does a signal change over time within a participant, task, or experimental condition?__
- Programming language: **`Python` suggested for raw-data processing** (BIDS/NIfTI/event-file handling: `nibabel`, `pybids`, `nilearn`, `numpy`, `pandas`, and the NSD-specific `nsdcode` / `nsd_access`). **`R` suggested for the modeling and analysis stage** (`lme4`, `nlme`, `tidyverse`) once Week 2 has produced the participant-session-ROI panel. Students may stay in one language throughout if they prefer, but the default split is Python → panel → R.
- Expert contact: TBD, Ben Harvey?

> **Canonical course conventions live in [project_guidelines.md](../project_guidelines.md).** That file is the source of truth for the four required workflow files (`week1_explore.qmd`, `week2_operationalize_clean.qmd`, `week3_model.qmd`, `week4_storytelling.qmd`), the `data/model_data.rds` -> `data/model_results.rds` pipeline, the raw-data policy, quality-check requirements, decision logs, and contribution tracking. Read it before starting and treat anything below as project-specific guidance on top of those conventions.

## Tutorial framing

Scientific time-series data are complex because observations are ordered, repeated, metadata-dependent, and often stored in domain-specific standards designed for reproducibility rather than immediate analysis as a flat table.

Students should learn three main things about these data:
1. How scientific time-series data are represented through samples, events, timestamps, participant metadata, task metadata, calibration or acquisition settings, and standards such as BIDS-style folder structures, NIfTI, EDF/ASC, TSV sidecars, JSON metadata, HDF5, or NetCDF.
2. How to turn a raw temporal scientific object into an analysis-ready panel or time-series table by defining the signal, unit of analysis, time window, alignment rule, missing-data rule, and feature extraction choices.
3. How temporal dependence, sampling rate, smoothing, aggregation, lag construction, and scientific metadata affect modeling, visualization, assumptions, and the claims that can be made from the data.

## Peer-teaching checklist

| Dimension | This project teaches |
|---|---|
| Data structure | Time-indexed samples or events, multivariate time series, participant/task metadata, and possibly spatiotemporal arrays. |
| Storage system | Scientific repository or instructor-provided raw dataset organized through a scientific data standard. |
| File formats | One chosen standard such as BIDS with NIfTI/TSV/JSON sidecars, EDF/ASC eye-tracking exports, HDF5, NetCDF, or comparable domain files. |
| Encoding | Text metadata or event files, JSON sidecars, and binary scientific signal formats. |
| Model | Group comparison of extracted temporal features, linear or mixed model, lagged regression, simple classifier, or time-window comparison. |
| Key aspects to explain | Temporal order, sampling rate, alignment, smoothing, aggregation windows, missing segments, lag construction, scientific metadata, and sensitivity to preprocessing choices. |

## Resources
### Data source

The practical is built around fMRI data. European fMRI datasets are difficult to share publicly: anything that reveals the detailed structure of an individual brain — including raw fMRI volumes — is typically considered individually identifiable under the GDPR and cannot be released openly. The practical therefore uses an American dataset that is shareable.

Primary dataset: **Natural Scenes Dataset (NSD)** — a high-resolution 7T fMRI dataset of individuals viewing thousands of natural images, with raw BIDS files, prepared NIfTI files, repeated scan sessions, visual ROI masks, behavioral/task event files, and extensive documentation. Access is public through AWS Open Data after signing the NSD data access agreement.

- Dataset and documentation: https://naturalscenesdataset.org/
- Main reference paper: Allen et al. (2022), Nature Neuroscience. https://doi.org/10.1038/s41593-021-00962-x
- Session-drift / repeated-measures reference (a useful precedent for the kind of question students can replicate): https://doi.org/10.1038/s41467-023-40144-w

### Candidate research question

Good fMRI research has moved well beyond simple summaries — current work uses complex models of neural responsivity, not toy questions. Students do not need to invent a new contribution. Instead they can replicate one of two well-established demonstrations, both supported directly by NSD:

1. Response amplitudes in a visual ROI vary across scan sessions for one participant (the session-drift / repeated-measures phenomenon documented in the reference above).
2. Animate versus inanimate object categories produce distinguishable responses in many brain areas.

Either question keeps the project at a defensible size, foregrounds the BIDS/NIfTI raw object, and gives students something real to learn rather than a manufactured small question.

### Alternative: NSD eye-tracking data

If a group has a strong eye-tracking reason to deviate, NSD also includes eye-tracking data on AWS, which keeps the dataset and provenance story consistent:

- Raw EyeLink files per run: `s3://natural-scenes-dataset/nsddata_timeseries/ppdata/subj01/eyedata/` (e.g. `eyedata_nsdimagery_run01.edf`)
- Preprocessed eye-tracking file per subject: `s3://natural-scenes-dataset/nsddata_timeseries/ppdata/subj01/eyedata_preprocessed.mat` (~162 MB for `subj01`)
- Eye-tracking inspection plots: `s3://natural-scenes-dataset/nsddata/inspections/eyetrackinginspections/` (e.g. `pupil_subj01_nsdimagery_run01.jpg`)

This is the fallback path, not the default. The main practical is fMRI.

### Knowledge sources
- BIDS documentation for neuroimaging data organization and metadata.
- Basic introductions to NIfTI, JSON sidecars, events files, and participant metadata.
- NSD documentation, the main paper (https://doi.org/10.1038/s41593-021-00962-x), and the session-drift paper (https://doi.org/10.1038/s41467-023-40144-w) on the dataset page.
- Python packages for raw-data processing: `nibabel` and `nilearn` for NIfTI/ROI handling, `pybids` for BIDS queries, `numpy`, `pandas`, `matplotlib`, the official NSD `nsdcode`, and community helpers such as `nsd_access` or `nsdget`.
- R packages for the modeling stage (after the panel is built): `lme4` or `nlme` for mixed models, `broom.mixed` for tidy output, `tidyverse` for wrangling, and `ggplot2` for visualization.

### Teaching angle
- Week 1: inspect BIDS metadata, events TSV files, NIfTI headers, ROI masks, and the AWS scientific repository structure.
- Week 2: extract a participant-session-ROI panel from NIfTI arrays.
- Week 3: fit a within-subject model that addresses one of the two candidate questions (session drift or animate-vs-inanimate distinction) and one sensitivity check tied to the operationalization.
- Week 4: visualize the result and explain what was gained and lost by reducing voxelwise fMRI maps to the summary used.


## Week-by-week
### Week 1
Start from the raw scientific files, identify the data-generating process, and explain why the data are stored in a standard rather than in one analysis-ready table.
- What is the scientific object: gaze samples, fixation events, fMRI volumes, task events, or participant-level metadata?
- What is the storage standard or raw format, and which files belong together?
- What is the sampling rate or temporal resolution, and how is time represented?
- Which metadata are required to interpret the signal correctly?

Prepare for roundtable in week 2:
- Explain why temporal order is itself a data structure and why it cannot be treated like independent rows.
- Explain what a scientific data standard is and why standards such as BIDS, NIfTI plus JSON sidecars, EDF/ASC exports, HDF5, or NetCDF exist.
- Explain the difference between raw measurements, task events, derived features, and analysis-ready summaries.
- Explain one provenance or power issue: who was measured, under what task or device constraints, and what is invisible in the recorded signal?

### Week 2
Operationalize the research question by turning the raw scientific files into one analysis-ready time-series or panel object.
- What, exactly, is the outcome signal: gaze position, fixation duration, pupil size, regional fMRI signal, task response, or another feature?
- What is the unit of analysis: sample, event, time window, trial, participant, region, or participant-condition?
- How should time be aligned across participants, trials, regions, or task events?
- How should gaps, blinks, missing volumes, noisy segments, or implausible values be handled?

Prepare for roundtable in week 3:
- Explain how aggregation, smoothing, filtering, baseline correction, lag construction, or feature extraction changed the raw signal.
- Explain what is gained and lost when a rich temporal object is reduced to windows, averages, slopes, or event-level summaries.
- Explain one alternative cleaning choice and how it could affect the result.

### Week 3
Fit a simple within-subject model on the panel from Week 2, evaluate it, and show one sensitivity check to a processing choice that is actually present in your pipeline. The specific model depends on which of the two candidate RQs the group chose:

- If the question is **session drift in a visual ROI** (RQ 1): fit a linear or mixed model of mean ROI beta on session number for one participant, and the key parameter is the session slope. Sensitivity: alternative ROI definition (V1v vs. V1d vs. combined V1), alternative session-aggregation window, or alternative missing-session rule.
- If the question is **animate vs. inanimate distinguishability** (RQ 2): fit a group comparison or a simple classifier on trial- or condition-level ROI responses, and the key parameter is the contrast / classification metric. Sensitivity: alternative ROI choice, alternative trial selection, or alternative animacy labeling rule.

Common prompts for both RQs:
- Is the goal association, prediction, or causal effect? (For both candidate RQs this is a descriptive within-subject question.)
- Which model is small enough to explain clearly given that the temporal index is sessions or trials, not raw samples?
- Which parameter answers the substantive research question, and what would a null result actually look like?

Prepare for roundtable in week 4:
- Explain why the temporal index here is session order (RQ 1) or trial structure (RQ 2), not within-trial autocorrelation, and what that implies for which "time-series" concepts apply and which don't.
- Explain how within-subject repeated measurement creates dependence that ordinary i.i.d. regression ignores, and how a mixed model or paired comparison addresses it.
- Explain how the model uses the extracted signal (session-mean beta in an ROI, or condition-level ROI response) and what parts of the original scientific object (voxel-level structure, trial-level events, full BOLD time series) it ignores.
- Explain why sensitivity to ROI choice, aggregation level, and labeling rules is central rather than optional in this kind of work.

### Week 4
Visualize and tell a story about the within-subject result while making the data standard, preprocessing, and model assumptions explicit.
- What is the context? What is the main result? Why is it important?
- Which visualizations best separate raw NIfTI data, the ROI-aggregated summary, and the fitted model? For RQ 1: a per-session line/dot plot of mean beta per ROI with the fitted slope and an uncertainty band. For RQ 2: ROI-level mean response by animacy category, with appropriate uncertainty.
- Which scientific metadata or preprocessing choices (BIDS structure, ROI definition, beta version, session/trial filter, animacy labels) are necessary for someone else to reproduce the result?
- What are the assumptions and limitations of your design, especially the move from voxelwise fMRI to ROI-level summaries?
