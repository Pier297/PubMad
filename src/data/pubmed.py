from html import entities
from typing import List, Optional, Tuple
from pymed import PubMed 
import json 
import requests
import networkx as nx
from datetime import datetime
from itertools import product
from Article import Article
from Entity import Entity 

def download_articles(query: str, start_year: int, end_year: int, max_results: int = 100) -> List[Article]:
    """
    Download articles from PubMed.

    Args:
        query: The query to search for. 
        start_year: The start year to search for.
        end_year: The end year to search for. 
        max_results: The maximum number of results to return. Defaults to 100.

    Returns:
        A list of Articles.
    """
    pubmed = PubMed(tool="PubMad", email="m.natali10@studenti.unipi.it")
    results = pubmed.query('(' + query + '[Title])' + ' AND ' + '(("' + str(start_year) + '"[Date - Create] :"' + str(end_year) + '"[Date - Create]))', max_results=max_results)

    articles = []
    for article in results:
        article = article.toJSON()
        article = json.loads(article)
        articles.append(Article(title=article['title'], abstract=article['abstract'], 
                                pmid=article['pubmed_id'], full_text='', publication_data=datetime.strptime(article['publication_date'], '%Y-%m-%d')))
    #print(articles[0])
    return articles


def query_plain(text, url="http://bern2.korea.ac.kr/plain"):
    """
    Query the BERN2 server for plain text.
    """
    result = requests.post(url, json={'text': text})
    if result.status_code != 200:
        raise ValueError("Error {}: {}".format(result.status_code, result.text))
    return result.json()
def extract_entities(article: Article, source: str ='abstract') -> List[Entity]:
    """
    Extract entities from an article using BERN2 (online).

    Args:
        article: The article to extract entities from. 
        source: The source to extract entities from. Can be 'abstract' or 'full_text'. Defaults to 'abstract'. 

    Returns:
        A list of entities. 
    """

    text = ''
    if source == 'abstract':
        text = article.abstract
    elif source == 'full_text':
        text = article.full_text        
    else:
        raise ValueError("Invalid source: {}".format(source))

    # Query BERN2 server for entities.
    bern_result = query_plain(text)

    # Parse the result.
    annotations = bern_result['annotations']
    entities = []
    for entity in annotations:
        if (entity['obj'] == 'disease' or entity['obj'] == 'gene'):
            new_entity = Entity(id=entity['id'], mention=entity['mention'], obj=entity['obj'], prob=entity['prob'], span_begin=entity['span']['begin'], span_end=entity['span']['end'])
            entities.append(new_entity)

    return entities

def mask_entities(article : Article, entities: List[Entity]) -> List[str]:
    """
    Mask entities in an article.

    Args:
        article: The article to mask entities in. 
        entities: The entities to mask. 

    Returns:
        A list of masked articles. 
    """

    abstract = article.abstract

    #divide entities in gene and disease entities
    gene_entities = []
    disease_entities = []
    for entity in entities:
        if (entity.obj == "disease"):
            disease_entities.append(entity)
        else:
            gene_entities.append(entity)

    masked_articles = []
    for gene_entity in gene_entities:
        for disease_entity in disease_entities:
            if (gene_entity.span_begin < disease_entity.span_begin):
                masked_articles.append(abstract[:gene_entity.span_begin] + "@GENE$" + abstract[gene_entity.span_end:disease_entity.span_begin] + "@DISEASE$" + abstract[disease_entity.span_end:])
            else:
                masked_articles.append(abstract[:disease_entity.span_begin] + "@DISEASE$" + abstract[disease_entity.span_end:gene_entity.span_begin] + "@GENE$" + abstract[gene_entity.span_end:])
  
    return masked_articles

def extract_naive_relations(articles: List[Article], source: str ='abstract | full_text') -> List[Tuple[Entity]]:
    # Connect each entity returned from 'extract_entities' between all others.

    # lasciata vuota senn?? dovevo ricomputare entity qua dentro inutilmente

    return []


def get_graph(articles: List[Article], source: str ='abstract') -> nx.Graph:
    # using NetworkX
    # and plot

    if source != 'abstract' and source != 'full_text':
        raise ValueError("Invalid source: {}".format(source))


    G = nx.Graph()

    nodelist = []

    # adding nodes
    for article in articles:
      entities = extract_entities(article, source=source)
      for entity in entities:
        nodelist.append(entity.get_dictionary())
      G.add_nodes_from(nodelist)
      nodelist = []

    #??adding relationship 
    G.add_edges_from((a,b) for a,b in product(list(G.nodes()), list(G.nodes())) if a != b)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=700)

def download_biobert():
    # download and save it somewhere..
    pass

def extract_relations_using_biobert(article: Article, source: str ='abstract | full_text') -> List[Tuple[Entity]]:
    pass


if __name__ == "__main__":
    res = download_articles("alzheimer", 2012, 2020)
    
    print('\n\n\n')
    
    print(res[1])

    print('\n\n\n')

    print(extract_entities(res[1]))