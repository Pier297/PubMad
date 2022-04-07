from typing import List, Optional, Tuple
from pymed import PubMed 
import json 
from Article import Article
from Entity import Entity

def download_articles(query: str, start_year: int, end_year: int, max_results: int = 100) -> List[Article]:
    """
    Download articles from PubMed.

    Args:
        query: The query to search for.
        start_year: The start year to search for.
        end_year: The end year to search for.
        max_results: The maximum number of results to return.

    Returns:
        A list of Articles.
    """
    pubmed = PubMed(tool="PubMad", email="m.natali10@studenti.unipi.it")
    results = pubmed.query("Some query", max_results=max_results)

    articles = []
    for article in results:
        article = article.toJSON()
        article = json.loads(article)
        articles.append(Article(title=article['title'], abstract=article['abstract'], 
                                pmid=article['pubmed_id'], full_text='', publication_data=''))
    return articles


def extract_entities(article: Article, source: str ='abstract | full_text') -> List[Entity]:
    """
    Extract entities from an article using BERN2 (online).

    Args:
        article: The article to extract entities from.

    Returns:
        A list of entities.
    """
    return []


def extract_naive_relations(article: Article, source: str ='abstract | full_text') -> List[Tuple[Entity]]:
    # Connect each entity returned from 'extract_entities' between all others.
    return []


#def get_graph(articles: List[Article], source: str ='abstract | full_text') -> Graph:
    pass
    # using NetworkX
    # and plot

def download_biobert():
    # download and save it somewhere..
    pass

def extract_relations_using_biobert(article: Article, source: str ='abstract | full_text') -> List[Tuple[Entity]]:
    pass

res = download_articles("alzhaimer", 2012, 2020)
print(res[1])