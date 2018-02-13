import logging
from enum import Enum
from battlerite_client.client import Match, Response

class Crawler:
    SAVE_TYPES = Enum('Save types', 'MATCH ROUND ROSTER PARTICIPANT PLAYER')

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

    def save(self, obj, connection, save_type: SAVE_TYPES) -> int:
        """
        Saves the obj into the DB.
        """
        if save_type == SAVE_TYPES.MATCH:
            raise NotImplementedError()
        if save_type == SAVE_TYPES.ROUND:
            raise NotImplementedError()
        if save_type == SAVE_TYPES.ROSTER:
            raise NotImplementedError()
        if save_type == SAVE_TYPES.PARTICIPANT:
            raise NotImplementedError()
        if save_type == SAVE_TYPES.PLAYER:
            raise NotImplementedError()
        else:
            raise NotImplementedError()