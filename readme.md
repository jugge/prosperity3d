# Intro 

There is an entity with roles and obligations. But also with values. Values which are not always clear.

The entity is a world in itself. But it also exists in a larger content. Another world. We can call it the outside world, but actually it is reality.

The outside world is not separate from the entity. It contains the entity. The entity is a part of the outside world.

It is not possible to put the outside world inside the entity. It does not fit. Only a representation of the outside world fits within the entity.

It is not possible to put the outside world inside a piece of software. Only a representation of the outside world fits within a piece of software.

This piece of software is not the outside world. It is a representation of the outside world. It is not the entity. It is a representation of the entity.

# Structure

```
trueprosperity/
├── core/
│   ├── entity.py              # Defines the Entity class: age, roles, snapshots
│   ├── role.py                # Role and RoleTemplate logic: value contribution, resource needs
│   ├── resources.py           # Defines the Resources class: time, money, emotional_energy
│   ├── snapshot.py            # YearSnapshot and Consequence classes
│   └── environment.py         # The World / Environment simulation context
│
├── simulation/
│   ├── engine.py              # Main simulation loop: advances time, updates world and entities
│   ├── policies.py            # Global rulesets: e.g. economic systems, welfare models
│   └── events.py              # Major global events: pandemics, wars, climate shifts
│
├── data/
│   ├── initial_entities.json  # Starting configuration for simulated population
│   ├── role_templates.json    # Definitions for available role types in the world
│   └── world_config.yaml      # World settings: starting year, parameters, constraints
│
├── analysis/
│   ├── visualizer.py          # Tools for plotting resource flows, roles, value over time
│   ├── metrics.py             # System-wide indicators: wellbeing, survival, stagnation
│   └── experiments.py         # Code for running different configurations and comparing them
│
├── cli/
│   └── run_simulation.py      # Command-line interface for running and exporting simulations
│
├── notebooks/
│   └── exploration.ipynb      # Jupyter notebook for fast prototyping and hypothesis testing
│
├── tests/
│   └── test_simulation.py     # Unit tests for the main logic
│
├── README.md
└── pyproject.toml
```
