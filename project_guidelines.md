# Project Guidelines

These guidelines apply to all project variants in **Processing Complex Data**.

- Team size: 4 students.
- Level: 1st-year master.
- Language priority: R + Quarto (`.qmd`). Use Python only when a raw format is substantially easier there.
- Difficulty target: all variants should feel comparable in scope and workload.

## Project Management

> [!NOTE]
> Remember that you need to write down how you each contribute.

- How will we work together? Meetings to sit together? Teams channel? Email?
- How will you write the report? Microsoft Office? Overleaf / LaTeX? Quarto? Google Docs? You decide.
- The projects are very short: be strict on your deadlines. Also help each other out.
- Assign weekly roles: coordinator, data lead, modeling lead, and presenter/reviewer.
- Keep a short decision log inside each weekly `.qmd` under `Scope choices`.
- Record how work was divided; contribution tracking is part of the project.
- Use short weekly deadlines because the project is intentionally scoped for fast iteration.

## Exploration and Data

> [!NOTE]
> Start trying to implement small solutions for subquestions quickly.

## Research Question Operationalization

> [!NOTE]
> Keep it small, do not be afraid to make choices, the projects are short.

## Modeling and Report

> [!NOTE]
> Make things understandable for your audience: your peers.

## Raw-Data Policy

- Do not start from a pre-cleaned analysis file committed by the instructor.
- Week 1 and Week 2 should begin from raw website, repository, API, database, or scientific-format data.
- It is fine to create a clean analysis object inside Week 2 code, but that cleaning must happen inside the student workflow.
- Prefer complex formats over plain CSV when a realistic raw source exists.
- At least one variant should explicitly discuss Parquet as a columnar storage alternative when contrasting storage choices.

## Reproducible Structure

- What is a good folder structure for collaboration and sharing? Tip: get inspiration from the [ODISSEI-SODA guide to sharing research code](https://odissei-soda.nl/tutorials/share-your-reserarch-code/).
- Each variant must have exactly four executable workflow files:
  - `week1_explore.qmd`
  - `week2_operationalize_clean.qmd`
  - `week3_model.qmd`
  - `week4_storytelling.qmd`
- The weeks form one pipeline rather than four unrelated notebooks.
- `week1_explore.qmd` should download the raw data if they are not already present and then explore those raw files.
- `week2_operationalize_clean.qmd` should read the raw files and write `data/model_data.rds` for the Week 3 model.
- `week3_model.qmd` should read `data/model_data.rds`, fit the model, and write `data/model_results.rds`.
- `week4_storytelling.qmd` should read `data/model_results.rds` and turn those saved results into presentation-ready figures.
- Keep executable code under about 100 non-empty lines per file.
- It is still preferable for most files to stay compact and readable, but preprocessing in Week 2 does not need to be artificially short.

## Week-by-Week Scope

- Week 1: explain origin, purpose, storage system, file format, encoding, download the raw data, and show the first exploratory view of the raw source.
- Week 2: define whether the question is about association, prediction, or causal effect, and build one analysis-ready object from the raw source that is saved for later use.
- Week 3: fit the baseline model on the saved Week 2 data, evaluate it, and save the model output that Week 4 will visualize.
- Week 4: explain the model assumptions, turn the saved model output into figures for the presentation, and state the main limitation clearly.

## Quality Checks

- Week 1: report row counts, feature counts, missingness, and one note on data provenance or power.
- Week 2: test keys, parsing, impossible values, and one alternative cleaning choice.
- Week 3: report at least one fit metric and one sensitivity or robustness check.
- Week 4: include one uncertainty statement and one limitation slide or paragraph.

## Documentation Minimum

- Keep source links in the project description `.md` files.
- Keep operational definitions in Week 2.
- Keep model interpretation and caveats in Week 4.
- If AI assistance was used, state where it entered the workflow.
