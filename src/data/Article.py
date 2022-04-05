from typing import Optional
from dataclasses import dataclass

@dataclass
class Article:
    title: str
    abstract: Optional[str]
    pmid: str