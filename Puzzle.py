import itertools
import Unlockattempt
import powerset
import time

start_time = time.time()

persons = 4
number_for_access = 3

# Puzzle:
# Can one lock a box with multiple locks and distribute keys to the boxes (potentially more than one key per box) to a number of persons, such that the box can be unlocked [number_for_access] persons, but cannot be unlocked by [number_for_access]-1 persons?

locks = 1

while True:
    key_list = powerset.powerset(range(persons))
    for i in itertools.product(key_list, repeat=locks):
        attempt = Unlockattempt.Unlockattempt(i,persons,number_for_access)

        #print(i)
        if attempt.check_unlockable_combination():
            print (attempt.locks)
            print("--- %s seconds ---" % (time.time() - start_time))
            exit()
    locks=locks+1
