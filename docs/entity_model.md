# Strategiarkitektur – TrueProsperity

```mermaid
classDiagram
  class Entity {
    +age: int
    +savings: float
    +retirement_funds: float
    +roles: List~Role~
    +history: List~YearSnapshot~
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

  Entity *--> Role
  Entity *--> YearSnapshot
  Role --> Resources
  YearSnapshot --> Resources
  YearSnapshot --> Consequence
