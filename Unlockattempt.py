import itertools

class Unlockattempt (object):
    def __init__(self,locks,persons,number_for_access):
        self.locks              = locks
        self.persons            = persons
        self.number_for_access  = number_for_access

    def check_unlockable_combination(self):
        unlockable_by_number_for_access = True
        for i in itertools.combinations(range(self.persons), self.number_for_access):
            if not self.check_unlockable(i):
                unlockable_by_number_for_access=False
                return False
        unlockable_by_number_for_access_minus_one = False
        for i in itertools.combinations(range(self.persons), self.number_for_access-1):
            if self.check_unlockable(i):
                unlockable_by_number_for_access_minus_one = True
                return False
        return True

    def check_unlockable(self,persons_chosen):
        unlockable = True
        for i in self.locks:
            if set(i).isdisjoint(persons_chosen):
                unlockable = False
        return unlockable