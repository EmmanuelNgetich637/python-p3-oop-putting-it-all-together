#!/usr/bin/env python3

class Book:# Define a class named Book
    def __init__(self, title, page_count):#(__init__: a special method that runs when you create an of the class.)
        self.title = title # Save the book title to the instance 
        self._page_count = None # initialize private variable for page_count
        self.page_count = page_count # use the setter to validate and set page_count 
        #(self.title and self.page_count stores the values pased in when creating the Book object)
    @property
    def page_count(self): #Getter method: used to access the page_count
        return self._page_count # Return the value of the private variable
    
    @page_count.setter
    def page_count(self, value):#Setter metod: used to validate and set page_count 
        if isinstance(value, int): # Check if the value is an integer
            self._page_count = value #If valid, set the private variable
        else:
            print("page_count must be an integer") # Print error if value is not an integer

    def turn_page(self):
        print("Flipping the page...wow, you read fast!") # Print message when method is called
        