# PubMad

Literature Mining Python Package

Develop a Python library that implements the literature mining pipeline seen in class: automatically query PubMed, download abstracts and full text if possible, perform named entity recognition, and generate a knowledge graph using either co-occurrences or relationship recognition. Include network analysis to identify nodes and edges imporatnt in the graph. Demonstrate for a set of metabolic diseases, identifying the drugs in the knowledge graph and the links to the various diseases.

Links:

https://www.sciencedirect.com/science/article/abs/pii/S0958166920301269

https://www.britannica.com/science/metabolic-disease

https://arxiv.org/pdf/1901.08746.pdf

https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-018-2167-5

https://github.com/dmis-lab/biobert


## Quick running guide

Clone this repo

> git clone git@github.com:Pier297/PubMad.git

CD in the directiory

> cd PubMad

Download the submodules by running:

> git submodule init

> git submodule update

Create the conda env

> conda create -n pubmad python=3.9

> conda activate pubmad

TODO: Installare i pacchetti (pytorch, ...)