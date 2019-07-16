import itertools

class Unlockattempt (object):
    """Given a number of locks an distribution of keys this class has methods to determine whether it is a solution to the puzzle."""
    def __init__(self,locks,persons,number_for_access):
        self.locks              = locks
        self.persons            = persons
        self.number_for_access  = number_for_access

    def check_unlockable_combination(self):
        """Check if the given distribution is a solution to the puzzle."""

        for i in itertools.combinations(range(self.persons), self.number_for_access):
            if not self.check_unlockable(i):
                return False

        for i in itertools.combinations(range(self.persons), self.number_for_access-1):
            if self.check_unlockable(i):
                return False

        return True

    def check_unlockable(self,persons_chosen):
        """Given the key distribution and a subset of persons, determine whether they can unlock the box."""
        unlockable = True
        for i in self.locks:
            if set(i).isdisjoint(persons_chosen):
                unlockable = False
        return unlockable