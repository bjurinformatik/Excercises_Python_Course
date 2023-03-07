#! /usr/bin/env python

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Orca', 'Shark', 'Piranha']

    def printMembers(self):
        print("Printing dangerous fish from the Fish class")
        for member in self.members:
            print("\t%s", % member)
