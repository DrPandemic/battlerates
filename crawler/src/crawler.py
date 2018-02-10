import logging
from battlerite_client.client import Match, Response

class Crawler:
    def __init__(self, client, database, rate: int):
        """
        The rate is in op/minute.
        """
        self.client = client
        self.rate = rate

    def start(self) -> None:
        """
        Starts the infinite loop. It will call run at every tick.
        """
        self.run()

    def run(self) -> None:
        """
        Main loop.
        """
        response = self.client.matches()
        if response.success:
            self.save_matches(response.parse())
        else:
            logging.warning("Match query failed with: %s", response.raw.json())

    def save_matches(self, matches: [Match]) -> None:
        """
        Saves matches to db.
        """
        print([match.type for match in matches])
