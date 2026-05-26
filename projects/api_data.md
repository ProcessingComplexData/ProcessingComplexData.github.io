# API Data Project: ClinicalTrials.gov and Scientific API Workflows

- Project name: `clinical_trials_api`
- Research question (example): __Which study attributes are associated with completed versus ongoing clinical trials in a topic area such as depression?__
- Programming language: `R` (suggested) or `python` (allowed)
- Expert contact: `Javier Garcia-Bernardo`

> **Canonical course conventions live in [`project_guidelines.md`](../project_guidelines.md).** That file is the source of truth for the four required workflow files (`week1_explore.qmd`, `week2_operationalize_clean.qmd`, `week3_model.qmd`, `week4_storytelling.qmd`), the `data/model_data.rds` -> `data/model_results.rds` pipeline, the raw-data policy, quality-check requirements, decision logs, and contribution tracking. Read it before starting and treat anything below as project-specific guidance on top of those conventions.

## Tutorial framing

ClinicalTrials.gov API data are complex because study records arrive through paginated endpoints as nested, institutionally defined JSON rather than as one complete analysis-ready table.

Students should learn three main things about these data:
1. How API data are represented through endpoints, query parameters, OpenAPI specifications, nested JSON, repeated fields, pagination tokens, status codes, and response metadata.
2. How to collect API data responsibly by limiting requests, waiting between calls, caching raw responses, handling `429 Too Many Requests`, and documenting exactly which query produced the dataset.
3. How to turn nested scientific records into one analysis-ready table by choosing fields, flattening modules, handling repeated values, preserving provenance, and explaining what the API schema makes visible or invisible.

## Peer-teaching checklist

| Dimension | This project teaches |
|---|---|
| Data structure | Nested key-value records, arrays of repeated fields, response metadata, pagination tokens, and tabular data after extraction. |
| Storage system | Remote API endpoint, local cache of raw JSON responses, and a small MongoDB (NoSQL/document-store) instance loaded from the cached responses for the relational-vs-document comparison. |
| File formats | JSON responses, OpenAPI YAML specification, and clean table outputs such as CSV/RDS. |
| Encoding | JSON over HTTP, URL query parameters, UTF-8 text, and structured API response metadata. |
| Model | Logistic regression, linear regression, grouped comparison, or simple classifier using the flattened study-level table. |
| Key aspects to explain | Endpoints, query parameters, pagination, rate limits, caching, status codes, schema-defined fields, repeated-field flattening, responsible API use, and when a document store (NoSQL/MongoDB) is preferable to a relational database for nested JSON. |

## Resources
### Data sources
- [ClinicalTrials.gov API documentation](https://clinicaltrials.gov/data-api/api): official documentation for the modern ClinicalTrials.gov REST API.
- [ClinicalTrials.gov API v2 endpoint](https://clinicaltrials.gov/api/v2/studies): main studies endpoint used for search queries.
- [ClinicalTrials.gov OpenAPI specification](https://clinicaltrials.gov/api/oas/v2/ctg-oas-v2.yaml): machine-readable API specification.
- [ClinicalTrials.gov study data structure](https://clinicaltrials.gov/data-api/about-api/study-data-structure): field-level explanation of study records.
- [ClinicalTrials.gov API reference notes](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/scientific/clinicaltrials-database/references/api_reference.md?plain=1): practical notes on pagination, `pageSize`, `pageToken`, and handling `429` responses.

Main raw source for this project: JSON responses from the ClinicalTrials.gov v2 studies endpoint. Students should use a query that returns enough records to require pagination, for example a condition such as depression, diabetes, cancer, or Alzheimer disease.

Alternative API source if ClinicalTrials.gov becomes impractical: Wikimedia APIs. A possible research question is: __Do Wikipedia pages about climate change, fossil fuels, and renewable energy differ in pageviews, edit activity, or revision patterns over time?__

### Knowledge sources
- API concepts: endpoint, query parameter, response, status code, pagination, rate limit, retry, cache, schema, and authentication.
- JSON concepts: nested objects, arrays, repeated fields, missing modules, type conversion, and flattening.
- R packages `httr2`, `jsonlite`, `purrr`, `dplyr`, `tidyr`, `readr`, and `arrow`.
- Wikimedia API documentation as a comparison case for platform rules, user agents, rate limits, and public web infrastructure.

## Week-by-week
### Week 1
Start from the ClinicalTrials.gov endpoint, inspect the API documentation and raw JSON, and download a cached sample using a polite paginated request workflow.
- What is the base URL, endpoint, and query used to collect the studies?
- Which query parameters matter: condition, status, phase, sponsor, location, `pageSize`, `pageToken`, fields, and format?
- What is the raw response structure, and where are the study records, pagination token, and metadata stored?
- How should the script wait between requests, cache each raw response, and respond if the API returns `429 Too Many Requests`?

Prepare for roundtable in week 2:
- Explain how APIs package data through endpoints, query parameters, schemas, nested JSON, and query-specific responses rather than ready-made research tables.
- Explain pagination with `pageToken`: why one request is not necessarily the dataset, and why repeated requests need to be controlled.
- Explain why students should wait between requests, cache raw responses, and avoid repeatedly downloading the same pages.
- Explain one provenance or power issue: who submits trial records, who defines the fields, what quality-control process exists, and what the API does not verify.

### Week 2
Operationalize the research question by flattening the nested API records into one study-level analysis table.
- Is the question about association, prediction, or causal effect?
- What counts as one observation: a study, sponsor-study, condition-study, location-study, arm, outcome, or posted result?
- Which fields are needed: NCT ID, status, sponsor class, study type, phase, enrollment, start year, condition, intervention type, country, or whether results are posted?
- How should repeated fields be handled, such as multiple conditions, phases, sponsors, locations, arms, or outcomes?
- Connect to what the relational-database group taught in the Week 2 roundtable: ClinicalTrials.gov returns deeply nested JSON, which fits a document-store (NoSQL) model like MongoDB much more naturally than a normalized relational schema. Be ready to explain when a NoSQL/document store is the right choice (heterogeneous, nested, schema-flexible records; rapidly evolving fields; whole-document reads), and when a relational database is preferable (strong joins across well-defined entities; transactional integrity; constrained schema). Cite at least one concrete advantage and one concrete disadvantage of each.
- **[TODO before course starts, maybe for the relational data project instead of here]** Load a subset of the cached ClinicalTrials.gov JSON into a small MongoDB instance so students can run a few document queries (find by condition, project specific fields, count by status) and contrast that experience with relational SQL queries on the same conceptual data. This makes the relational-vs-document comparison hands-on rather than purely conceptual.

Prepare for roundtable in week 3:
- Explain the basic API-to-table pipeline: request, wait, cache, parse JSON, flatten nested modules, type-convert fields, and save the clean table.
- Explain how flattening choices change the unit of analysis and can duplicate or drop studies.
- Explain why nested JSON is the natural input to a document store (NoSQL), and what trade-offs you observed when querying the MongoDB version versus the flattened relational/CSV version of the same data.
- Explain one alternative extraction choice, such as study-level versus condition-study-level data, and how it could change the result.

### Week 3
Fit a small interpretable model using the saved Week 2 table, evaluate it, and show one sensitivity check to an API extraction or flattening choice.
- Which outcome and predictors answer the research question: completion status, posted results, enrollment, phase, sponsor class, or study type?
- Which model is small enough to explain clearly: logistic regression, linear regression, grouped comparison, or simple classifier?
- Which parameters answer the substantive question?
- How do conclusions change if the query, page limit, date range, sponsor grouping, status grouping, or repeated-field flattening changes?

Prepare for roundtable in week 4:
- Explain what the model is learning from the API-derived table and what it cannot learn from the original trial records.
- Explain how API limits, waiting, pagination, missing fields, and institutional reporting rules shape what can and cannot be concluded.
- Explain why a failed request, a partial response, or an unhandled `pageToken` can become a scientific problem rather than only a technical problem.

### Week 4
Visualize and tell a story about the clinical-trials pattern while making the API workflow, waiting strategy, and flattening choices explicit.
- What is the context? What is the main result? Why is it important?
- Which visualizations best show the API-derived pattern: status by sponsor class, enrollment by phase, trial counts over time, or completion probability?
- Which parts of the endpoint, query, pagination, and flattening pipeline must the audience understand to trust the result?
- What are the assumptions and limitations of your design?
