from src.data.pubmed import download_articles
from src.data.Article import Article
import unittest
from typing import List

class TestPubmedDownloadData(unittest.TestCase):
    def test_download_data(self):
        data: List[Article] = download_articles(query='covid-19', max_results=10)
        self.assertEqual(len(data), 10)
        self.assertEqual(data[0].title, '')
        self.assertEqual(data[0].abstract, '')
        self.assertEqual(data[0].pmid, '')