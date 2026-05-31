from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class Favorite:
    title: str
    ingredients: List[str]
    instructions: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)