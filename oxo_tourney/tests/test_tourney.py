from unittest import TestCase

from hamcrest import assert_that, equal_to
from oxo_tourney.player import ExamplePlayer
from oxo_tourney.tourney import Tourney


class TestTourney(TestCase):
    def test_start_returns_2_results_when_2_players_passed_in(self):
        player_list = [ExamplePlayer(""), ExamplePlayer("")]
        tourney = Tourney(player_list)

        results = tourney.start()

        assert_that(len(results), equal_to(2))