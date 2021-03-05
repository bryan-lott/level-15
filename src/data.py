from dataclasses import dataclass, field
from collections import defaultdict
from functools import partial
from uuid import UUID, uuid4
from typing import Dict, Tuple, List


@dataclass
class Card:
    id: UUID = field(default_factory=uuid4)
    keywords: defaultdict = field(default_factory=partial(defaultdict, int))
    text: str = ""


@dataclass
class DB:
    id_to_card: Dict[UUID, Card] = field(default_factory=dict)
    word_to_cards: Dict[str, List[Tuple[UUID, int]]] = field(default_factory=dict)


def sort_by_word_count(l: List[Tuple[UUID, int]]):
    return sorted(l, key=lambda t: t[1], reverse=True)
