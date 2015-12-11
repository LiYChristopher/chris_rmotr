''' implementing battleship
'''
from collections import OrderedDict
from random import randint


class Grid(object):
    ''' setting up the grid for the game
    '''
    def __init__(self):
        self._inputs = [i+str(j) for i in map(chr, range(65, 75)) for j in range(1, 11)]
        self.grid = OrderedDict(zip(self._inputs, ['_|']*len(self._inputs)))

    def __repr__(self):
        return 'Grid({})'.format(self.grid)

    def __str__(self):
        ''' Need to implement a way to show the grid in a good format
        '''
        for row in range(65, 75):
            row_idx = chr(row)
            row_keys = filter(lambda key: key if key.startswith(row_idx)
                                else None, self.grid.keys())
            row = [self.grid[e] for e in row_keys]
            print ''.join(row)
        return 'Grid'

    def place(self, *ships):
        ''' takes in a list of ships and places them on the grid if ships fit
            otherwise throws and OutOfBoundsError.
            #TODO: Need to implement this
        '''
        for ship in ships:
            place_y = ship.position[0].capitalize()
            place_x = int(ship.position[1])

            if ship.orientation.lower() == 'h':
                allocation = [place_y + str(i) for i in range(place_x,
                                place_x + ship.size)]
                print allocation
                for loc in allocation:
                    self.grid[loc] = ship.marker

            elif ship.orientation.lower() == 'v':
                allocation = [chr(i) + str(place_x) for i in range(ord(place_y),
                                ord(place_y) + ship.size)]
                print allocation
                for loc in allocation:
                    self.grid[loc] = ship.marker

            else:
                print "That's not proper orientation"


class Ship(object):
    ''' Base ship class
    '''
    def __init__(self, count, position, orientation):
        self.count = count
        self.position = position
        self.orientation = orientation

    def __repr__(self):
        # nice to have a repr which shows the actual subclass names
        return '{cls}({c}, {p}, {o})'.format(cls=self.__class__.__name__,
                                             c=self.count, p=self.position,
                                             o=self.orientation)


class Aircraft(Ship):
    ''' Aircraft class
    '''
    def __init__(self, count, position, orientation):
        super(Aircraft, self).__init__(count, position, orientation)
        self.marker = 'A|'
        self.size = 5


class Submarine(Ship):
    ''' Submarine class
    '''
    def __init__(self, count, position, orientation):
        super(Submarine, self).__init__(count, position, orientation)
        self.marker = 'S|'
        self.size = 3


class PatrolBoat(Ship):
    ''' PatrolBoat class
    '''
    def __init__(self, count, position, orientation):
        super(PatrolBoat, self).__init__(count, position, orientation)
        self.marker = 'P|'
        self.size = 2


class GameEngine(object):
    '''
    This class control gamestate, and regulates flow
    '''
    def __init__(self):
        pass

    def show_available_ships(self):
        ''' creates random number of aircrafts, submarines and patrol boats
        '''
        num_a, num_s, num_pb = [randint(1, 4) for i in range(3)]
        print 'You have:'
        print '{} Aircraft (size = 5)'.format(num_a)
        print '{} Submarine (size = 3)'.format(num_s)
        print '{} Patrol Boat (size = 2)'.format(num_pb)
        return num_a, num_s, num_pb
    
    def choose_ships(self, numa, nums, numpb):
        ''' follows the Defend strategy for creating the ships.
            return the actual relevant ship objects
        '''
        aircrafts_input = raw_input('Position, Orientation for Aircrafts: ')
        submarines_input = raw_input('Position, Orientation for Submarines: ')
        patrol_boats_input = raw_input('Position, Orientation for Patrol Boats: ')
    
        a_pos, a_orient = map(str.strip, aircrafts_input.split(','))
        s_pos, s_orient = map(str.strip, submarines_input.split(','))
        pb_pos, pb_orient = map(str.strip, patrol_boats_input.split(','))
    
        # create ships
        aircrafts = Aircraft(numa, a_pos, a_orient)
        submarines = Submarine(nums, s_pos, s_orient)
        patrol_boats = PatrolBoat(numpb, pb_pos, pb_orient)
        return aircrafts, submarines, patrol_boats
    
    def initialize(self):
        grid = Grid()
        print grid
        numa, nums, numpb = self.show_available_ships() # get number of aircrafts from show_available_ships
        air, sub, pb = self.choose_ships(numa, nums, numpb)   #user inputs ship placement
    
        print grid.place(air, sub, pb)    #takes ships ==> places them on grid ==> prints for user
        print grid


#implementation zone
if __name__ == '__main__':
    game = GameEngine()
    game.initialize()