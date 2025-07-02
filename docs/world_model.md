# Strategiarkitektur – Tools (analogue with World)

```mermaid
classDiagram
  class World {
    +year: int
    +entities: List~Entity~
    +global_factors: List~Consequence~
    +available_roles: List~RoleTemplate~
    +simulate_year(): void
  }

  class Entity {
    +id: str
    +age: int
    +roles: List~Role~
    +history: List~YearSnapshot~
    +choose_roles(environment): void
    +react_to_consequences(conseqs): void
  }

  class RoleTemplate {
    +name: str
    +base_value(): float
    +resource_costs(): Resources
  }

  World --> Entity
  World --> RoleTemplate
  World --> Consequence
  Entity --> YearSnapshot
  Entity --> Role

