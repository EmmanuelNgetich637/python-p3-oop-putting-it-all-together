#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand # set brand directly
        self._size = None # private variable for size
        self.size = size # use setter to validate
        self.condition = None # default condition is None

    @property
    def size(self):
        return self._size #return private size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int): # check if size is int
            self._size = value 
        else:
            print("size must be an integer") # error message if invalid

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New" # set condition to 'New'
