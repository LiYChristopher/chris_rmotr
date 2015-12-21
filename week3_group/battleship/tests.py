''' Test suite for battlefield.py

Status - Incomplete:
- Player
- AI
- GameEngine
'''

from unittest import TestCase
from mock import patch, Mock

class GridTest(TestCase):

	@classmethod
	def setUpClass(cls):
		from battleship import Grid
		from colorama import Fore
		cls.grid = Grid()

	@classmethod
	def tearDownClass(cls):
		del cls.grid

	def test_length_grid(self):
		self.assertEqual(len(self.grid.grid.keys()), 100)

	def test_first_grid(self):
		self.assertEqual(self.grid.grid.keys()[0], 'A1')

	def test_last_grid(self):
		self.assertEqual(self.grid.grid.keys()[-1], 'J10')

	@patch('battleship.Aircraft', autospec=True)
	@patch('battleship.Submarine', autospec=True)
	def test_place_grid(self, aircraft_carrier, submarine):
		from colorama import Fore
		ac_attr = {'position': ['A1', 'A2', 'A3', 'A4', 'A5'],
		 	      'marker': Fore.WHITE + 'A|'}
		sub_attr = {'position': ['G1', 'H1', 'I1'],
					'marker': Fore.WHITE + 'S|'}

		aircraft_carrier.configure_mock(**ac_attr)
		submarine.configure_mock(**sub_attr)
		ships = [aircraft_carrier, submarine]
		self.grid.place(*ships)
		blank = Fore.BLUE + '_|'

		ships = set(filter(lambda x: x if self.grid.grid[x] != blank else None,
										self.grid.grid.keys()))
		self.assertEqual(ships, set(['G1', 'I1', 'H1', 'A1',
									'A3', 'A2', 'A5', 'A4']))

class ShipTest(TestCase):

	@classmethod
	def setUpClass(cls):
		from battleship import Ship, Aircraft
		from battleship import PatrolBoat, Submarine
		cls.base_ship = Ship(['G1', 'G2', 'G3'], 'h')
		cls.aircraft_carrier = Aircraft(['E1', 'F1', 'G1', 'H1', 'I1'], 'v')
		cls.patrol_boat = PatrolBoat(['E2', 'F2'], 'v')
		cls.submarine = Submarine(['E3', 'F3', 'G3'], 'v')

	@classmethod
	def tearDownClass(cls):
		del cls.base_ship
		del cls.aircraft_carrier
		del cls.patrol_boat
		del cls.submarine

	def test_default_size_aircraft(self):
		self.assertEqual(self.aircraft_carrier.size, 5)

	def test_default_size_patrol_boat(self):
		self.assertEqual(self.patrol_boat.size, 2)

	def test_default_size_submarine(self):
		self.assertEqual(self.submarine.size, 3)

	def test_position_submarine(self):
		self.assertEqual(self.submarine.position, ['E3', 'F3', 'G3'])

	def test_no_marker_ship(self):
		self.assertEqual(self.base_ship.marker, None)

class PlayerTest(TestCase):

	@classmethod
	def setUpClass(cls):
		from battleship import Player
		cls.player = Player('Test')

	@patch('battleship.AI', autospec=True)
	def test_attack_player(self, AI):
		from colorama import Fore
		from battleship import Grid

		AI_attr = {'grid': Grid()}
		AI.configure_mock(**AI_attr)
		AI.grid.grid['G2'], AI.grid.grid['G3'] = (Fore.WHITE + 'P|',)*2
		self.player.enemy = AI.grid
		self.player.attack()

	@classmethod
	def tearDownClass(cls):
		pass
