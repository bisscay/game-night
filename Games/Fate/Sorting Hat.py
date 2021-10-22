"""Sorting Hat
    Author: bAe
    Description: Lol, I'm so extra.
    Date: 13/08/2021
"""
# Boujee Bandits
# vs
# Top Members

# Functionality:
# Take a name,
# Randomly place name in a group,
# Ensure one group is never above the other by 1.

# Pseudocode:
# Prompt for name
# Check group condition
# Place in group
# Prompt group
from random import randrange

class Sorting_Hat:
    GROUP_LIMIT = 8
    BB_count = TM_count = 0

    def get_faith(self,_):
        if self.BB_count == self.GROUP_LIMIT:
            return "Everyone else is a Top Member."

        if self.TM_count == self.GROUP_LIMIT:
            return "Everyone else is a Boujee Bandit."

        faith = randrange(1, 7)

        if faith%2 == 0:
            self.BB_count = self.BB_count + 1
            return "Boujee Bandit"
        self.TM_count = self.TM_count + 1
        return "Top Member"

def main():
    judge = Sorting_Hat()

    while (input("Exit?: ") not in ["exit","yes","y"]):
        challenger = input('Challenger: ')

        print("\n\n************ "+judge.get_faith(challenger)+" !!!!!************\n")
    print("\nFate has Begun.")

if __name__ == "__main__":
    main()
