from typing import List

class Entity:
    def __init__(self, biological_age: int):
        self.biological_age = biological_age

class Identity:
    def __init__(self, entity_ref: Entity, birth_year: int):
        self.entity_ref = entity_ref
        self.birth_year = birth_year

class CollectiveMap:
    def __init__(self, calender_year: int, identities: List[Identity]):
        self.calender_year = calender_year
        self.identities = identities

    def __repr__(self):
        return (
            f"CollectiveMap(year={self.calender_year}, "
            f"identities=[{', '.join(f'age={id.entity_ref.biological_age}' for id in self.identities)}])"
        )
