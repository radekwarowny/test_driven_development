
def get_greetings():
    return 'Hello World!'


class Rick(object):
    def __init__(self, universe):
        self.universe = universe
        self.morty = None
        self.is_pickle = False

    def assign(self, morty):
        self.morty = morty
        morty.is_assigned = True


class Morty(object):
    def __init__(self, universe):
        self.universe = universe
        self.is_assigned = False


class Citadel(object):
    def __init__(self):
        self.__residents__ = []

    def get_all_residents(self):
        return self.__residents__

    def add_resident(self, resident):
        self.__residents__.append(resident)

    def pickle_ricks_with_morties(self):
        for resident in self.__residents__:
            if isinstance(resident, Rick):
                if resident.morty: resident.isPickle = True