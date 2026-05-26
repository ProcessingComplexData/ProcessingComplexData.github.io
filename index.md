# Processing Complex Data

This webpage contains all materials for the Methodology and Statistics master course **Processing Complex Data (PCD)**. The materials on this website are [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) licensed.

![cc](https://mirrors.creativecommons.org/presskit/icons/cc.svg) ![by](https://mirrors.creativecommons.org/presskit/icons/by.svg)

## About the course

Contrary to what most introductory data science and statistics courses teach, real-world scientific data come in an enormous variety of formats, sizes, structures, and procedures — from simple tables to spatiotemporal arrays, normalized relational schemas, nested API responses, raw scraped web pages, networks, and domain-specific scientific standards. This course gives students hands-on experience with handling, processing, and modelling six families of complex data, in a hackathon-style format where each group goes deep on one data type and teaches the rest of the class.

The narrative spine of the course is *from raw traces to defensible claims*. Each group works through a single pipeline: raw source → operationalized clean object → baseline model with one sensitivity check → presentation.

## Course materials

- [Course manual](course_manual.md) — official course description, learning goals, assessment, and materials.
- [Project guidelines](project_guidelines.md) — workflow files, raw-data policy, decision logs, quality checks, and contribution tracking.

## Lectures

| Week | Title | Lecture |
| :--- | :---- | :------ |
| 1 | What Makes Data Complex? | TBD |
| 2 | From Complex Data to Clean Data | TBD |
| 3 | Scaling Up Modeling | TBD |
| 4 | Communicating Research | TBD |
| 5 | Presentations | — |
| 6 | Short Report | — |

## Group projects

Six project variants. Each group works through the same four-week workflow (`week1_explore.qmd`, `week2_operationalize_clean.qmd`, `week3_model.qmd`, `week4_storytelling.qmd`) on its own data family, and teaches the same six dimensions to the rest of the class: **data structure, storage system, file formats, encoding, model, and key aspects**.

| Variant              | Data family                                                    | Example research question                                                                                  |
| :------------------- | :------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| Geospatial           | [`projects/geospatial.md`](projects/geospatial.md)             | What is the relation between municipal land use and population composition?                                |
| Networks             | [`projects/networks.md`](projects/networks.md)                 | What is the relationship between gender and cross-program relations in high school?                        |
| Messy web text       | [`projects/messy_web_text.md`](projects/messy_web_text.md)     | Do company sustainability pages differ linguistically from public-interest climate information pages?      |
| Relational database  | [`projects/relational_database.md`](projects/relational_database.md) | Which driver, constructor, grid, circuit, and season characteristics are associated with F1 finishing points? |
| Time series          | [`projects/time_series.md`](projects/time_series.md)           | How does an fMRI signal change across NSD scan sessions? |
| API data             | [`projects/api_data.md`](projects/api_data.md)                 | Which study attributes are associated with completed versus ongoing clinical trials?                       |

## Assessment

Assessment is based on the group project, which runs for the full duration of the course. The project grade is the final course grade. Each group submits a short structured report and gives a final presentation; both are evaluated on the raw-to-clean-to-model pipeline, the methodological choices, and the limits of the claim.
