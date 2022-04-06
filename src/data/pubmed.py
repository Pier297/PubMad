from typing import List, Optional, Tuple
from src.data.Article import Article
from src.data.Entity import Entity

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
    return [Article(title='', abstract='', pmid='', full_text='') for _ in range(max_results)]


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


def get_graph(articles: List[Article], source: str ='abstract | full_text') -> Graph:
    pass
    # using NetworkX
    # and plot

def download_biobert():
    # download and save it somewhere..
    pass

def extract_relations_using_biobert(article: Article, source: str ='abstract | full_text') -> List[Tuple[Entity]]:
    pass
