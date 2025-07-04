# Core Model – TrueProsperity

```mermaid
classDiagram

  class CollectiveMap {
    +calender_year: int
    +identities: List~Identity~
  }

  class Identity {
    +entity_ref: Entity
    +birth_year: int
  }

  class Entity {
    +biological_age: int
  }

  CollectiveMap "1" *--> "many" Identity : contains
  Identity --> Entity : references