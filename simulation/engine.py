"""
Runs the chosen prosperity strategy simulation based on user input.

Responsible for instantiating the strategy class, running it, and returning results.
"""

from core.model import Entity, Identity, CollectiveMap

def run_simulation(inputs):
    # Initiera objekt enligt modellen
    entity = Entity(biological_age=inputs['calender_year'] - inputs['birth_year'])
    identity = Identity(entity_ref=entity, birth_year=inputs['birth_year'])
    world = CollectiveMap(calender_year=inputs['calender_year'], identities=[identity])

    # Initiera och kör strategi
    strategy = inputs['strategy_class'](inputs['strategy_name'])
    results = strategy.run(world)

    return results, inputs['strategy_name']

