import numpy as np

class Agent(object):
    def __init__(self, id, initial_pos):
        self.x = initial_pos[0]
        self.y = initial_pos[1]
        self.id = id
        self.bombs_left = 3
        self.alive = True
        self.events = []
        self.score = 0

        self.past_positions = [initial_pos]
        self.past_positions_set = set()

    def get_pos(self):
        return (self.x, self.y)


class Item(object):
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]


class Bomb(Item):
    def __init__(self, pos, owner, timer, power):
        super(Bomb, self).__init__(pos)
        self.owner = owner
        self.timer = timer
        self.power = power
        self.active = True

    def get_pos(self):
        return (self.x, self.y)

    def get_state(self):
        return (self.x, self.y, self.timer)


class Coin(Item):
    def __init__(self, pos):
        super(Coin, self).__init__(pos)
        self.collectable = True
        self.collected = False

    def get_state(self):
        return (self.x, self.y)


class Explosion(object):
    def __init__(self, blast_coords, owner, explosion_timer):
        self.blast_coords = blast_coords
        self.owner = owner
        self.timer = explosion_timer
        self.active = True