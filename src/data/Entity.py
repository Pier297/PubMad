from itertools import tee
from tokenize import Number
from typing import Optional
from dataclasses import dataclass

from matplotlib.pyplot import text

@dataclass
class Entity:
    id: str
    mention: str
    obj: str
    prob: float
    span_begin: int
    span_end: int

    def get_dictionary(self):
      return (self.id[0], {'mention': self.mention, 'obj' : self.obj, 'prob':self.prob})