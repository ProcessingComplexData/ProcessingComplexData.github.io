# Network Projects

- Project name: `networks`
- Research question (example): __What is the relationship between gender and cross-program relations in high school?__
- Expert contact: `Javier Garcia-Bernardo`

- Programming language:  `python` (suggested) or `R` (allowed)

> **Canonical course conventions live in [project_guidelines.md](../project_guidelines.md).** That file is the source of truth for the four required workflow files (`week1_explore.qmd`, `week2_operationalize_clean.qmd`, `week3_model.qmd`, `week4_storytelling.qmd`), the `data/model_data.rds` -> `data/model_results.rds` pipeline, the raw-data policy, quality-check requirements, decision logs, and contribution tracking. Read it before starting and treat anything below as project-specific guidance on top of those conventions.

## Tutorial framing

Network data are complex because observations are connected through ties, direction, weights, missing nodes and ties, and dependence between relations rather than data structured as independent rows in a single analysis-ready table.

Students should learn three main things about these data:
1. How networks are represented through nodes, edges, edge lists, adjacency matrices, sparse matrices, GraphML, and how to make critical choices about direction, weight, time, and isolates.
2. How to turn raw graph files into a clean network object while documenting what counts as a node, what counts as a tie, and which representation best matches the research question.
3. How network dependence affects standard statistical assumptions, and how network statistics, reference models, permutation tests, or clustering can support claims about homophily, polarization, centrality, or other network structures.

## Peer-teaching checklist

| Dimension | This project teaches |
|---|---|
| Data structure | Graphs with nodes, edges, node attributes, edge attributes, edge lists, adjacency matrices, and sparse matrix representations. |
| Storage system | File-based network repositories and downloaded graph files. |
| File formats | CSV edge lists, GraphML, and compressed repository downloads where relevant. |
| Encoding | Text CSV and XML-based GraphML. |
| Model | Assortativity or homophily statistic, permutation test, clustering, or a small network summary model. |
| Key aspects to explain | What counts as a node or tie, directed vs. undirected graphs, weighted vs. unweighted ties, isolates, sparse vs. dense matrices, network visualization, and why network dependence violates ordinary i.i.d. assumptions. |

## Resources
### Data sources
- Network data:
  - Stanford Large Network Dataset Collection: https://snap.stanford.edu/data/
  - Network repository: https://networkrepository.com/networks.php
  - Netzschleuder: https://networks.sweked.de
  - Index of Complex Networks: https://icon.colorado.edu
- Potential dataset: https://networks.skewed.de/net/sp_high_school (interactive viz: https://javier.science/panel_network/)


### Knowledge sources
- C/R/Python packages `igraph`
- Introduction to networks
  - Chapter 0 of "A First Course in Network Science": https://github.com/CambridgeUniversityPress/FirstCourseNetworkScience/blob/master/sample/chapters/chapter0.pdf
  - App: https://javier.science/marimo_intro_networks/
- Guide for reference models: https://pubmed.ncbi.nlm.nih.gov/34216192/
- Observed vs latent networks: https://www.nature.com/articles/s41467-022-34267-9


## Week-by-week
### Week 1:
Begin with raw repository files and explain what the network is, who generated it, for what purpose, and the different storage formats.
- Explain the underlying network in substantive terms: what the nodes and ties represent, and whether the graph is directed or undirected, weighted or unweighted, static or temporal.
- What is the GraphML data type? How does it relate to XML? How is this different from other network data types?
- Are adjacency matrices sparse or dense?
- Read about different visualization layout algorithms. Explore static/interactive visualization tools.


Prepare for roundtable in week 2:
- What is a network and why is it a useful representation of data?
- What are the main ways to represent a network: edge lists, adjacency matrices, and XML or GraphML-like?
- What are the advantages and disadvantages of adjacency matrices over edge lists? How do sparse matrices fix this and what are they?
- How do you visualize a network? What could be the pitfalls of having your analysis based on the network visualization only?


### Week 2:
Operationalize the research question by turning raw graph files into a clean file with explicit decisions about direction, weights, and isolates.


- Think about the difference between network-wide questions like homophily or polarization and node-level questions like brokerage or node centrality.
- What are ways to measure the relationships between a node attribute (e.g. gender) and an edge attribute (cross-program relationships)?
- What is the "real" network?
- Commit to **one** primary network statistic for the project (e.g. assortativity by program/gender) and **one** permutation-style reference comparison. Do not try to cover multiple centrality measures, clustering, homophily, polarization, and temporal dynamics in the same project.


Prepare for roundtable in week 3:
- Be able to describe three analyses typically done on networks (e.g. assortativity, centrality, clustering) at a conceptual level, so the rest of the class understands the landscape, but your own project should report only the one statistic and one permutation comparison committed to above.
- Explain the selection vs influence debate in networks.



### Week 3:
Use a network-appropriate statistic and an appropriate model, and check sensitivity to preprocessing choices.
- How does using different operationalizations of the network impact the result?
- Which parameters, specifically, answer our research question?


Prepare for roundtable in week 4:
- Explain how network dependence impacts standard i.i.d. assumptions
- Explain how the chosen network statistic or model works and what assumptions are hidden in the representation of ties.
- Explain how sensitive conclusions are to representation choices (e.g. type of network)


### Week 4
Visualize and tell a story
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
