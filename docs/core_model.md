# Core Model – TrueProsperity

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
    +savings: float
    +retirement_funds: float
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

  class Role {
    +get_time_demand(year: int): float
    +get_value_contribution(year: int): float
    +get_resource_requirements(year: int): Resources
  }

  class Resources {
    +time: float
    +money: float
    +emotional_energy: float
  }

  class YearSnapshot {
    +year: int
    +total_spent_time: float
    +total_value: float
    +resource_balance: Resources
    +consequences: List~Consequence~
  }

  class Consequence {
    +description: str
    +impact_on_roles(): void
    +impact_on_capacities(): void
  }

  World --> Entity
  World --> RoleTemplate
  World --> Consequence
  Entity --> YearSnapshot
  Entity --> Role
  Role --> Resources
  YearSnapshot --> Resources
  YearSnapshot --> Consequence
