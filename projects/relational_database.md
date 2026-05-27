# Relational Database Project: Formula 1 Race History

- Project name: `f1_race_history`
- Research question (example): __Which driver, constructor, grid, circuit, and season characteristics are associated with Formula 1 finishing points?__
- Programming language: `R` + PostgreSQL (suggested) or `python` (allowed)
- Expert contact: TBD

> **Canonical course conventions live in [project_guidelines.md](../project_guidelines.md).** That file is the source of truth for the four required workflow files (`week1_explore.qmd`, `week2_operationalize_clean.qmd`, `week3_model.qmd`, `week4_storytelling.qmd`), the `data/model_data.rds` -> `data/model_results.rds` pipeline, the raw-data policy, quality-check requirements, decision logs, and contribution tracking. Read it before starting and treat anything below as project-specific guidance on top of those conventions.

## Tutorial framing

Formula 1 relational data are complex because race results are distributed across normalized tables for races, drivers, constructors, circuits, seasons, standings, and result views rather than arriving as one analysis-ready rectangular file.

Students should learn three main things about these data:
1. How relational data are represented through tables, schemas, primary keys, foreign keys, one-to-many relationships, many-to-many relationships, SQL queries, views, indices, and database files or dumps.
2. How to turn normalized racing tables into one analysis-ready object by defining the analytic unit, writing joins, filtering races, aggregating related rows, and documenting the assumptions built into the join pipeline.
3. How schema design, views, missing keys, join type, aggregation level, era restrictions, sprint-era rules, transaction-oriented storage, and analytical columnar storage affect modeling, interpretation, and the claims that can be made from race-history data.

## Peer-teaching checklist

| Dimension | This project teaches |
|---|---|
| Data structure | Relational schema, normalized tables, primary and foreign keys, one-to-many and many-to-many relationships, and joined analysis tables. |
| Storage system | PostgreSQL database from an SQL dump, with comparison to SQLite, CSV/Excel/RDS exports, and Parquet as analytical columnar storage. |
| File formats | PostgreSQL SQL dump, SQLite database file where relevant, CSV, JSON, RDS, Excel, and Parquet. |
| Encoding | SQL text dump, binary database storage, text delimited files, R-specific serialization, and columnar Parquet encoding. |
| Model | Linear, logistic, count, or grouped comparison model on a constructed driver-race, constructor-race, or season-level table. |
| Key aspects to explain | Schemas, joins, keys, views, indices (including hash indexes and hash joins as the under-the-hood mechanism for equality lookups), ACID, row duplication or loss, unit of analysis, row-oriented database storage vs. columnar Parquet, and why SQL is declarative. |

## Resources
### Data sources
- [F1DB GitHub repository](https://github.com/f1db/f1db): Formula 1 race-history database with releases in multiple formats.
- [F1DB releases](https://github.com/f1db/f1db/releases): download the PostgreSQL release asset, such as `f1db-sql-postgresql.zip` or `f1db-sql-postgresql-single-inserts.zip`. The same releases also provide SQLite, MySQL, CSV, and JSON versions.
- Main raw source for this project: the PostgreSQL SQL dump from F1DB. It contains a normalized racing schema with races, drivers, constructors, circuits, seasons, entrant tables, standings, and result views.

Alternative data sources only if F1DB becomes impractical: Lahman Baseball Database, CTU Financial, CTU Credit, Chinook, and Northwind.

### Knowledge sources
- SQL concepts: `SELECT`, `JOIN`, `GROUP BY`, `WHERE`, `HAVING`, views, indices, primary keys, foreign keys, and common table expressions.
- PostgreSQL concepts: schemas, SQL dumps, `psql`, table constraints, views, indices, and `EXPLAIN`.
- R packages `DBI`, `RPostgres`, `dbplyr`, `dplyr`, `dm`, and `arrow`.
- F1DB documentation and release notes for understanding available formats and updates.
- Parquet as a columnar storage alternative to discuss when contrasting analytical storage with relational database storage.

## Week-by-week
### Week 1
Start from the raw PostgreSQL SQL dump, identify the schema, and explain why the data are stored relationally rather than as one flat file.
- What are the main tables, and what real-world entities do they represent?
- Which columns are primary keys, foreign keys, or plausible join keys?
- Which relationships are one-to-many or many-to-many?
- What is the storage system, file format, and encoding, and how does PostgreSQL differ from CSV, SQLite, or Parquet?
- Choose one large or central table or view, export it to CSV, Excel, RDS, and Parquet, and compare file size, readability, metadata preservation, and loading behavior.

Prepare for roundtable in week 2:
- Explain schemas, primary keys, foreign keys, one-to-many relationships, and many-to-many relationships in a way that other groups can understand.
- Explain why the data are stored in a relational database rather than in one flat file, including the role of SQL, views, indices, and transaction-oriented database storage.
- Explain how a database actually executes a join or a selective `WHERE`/key lookup under the hood. Cover hash indexes and hash joins specifically: how a hash table maps keys to row locations in O(1) average lookup, why hash joins are efficient for large equality joins, and how this relates to B-tree indexes for range queries. This gives the other groups a concrete picture of why "schemas + indexes" is faster than scanning a CSV.
- Compare row-based relational storage with columnar or analytical storage: when would PostgreSQL, CSV, Excel, RDS, or Parquet be more appropriate?
- Explain what can go wrong when joins duplicate rows, drop rows, or silently change the unit of analysis.
- Explain one provenance or power issue: who generated the records, for what institutional purpose, and which processes are invisible in the database.

### Week 2
Operationalize the research question by writing one join pipeline that creates an analysis-ready object from the raw tables.
- Is the question about association, prediction, or causal effect?
- What is the unit of analysis: driver-race, constructor-race, driver-season, constructor-season, circuit-race, or something else?
- Which joins, filters, and aggregations are needed to create that unit?
- Which records are lost or duplicated under different join choices?
- Try the same simple operations on the exported CSV, Excel, RDS, and Parquet versions, such as filtering seasons, selecting columns, grouping by constructor, and calculating mean points. Which format is easiest to inspect, easiest to share, smallest on disk, and fastest or most convenient for analysis?

Prepare for roundtable in week 3:
- Explain the full data lineage from raw tables to the Week 2 modeling table.
- Explain how aggregation level, join type, missing keys, or filtering thresholds shape the variables that enter the model.
- Explain what the storage-format comparison taught you about relational databases versus analytical files, especially CSV, Excel, RDS, and Parquet.
- Explain one alternative join or aggregation choice and how it could affect the result.

### Week 3
Fit a small model on the joined Week 2 data, evaluate it, and show one sensitivity check to a join, filter, or aggregation choice.
- Which outcome and predictors answer the research question?
- Which model is small enough to explain clearly: linear regression, logistic regression, count model, simple classifier, or grouped comparison?
- Which parameters answer the substantive question?
- How do conclusions change if the analytic unit, join type, era restriction, sprint-era handling, or filtering threshold changes?

Prepare for roundtable in week 4:
- Explain how the model depends on the join pipeline rather than only on the final table.
- Explain why the model is usually a descriptive or predictive summary of organizational data rather than automatic evidence of a causal process.
- Explain what assumptions are hidden in the database schema, missing records, and aggregation choices.

### Week 4
Visualize and tell a story about the joined data and model while making the schema and preprocessing choices explicit.
- What is the context? What is the main result? Why is it important?
- Which visualizations best show the constructed unit of analysis, the model result, and the uncertainty or sensitivity check?
- Which parts of the schema and join pipeline must the audience understand to trust the result?
- What are the assumptions and limitations of your design?
