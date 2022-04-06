from typing import Optional
from dataclasses import dataclass

@dataclass
class Article:
    title: str
    abstract: Optional[str]
    full_text: Optional[str]
    pmid: str