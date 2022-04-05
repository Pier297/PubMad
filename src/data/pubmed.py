from typing import List, Optional
from src.data.Article import Article

def download_articles(query: str, max_results: int = 100) -> List[str]:
    """
    Download articles from PubMed.

    Args:
        query: The query to search for.
        max_results: The maximum number of results to return.

    Returns:
        A list of article IDs.
    """
    return [Article(title='', abstract='', pmid='') for _ in range(max_results)]