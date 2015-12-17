''' implementing battleship
'''

from __future__ import division
from colorama import Fore, Style, init
from collections import OrderedDict
from random import randint, choice

init(autoreset=True)

class Grid(object):
    ''' 10x10 (A1-J10) Grid via OrderedDict where ships reside. '''
    def __init__(self):
        self._inputs = [i+str(j) for i in map(chr, range(65, 75)) for j in range(1, 11)]
        self.grid = OrderedDict(zip(self._inputs, [Fore.BLUE + '_|']*len(self._inputs)))

    def __repr__(self):
        return 'Grid({})'.format(self.grid)

    def __str__(self):
        ''' Need to implement a way to show the grid in a good format '''
        for row in range(65, 75):
            row_idx = chr(row)
            row_keys = filter(lambda key: key if key.startswith(row_idx)
                                else None, self.grid.keys())
            row = [self.grid[e] for e in row_keys]
            print ''.join(row)
        return '\n'

    def place(self, *ships):
        ''' takes in a list of ships and places them on the grid if ships fit
            otherwise throws and OutOfBoundsError.
            #TODO: Need to implement this
        '''
        for ship in ships:
            for loc in ship.position:
                self.grid[loc] = ship.marker


class Ship(object):
    ''' Base ship class '''
    def __init__(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def __repr__(self):
        # nice to have a repr which shows the actual subclass names
        return '{cls}({p}, {o})'.format(cls=self.__class__.__name__,
                                             p=self.position,
                                             o=self.orientation)


class Aircraft(Ship):
    ''' Aircraft class '''
    def __init__(self, position, orientation):
        super(Aircraft, self).__init__(position, orientation)
        self.marker = Fore.WHITE + 'A|'
        self.size = 5


class Submarine(Ship):
    ''' Submarine class '''
    def __init__(self, position, orientation):
        super(Submarine, self).__init__(position, orientation)
        self.marker = Fore.WHITE + 'S|'
        self.size = 3


class PatrolBoat(Ship):
    ''' PatrolBoat class '''
    def __init__(self, position, orientation):
        super(PatrolBoat, self).__init__(position, orientation)
        self.marker = Fore.WHITE + 'P|'
        self.size = 2


class Player(object):

    markers = {'water': Fore.BLUE + '_|',
               'hit': Fore.RED + 'X|',
               'miss': Fore.BLUE + 'O|'}

    def __init__(self, name):
        self.name = name
        self.grid = Grid()
        self.enemy = None  # grid only
        self.active = False
        self.shipyard = Shipyard(self)
        self.ship_locations = set([])
        self.locations_already_fired = set([])
        self.ship_objs = self.shipyard.shipyard()

        self.shots_fired = 0
        self.shots_landed = 0
        self.highest_streak = 0
        self.streak_track = 0
        self.misscalls = 0
        self.shots_fired = 0

    def attack(self):
        ''' If AI - Attack random space, until a ship is hit. After, try and
        hit surrounding spaces to destroy remainder of ship.

        If human - select coordinate, fire missile.
        '''
        coordinate = ''
        while coordinate not in self.grid.grid.keys():
            coordinate = raw_input("Where would you like to fire? > ")
        self.locations_already_fired.add(coordinate)
        if coordinate in self.locations_already_fired:
            self.misscalls += 1

        print "{0} Firing at ... {1}".format(self.name, coordinate)
        if self.enemy[coordinate] not in self.markers.values():
            print "You've hit a ship!"
            self.enemy[coordinate] = self.markers['hit']
            self.shots_fired += 1
            self.shots_landed += 1
            self.streak_track += 1
        else:
            print "You missed ..."
            if self.enemy[coordinate] == self.markers['hit']:
                pass
            else:
                self.enemy[coordinate] = self.markers['miss']

            if self.streak_track > self.highest_streak:
                self.highest_streak += self.streak_track
            self.streak_track = 0
            self.shots_fired += 1
        return coordinate

    def defend(self, coordinate):
        ''' If AI - Adjust board if missile hits ship

        If human - Engage in interactions to confirm impact of missile, reflect
        changes on grid.
        '''
        confirm = ''
        while confirm not in ['y', 'n']:
            msg = 'Shot fired at {0}. Was there contact? (y/n) > '.format(coordinate)
            confirm = raw_input(msg)
        if confirm == 'y' and self.grid.grid[coordinate] == self.markers['hit']:
            print "Contact confirmed."
        elif confirm == 'n' and self.grid.grid[coordinate] == self.markers['hit']:
            print "False. Contact has been confirmed."
            self.misscalls += 1
        else:
            print "The enemy has missed. Phew!"
        return


class AI(Player):

    enemy_names = ['Lord Cthulu', 'Blackbeard']

    def __init__(self):
        super(AI, self).__init__(choice(self.enemy_names))
        self.latest_strike = None
        self.planned_strikes = set([])
        self.planned_missed_strikes = 0
        self.shipyard = Shipyard(self)
        self.ship_objs = self.shipyard.shipyard()

        self.shots_fired = 0
        self.shots_landed = 0
        self.highest_streak = 0
        self.streak_track = 0
        self.misscalls = 'N/A'
        self.shots_fired = 0

    def attack(self):
        if len(self.planned_strikes) >= 1:
            coordinate = self.planned_strikes.pop()
            print 'Planned coordinate ....', coordinate
        else:
            coordinate = choice(self.grid.grid.keys())
        print "{0} Firing at ... {1}".format(self.name, coordinate)
        if self.enemy[coordinate] not in self.markers.values():
            print "You've hit a ship!"
            self.enemy[coordinate] = self.markers['hit']
            self.shots_fired += 1
            self.shots_landed += 1
            self.streak_track += 1
            self.latest_strike = coordinate
            self.plan_strikes(coordinate)
        else:
            print "{0} missed ...".format(self.name)
            if coordinate in self.planned_strikes:
                self.planned_missed_strikes += 1
                if self.planned_missed_strikes >= 5:
                    self.abandon_plan_strikes()
            if self.enemy[coordinate] == self.markers['hit']:
                pass
            else:
                self.enemy[coordinate] = self.markers['miss']
            if self.streak_track > self.highest_streak:
                self.highest_streak += self.streak_track
            self.streak_track = 0
            self.shots_fired += 1
        return coordinate

    def defend(self, coordinate):
        pass

    def plan_strikes(self, hit):
        ''' Based on a successful strike, build a list
        of coordinates for potential future successful strikes.
        '''
        u = [chr(i) + hit[1] for i in range(ord(hit[0]) - 4, ord(hit[0]))]
        d = [chr(i) + hit[1] for i in range(ord(hit[0]) + 1, ord(hit[0]) + 5)]
        l = [hit[0] + chr(i) for i in range(ord(hit[1]) - 4, ord(hit[1]))]
        r = [hit[0] + chr(i) for i in range(ord(hit[1]) + 1, ord(hit[1]) + 5)]

        print 'UP', u
        print 'DOWN', d
        print 'LEFT', l
        print 'RIGHT', r

        check = lambda x: x if x in self.grid.grid.keys() else None
        check2 = lambda x: x if x in self.locations_already_fired else None

        self.planned_strikes |= set((filter(lambda x: x if check2(check(x)) else None, u)))
        self.planned_strikes |= set((filter(lambda x: x if check2(check(x)) else None, u)))
        self.planned_strikes |= set((filter(lambda x: x if check2(check(x)) else None, u)))
        self.planned_strikes |= set((filter(lambda x: x if check2(check(x)) else None, u)))
        print 'PLANNED STRIKES: ', self.planned_strikes
        return

    def abandon_plan_strikes(self):
        self.planned_strikes = set([])
        return


class GameEngine(object):
    '''
    This class control gamestate, and regulates flow
    '''

    def __init__(self):
        self.players = []
        self.ship_quant = self.query_ship_quant()

    def query_ship_quant(self):
        acceptable_answers = ['3', '4', '5']
        while True:
            user_input = raw_input('Enter the number of ships (3-5): >')
            if user_input not in acceptable_answers:
                continue
            else:
                return int(user_input)

    def turn(self):
        ''' Rotates defender and attacker, orchestrates appropriate behaviors
        for both.
        '''
        coordinate = None
        attacker = filter(lambda x: x if x.active else None,
                          self.players)[0]
        defender = filter(lambda x: x if not x.active else None,
                          self.players)[0]

        # print Grids, conduct appropriate responses. Set 'active' to new values
        print Fore.WHITE + Style.BRIGHT + "\nIt's {}'s turn to attack!".format(attacker.name)

        if not isinstance(attacker, AI):
            print '\n', attacker.grid

        elif not isinstance(defender, AI):
            pass

        coordinate = attacker.attack()
        defender.defend(coordinate)
        attacker.active, defender.active = False, True
        return

    def set_rotation(self):
        ''' Randomly selects first player,
        setting their 'active' attribute to true. '''
        first_player = choice(self.players)
        print "{} has been selected to go first.".format(first_player.name)
        first_player.active = True

    def initialize(self):
        ''' Game setup - Set up grids, place ships, set rotation. '''
        player_name = raw_input("What's your name, captain? > ")
        self.player = Player(player_name)
        self.computer = AI()
        player_grid, computer_grid = self.player.grid, self.computer.grid
        computer_grid.place(*self.computer.ship_objs)
        player_grid.place(*self.player.ship_objs)

        # Sets enemy attribute to the opposing player
        self.player.enemy = computer_grid.grid
        self.computer.enemy = player_grid.grid
        self.players.append(self.player)
        self.players.append(self.computer)

        # Select who goes first
        self.set_rotation()

    def detect_win(self):
        ''' If all ships have been destroyed: stop the game
        and then generate statistics. '''
        player_test = set(self.player.grid.grid.values())
        computer_test = set(self.computer.grid.grid.values())

        #print 'PLAYER TEST', player_test
        #print 'COMPUTER TEST', computer_test
        win = set([self.player.markers['hit'],
                   self.player.markers['miss'],
                   self.player.markers['water']])

        if player_test == win:
            print "All of {}'s ships are destroyed.".format(self.player.name)
            print "{} has won the game!".format(self.computer.name)
        elif computer_test == win:
            print "All of {}'s ships are destroyed.".format(self.computer.name)
            print "{} has won the game!".format(self.player.name)
        else:
            return False
        return True

    def game_summary(self):
        ''' Generate and display game statistics. '''
        for p in self.players:
            print "\nName: {}".format(p.name)
            print "\t Hit Percentage: {0:.2f}% ({1}/{2})".format((p.shots_landed / p.shots_fired) * 100,
                                                                 p.shots_landed, p.shots_fired)
            print "\t Longest Streak: {}".format(p.highest_streak)
            print "\t # of Miss-calls: {}".format(p.misscalls)

    def play(self):

        while not self.detect_win():

            self.turn()

        self.game_summary()
        return


class Shipyard(object):
    '''
    Class to hold helper functions
    '''
    g = Grid()

    def __init__(self, player):
        self.available_ship_type = [Submarine, Aircraft, PatrolBoat]
        self.player = player
        self.human = False if isinstance(player, AI) else True

    def in_bounds(self, position):
        '''
        Evualates if a position is in bounds == conforms to A1 - J10.
        Returns boolean.
        '''
        for p in position:
            if p not in self.g.grid.keys():
                return False
        return True

    def placement(self, position, size, orientation):
        '''
        Outputs a list of coordinates for a potential ship with orientation.
        Example output: [['A1', 'A2', 'A3'],'h']
        '''
        place_y, place_x = position[0], int(position[1])

        if orientation == 'h':
            allocation = [place_y + str(i) for i in range(place_x,
                          place_x + size)]

        elif orientation == 'v':
            allocation = [chr(i) + str(place_x) for i in range(ord(place_y),
                          ord(place_y) + size)]

        return allocation

    def is_in_locations(self, potential_new_ship):
        '''
        Inputs ship candidate and compares against all coordinates
        in Player.ship_locations to make sure there is no overlap.
        Return boolean. True == is in list, False == not in list
        '''
        for point in potential_new_ship:
            if point in self.player.ship_locations:
                return True
        return False

    def rand_ship(self, ship_type):

        position = choice(self.g.grid.keys())
        orientation = choice(['h', 'v'])

        if ship_type is Submarine:
            size = 3
        elif ship_type is Aircraft:
            size = 5
        else:
            size = 2

        potential_ship = self.placement(position, size, orientation)
        return ship_type(potential_ship, orientation)

    def choose_ship(self, ship_type):
        ''' For the human player. '''

        print "\nCurrent occupied tiles:", self.player.ship_locations

        if ship_type is Submarine:
            print "Please choose coordinates for your Submarine."
            size = 3
        elif ship_type is Aircraft:
            print "Please choose coordinates for your Aircraft Carrier."
            size = 5
        else:
            print "Please choose coordinates for your Patrol Boat."
            size = 2

        while True:
            position = ''
            orientation = ''

            while position not in self.g.grid.keys():
                position = raw_input("Place ship at what coordinate? (A1-J10) > ")

            while orientation not in ['h', 'v']:
                orientation = raw_input("Orientation? ('h' or 'v') > ").lower()

            potential_ship = self.placement(position, size, orientation)
            if not self.validate_ship(potential_ship):
                print "Sorry, your ship is in conflict (out of bonds, or colliding)."
                print "Please try setting it again!"
                continue 
            return ship_type(potential_ship, orientation)
        return

    def validate_ship(self, potential_ship_position):
        # collision
        if self.is_in_locations(potential_ship_position):
            return False
        # out of bounds check
        if not self.in_bounds(potential_ship_position):
            return False
        else:
            self.player.ship_locations = self.player.ship_locations | set(potential_ship_position)
            return True

    def shipyard(self):
        '''
        Outputs 'fleet' of ships based of quantity set by user.
        First 3 ships will be Submarine, Aircraft, PatrolBoat,
        all optional ships will be randomly chosen from that list
        '''
        fleet = []
        quantity = game.ship_quant
        build_queue = list(self.available_ship_type)
        optional_ship_count = quantity - len(build_queue)
        for i in range(optional_ship_count):
            new_ship_type = choice(self.available_ship_type)
            build_queue.append(new_ship_type)

        while build_queue:
            item = build_queue.pop()
            if self.human is True:
                new_ship = self.choose_ship(item)
            else:
                new_ship = self.rand_ship(item)
                if not self.validate_ship(new_ship.position):
                    build_queue.append(item)
                    continue
            fleet.append(new_ship)
        return fleet

#implementation zone
if __name__ == '__main__':
    game = GameEngine()

    game.initialize()

    game.play()
  