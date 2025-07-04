# Core Model – TrueProsperity

```mermaid
classDiagram
  class Entity {
    +id: str
    +roles: List~Role~
    +attributes: Attributes
    +skills: Skills
    +resources: Resources
    +history: List~YearSnapshot~
    +choose_roles(environment): void
    +react_to_consequences(conseqs): void
  }

  class Role {
    +name: str
    +notes: str
    +requirements: List~Requirement~
    +possible_consequences: List~Consequence~
    +consume_resources(entity: Entity): void
  }

  class Attributes {
    +age: int
    +energy: float
    +stress: float
    +mental_capacity: float
  }

  class Skills {
    +awareness: float
    +occupational_skill: float
  }

  class Resources {
    +money: float
  }

  class Requirement {
    +type: str
    +value: any
  }

  class YearSnapshot {
    +year: int
    +spent_time: float
    +resource_balance: Resources
    +consequences: List~Consequence~
  }

  class Consequence {
    +description: str
    +impact_on_roles(entity: Entity): void
    +impact_on_attributes(entity: Entity): void
  }

  class World {
    +year: int
    +entities: List~Entity~
    +global_factors: List~Consequence~
    +available_roles: List~Role~
    +simulate_year(): void
  }

  Entity --> Role
  Entity --> Attributes
  Entity --> Skills
  Entity --> Resources
  Entity --> YearSnapshot
  Role --> Requirement
  YearSnapshot --> Resources
  YearSnapshot --> Consequence
  World --> Entity
  World --> Role
  World --> Consequence
