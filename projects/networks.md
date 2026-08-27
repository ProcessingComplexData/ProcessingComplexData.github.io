# Network Projects

- Project name: `networks`
- Research question (example): __Are same-gender face-to-face contacts more common than expected, given the composition of each school class?__
- Expert contact: `Javier Garcia-Bernardo`
- Programming language:  `R` or `python`
- Last updated: 2026-08-27

> **Course conventions live in [project_guidelines.md](../project_guidelines.md).** Read it before starting and treat anything below as project-specific guidance on top of those conventions.

## Project framing and learning outcomes

Network data are complex because observations are connected through ties. The same social setting can produce different observed networks depending on how relationships are measured. Each measurement has its own direction, weight, coverage, missingness, and substantive meaning.

By completing this project, students should be able to:
1. Understand the advantages of a network approach.
2. Describe network data using nodes, ties, attributes, layers, edge lists, adjacency matrices, sparse matrices, graph objects, GraphML, and visualization layouts.
3. Construct comparable networks while making explicit decisions about direction, weight, node coverage, missing ties, isolates, and the meaning of each measurement.
4. Use one network statistic with an appropriate network model and check sensitivity to one representation choice.
5. Defend a network claim while distinguishing measurement from social reality, visualization from evidence, association from mechanism, and selection from influence.

## Peer-teaching checklist

| Dimension | This project teaches |
|---|---|
| Data structure | Graphs with nodes, edges, node attributes, edge attributes, edge lists, adjacency matrices, and sparse matrix representations. |
| Storage system | File-based network repositories and downloaded graph files. |
| File formats | CSV edge lists, GraphML, JSON |
| Encoding | Text CSV, XML-based GraphML, JSON |
| Model | Assortativity or homophily statistic, permutation test, clustering, or a small network summary model. |
| Key aspects to explain | What counts as a node or tie, directed vs. undirected graphs, weighted vs. unweighted ties, isolates, sparse vs. dense matrices, network visualization, and why network dependence violates ordinary i.i.d. assumptions. |

## Resources
### Data sources
- Network data:
  - [Original SocioPatterns high-school contact and friendship files](https://sociopatterns.org/datasets/high-school-contact-and-friendship-networks/)
  - Stanford Large Network Dataset Collection: https://snap.stanford.edu/data/
  - Network repository: https://networkrepository.com/networks.php
  - Netzschleuder: https://networks.skewed.de
  - Index of Complex Networks: https://icon.colorado.edu
- Potential dataset: https://networks.skewed.de/net/sp_high_school (interactive viz: https://javier.science/panel_network/)

For the suggested high-school data, the available measurements include sensor-recorded contact, contact diaries, friendship nominations, and Facebook relations. Treat sensor contacts as an aggregated static network for the core project. Use the original files when it matters to distinguish recorded non-ties from dyads that were not measured.


### Knowledge sources
- R/Python package `igraph`
- Introduction to networks
  - Chapter 0 of "A First Course in Network Science": https://github.com/CambridgeUniversityPress/FirstCourseNetworkScience/blob/master/sample/chapters/chapter0.pdf
  - App: https://javier.science/marimo_intro_networks/
- Guide for reference models: https://pubmed.ncbi.nlm.nih.gov/34216192/
- Observed vs latent networks: https://www.nature.com/articles/s41467-022-34267-9


## Week-by-week

### Week 1 — Explore the raw data

Begin with raw repository files and explain what the network is, who generated it, for what purpose, and the different storage formats.
- Explain the underlying network in substantive terms: what the nodes and ties represent, and whether the graph is directed or undirected, weighted or unweighted, static or temporal.
- What is the GraphML data type? How does it relate to XML? How is this different from other network data types?
- Construct a small edge-list and adjacency-matrix example and inspect its sparse structure.
- Make one exploratory view while treating the layout as a view of the graph rather than an analytical result.
- Report node counts, tie counts, isolates, missing metadata, and unrecorded ties or dyads whose status is unknown.

Prepare for roundtable in week 2:
- What is a network and why is it a useful representation?
- What are the main ways to represent a network: edge lists, adjacency matrices, and XML or GraphML-like?
- What are the advantages and disadvantages of adjacency matrices over edge lists? How do sparse matrices fix this and what are they?
- How do you visualize a network? What could be the pitfalls of having your analysis based on the network visualization only?


### Week 2 — Operationalize the research question and create analysis-ready data


- Think about a potential research question. Is it about a full network, such as homophily or polarization, or about nodes, such as brokerage or centrality?
- What are ways to relate node attributes, such as gender or program, to ties or network position?
- Is there one "real" network, or do different measurements construct different observed networks?
- Construct the analysis-ready network object or objects and document decisions about direction, weight, node coverage, isolates, and absent versus unknown ties.
- Check node identifiers, edge endpoints, self-ties, duplicate ties, symmetry assumptions, and missing attributes.
- Commit to **one** primary network statistic for the project (e.g. assortativity by program/gender) and **one** permutation-style reference comparison. Do not try to cover multiple centrality measures, clustering, homophily, polarization, and temporal dynamics in the same project.


Prepare for roundtable in week 3:
- Be able to describe three analyses typically done on networks (e.g. assortativity, centrality, clustering) at a conceptual level, so the rest of the class understands the landscape, but your own project should report only the one statistic and one permutation comparison committed to above.
- Explain the selection vs influence debate in networks.



### Week 3 — Model, evaluate, and check sensitivity

Use a network-appropriate statistic and an appropriate model, and check sensitivity to preprocessing choices.
- How does using different operationalizations of the network impact the result?
- In your permutation test (if used), state exactly what is held fixed and what is randomized. Compare the observed result with the reference distribution and report an interpretable effect or discrepancy.
- Repeat the analysis under at least one alternative network measurement or operationalization.
- Which parameters, specifically, answer your research question?


Prepare for roundtable in week 4:
- Explain how network dependence impacts standard i.i.d. assumptions.
- Explain how the chosen network statistic or model works and what assumptions are hidden in the representation of ties.
- Explain how sensitive conclusions are to representation choices (e.g. type of network)


### Week 4 — Visualize and communicate a defensible claim

- What is the context? What is the main result? Why is it important?
- Which visualizations support our research findings?
- What are the assumptions and limitations of your design?

<!--
## Variant: College messaging dynamics

- Repository source: SNAP `CollegeMsg.txt.gz`.
- Raw formats to discuss: compressed temporal edge list, timestamps, directed ties.
- Main research question: Do early messaging patterns predict who becomes central later in the network?
- Alternative question 1: How concentrated is messaging activity across users?
- Alternative question 2: Does reciprocity differ between early and late windows?
- Expected model: windowed summaries plus a simple regression or permutation-based comparison.
- Why this fits the course: the core complexity is temporal network structure, not just an edge list.
-->
