class TaughtLife:
    def __init__(self, name):
        self.name = name

    def run(self, world):
        # Dummystrategi som visar upp världens tillstånd
        results = {
            "year": world.calender_year,
            "ages": [id.entity_ref.biological_age for id in world.identities]
        }
        return results
