# Messy Web Text Project: Green Claims and Climate Communication

- Project name: `messy_text`
- Research question (example): __Do company sustainability pages differ linguistically from public-interest climate information pages?__
- Programming language: `python` (suggested) or `R` (allowed)
- Expert contact: TBD, Anastasia?

> **Canonical course conventions live in [project_guidelines.md](../project_guidelines.md).** That file is the source of truth for the four required workflow files (`week1_explore.qmd`, `week2_operationalize_clean.qmd`, `week3_model.qmd`, `week4_storytelling.qmd`), the `data/model_data.rds` -> `data/model_results.rds` pipeline, the raw-data policy, quality-check requirements, decision logs, and contribution tracking. Read it before starting and treat anything below as project-specific guidance on top of those conventions.

## Tutorial framing

Web text is complex because the data arrive wrapped in markup, navigation, scripts, boilerplate, duplicated page elements, and inconsistent page structure rather than as analysis-ready documents.

Students should learn three main things about these data:
1. How web text is produced and represented through HTML, DOM trees, URLs, HTTP requests and responses, CSS, JavaScript, metadata, and page templates.
2. How to turn raw pages into a clean corpus or analysis table by choosing a unit of analysis, extracting meaningful text, removing boilerplate, preserving source metadata, and documenting text-cleaning choices.
3. How extraction, tokenization, repeated page elements, and publisher purpose affect linguistic features, models, visualizations, and the claims that can be made from a small web corpus.

## Peer-teaching checklist

| Dimension | This project teaches |
|---|---|
| Data structure | HTML documents, DOM trees, text corpus, nested page metadata, and document-feature or document-term representations (which are sparse matrices — the same data structure used for network adjacency). |
| Storage system | Raw downloaded HTML files, with NoSQL/document-store storage such as MongoDB discussed as an optional comparison rather than a required implementation. |
| File formats | HTML, JSON metadata or exports, TXT, and CSV/RDS-style clean analysis outputs. |
| Encoding | UTF-8 text, HTML markup, and JSON serialization for metadata or document-style records. |
| Model | Group comparison, logistic or linear regression, clustering, or another small interpretable model using transparent text features. |
| Key aspects to explain | DOM structure, HTTP status codes, robots.txt, scraping legality and ethics, boilerplate removal, tokenization, document-term or TF-IDF features, and sensitivity to extraction choices. |

## Resources
### Data sources
- Raw HTML pages from corporate sustainability pages and public-interest climate information pages.
- Possible corporate sources: Shell, ExxonMobil, TotalEnergies, or other firms identified through Orbis or a similar source. [TODO: to be downloaded before the course]
- Possible public-interest sources: UN climate pages, National Geographic, government climate pages, or climate-focused NGOs.  [TODO]


### Knowledge sources
- Basic HTML and DOM tutorials.
- Python packages such as `requests`, `webSweep`, `beautifulsoup4`, TBD
- R packages such as `rvest`, TBD

## Week-by-week
### Week 1
Inspect raw HTML, explain who published it and why, and identify the DOM structure and markup noise that matter for extraction.
- What is HTML? How does it relate to CSS, JavaScript, and server-side systems such as PHP?
- How do users and scripts interact with websites through HTTP or HTTPS requests?
- What is the unit of raw data in this project: a page, a paragraph, a text block, a sentence, or something else?

Prepare for roundtable in week 2:
- What is the advantage of markup languages such as HTML? Where else are they used?
- Explain why raw HTML is not the same thing as clean text, and introduce the DOM tree and how to use it to extract information.
- Explain the practical and ethical constraints of web data collection, including error codes, scraping legality, and the role of `robots.txt`, even when the project uses already-downloaded pages.
- Explain how publisher type and page purpose shape the data-generating process, and how the unit of analysis was created from messy pages, for example by extracting comparable paragraphs or text blocks.

### Week 2
Operationalize the question by turning raw pages into one analysis table with transparent text-cleaning choices.
- What, exactly, counts as corporate climate communication or public-interest climate communication?
- Which parts of each page should be kept or removed: headers, menus, cookie banners, captions, footers, links, boilerplate, and repeated slogans?
- Which text representation fits the research question? Start with a transparent count-based or TF-IDF representation. Embeddings are an **optional** extension only if time allows and only after a count/TF-IDF baseline has been built and interpreted.
- The document-term matrix you build is typically extremely sparse (most documents do not contain most terms). This is the same sparse-matrix concept that the Networks group teaches with adjacency matrices — note this connection so the two groups can teach it jointly.
- **Optional cross-modality reflection:** how is turning text into a model table similar to turning images, audio, or video into model inputs (pixels, spectrograms, frames, embeddings, labels, or extracted features)? Skip if time is tight.
- What source metadata should stay attached to each unit, such as publisher type, URL, date collected, page title, or page section?

Prepare for roundtable in week 3:
- Explain the basic NLP ideas used in the project, such as tokenization, hand-built lexical features, or document-term style representations, without overselling their sophistication.
- Explain why the document-term matrix is sparse and how that connects to the sparse-matrix idea also seen in network adjacency matrices.
- Optional: compare text with images, audio, and video — what is the raw file format, what counts as the unit of analysis, and what choices are needed before the data become a table or model input?
- Explain why a simple text model can still be useful if the feature engineering is transparent and tied to a substantive framing question.
- Explain how extraction choices, token choices, and repeated text from the same page can change the model result.

### Week 3
Fit a small interpretable text model using hand-built features or simple document representations, and show sensitivity to extraction or tokenization decisions.
- Is the goal to describe linguistic differences, classify source type, or estimate an association between publisher type and framing?
- Which features answer the research question: risk terms, urgency terms, technology terms, efficiency terms, sentiment, modal verbs, or topic-like clusters?
- Build the baseline model on count or TF-IDF features first. Only add an embedding-based representation if the baseline is fully working and there is real time left.
- Which model or comparison is small enough to explain clearly: group differences, logistic regression, linear regression, clustering, or a simple classifier?
- How do results change if boilerplate removal, tokenization, stopword choices, or repeated pages are handled differently?

Prepare for roundtable in week 4:
- Explain what the model is actually learning from the text and what it is not learning.
- Explain which visual summary best teaches the contrast across sources: keyword frequencies, coefficient plots, or source-level framing differences.
- Explain the main limitation of drawing broad conclusions from a small purposive web corpus.

### Week 4
Visualize and tell a story about the contrast between sources, while making the limits of the corpus and preprocessing choices explicit.
- What is the context? What is the main result? Why is it important?
- Which visualizations support the finding without pretending the model understands the full meaning of the pages?
- Which extraction, labeling, or source-selection choices could change the story?
- What are the assumptions and limitations of your design?
