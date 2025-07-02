# Intro 

There is an entity with roles and obligations. But also with values. Values which are not always clear.

The entity is a world in itself. But it also exists in a larger content. Another world. We can call it the outside world, but actually it is reality.

The outside world is not separate from the entity. It contains the entity. The entity is a part of the outside world.

It is not possible to put the outside world inside the entity. It does not fit. Only a representation of the outside world fits within the entity.

It is not possible to put the outside world inside a piece of software. Only a representation of the outside world fits within a piece of software.

This piece of software is not the outside world. It is a representation of the outside world. It is not the entity. It is a representation of the entity.



# Roles

Entities likes to take on roles. It simplifies the rules how the should interact with other entities and behave in the outside world.
Some roles are offered by the outside world. Some roles are new. A result of the outside worlds inputs being scrambled into something new.

| Role                | Notes                                                                                                                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Full-time employee  | Certain jobs require certain skills and attributes. It is possible to work with a job where you do not fulfill the requirements, but it might have consequences on e.g. stress level. |
| Part-time employee  |                                                                                                                                                                                       |
| Student             |                                                                                                                                                                                       |
| Retired             |                                                                                                                                                                                       |
| Parent              |                                                                                                                                                                                       |
| Spouse              |                                                                                                                                                                                       |
| Child               |                                                                                                                                                                                       |
| Enthusiast          | Gardener, recreational exerciser, amateur musician, DIY hobbyist                                                                                                                      |
| Community organizer | Nonprofit group member, scout leader, activist, soccer coach for kids team                                                                                                            |
| Credential Role     | Academic degree                                                                                                                                                                       |

# Attributes

## Age
The entity is connected to a body. The body changes. Th

## Energy
Roles consume or generate energy. Why and how is not always clear. The only way to know is to continuosly be aware of energy levels via other systems.

## Stress

## Mental Capacity

# Skills

## Awareness
Being aware is a skill. It can be learned. By being aware if is easier to directly see things that might otherwise be harder to see.

## Occupational skill
Spending time with a task reinforces cognitive patterns. After a lot of time with a task the task will become automatic. It is often interpreted as skill.

# Resources

## Money

```
trueprosperity/
├── core/                    # Fundamental domain logic (Entity, Role, Resources, etc.)
│   ├── entity.py
│   ├── role.py
│   ├── resources.py
│   ├── snapshot.py
│   └── environment.py
│
├── simulation/             # Engine logic: time progression, policies, events
│   ├── engine.py
│   ├── policies.py
│   └── events.py
│
├── tools/                  # Individual tools built on top of core/simulation
│   ├── prosperity3d/       # Tool 1: Single-strategy lifetime simulation with visualization
│   │   ├── main.py
│   │   ├── strategy_selector.py
│   │   └── plotter.py
│   │
│   ├── lifepath_game/      # Tool 2: Game-like simulation with unlockable paths
│   │   ├── main.py
│   │   ├── game_state.py
│   │   └── ui_logic.py
│   │
│   └── worldsim/           # Tool 3: Multi-entity world-scale simulation
│       ├── main.py
│       ├── population_init.py
│       └── pattern_analysis.py
│
├── data/
│   ├── initial_entities.json
│   ├── role_templates.json
│   └── world_config.yaml
│
├── analysis/
│   ├── visualizer.py
│   ├── metrics.py
│   └── experiments.py
│
├── cli/
│   └── run_simulation.py
│
├── notebooks/
│   └── exploration.ipynb
│
├── tests/
│   └── test_simulation.py
│
├── README.md
└── pyproject.toml

```
