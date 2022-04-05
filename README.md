# BioSearch

Literature Mining Python Package

Develop a Python library that implements the literature mining pipeline seen in class: automatically query PubMed, download abstracts and full text if possible, perform named entity recognition, and generate a knowledge graph using either co-occurrences or relationship recognition. Include network analysis to identify nodes and edges imporatnt in the graph. Demonstrate for a set of metabolic diseases, identifying the drugs in the knowledge graph and the links to the various diseases.

Links:

https://www.sciencedirect.com/science/article/abs/pii/S0958166920301269

https://www.britannica.com/science/metabolic-disease

https://arxiv.org/pdf/1901.08746.pdf

https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2167-5

https://github.com/dmis-lab/biobert


## Quick running guide

### Create Conda Environment

To use first create a Conda environment with the required packages by running:

> conda env create -f environment.yml

Then activate the created 'biosearch' env:

> conda activate biosearch

### Download PubMed data

