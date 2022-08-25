# Author: Jason Smith
# August 21, 2022

import json
import tkinter
from tkinter import filedialog


class Main:
    """Represents an instance of the application."""
    
    def __init__(self):
        # has a catalog
        # has a card
        self._path_to_catalog = ''
        # self.catalog = Catalog()
        
    def startup_menu(self):
        """Menu dispalyed on startup."""
        
        print('')
        print(' -- MAGIC CARD CATALOG --')
        print('')
        print('Press the number of the option below and press Enter:')
        print('')
        print('1. Create New Catalog')
        print('2. Open Existing Catalog')
        print('3. Exit')
        print('')
        
        user_choice = str(input('Choice: '))
        if user_choice == '1':
            self.create_new_catalog()
        elif user_choice == '2':
            self.open_catalog()
            self.open_catalog_menu()
        elif user_choice == '3':
            self.exit_app()
        else:
            print('')
            print('!! Invalid number. Please try again. !!')
            self.startup_menu()
            
    def new_catalog_menu(self):
        """Menu disaplyed when a new catalog is created."""        
        pass
    
    def open_catalog_menu(self):
        """Menu displayed when an existing catalog has been opened."""
        
        print('')
        print('Press the number of the option below and press Enter:')
        print('')
        print('1. View Catalog')
        print('2. Add Card')
        print('3. Remove Card')
        print('4. Save Catalog')
        print('5. Go Back To Last Menu')
        print('6. Exit')
        print('')
        
        user_choice = str(input('Choice: '))
        if user_choice == '1':
            self.display_catalog()
        elif user_choice == '2':
            # call to catalog / card object
            pass
        elif user_choice == '3':
            # call to catalog / card object
            pass
        elif user_choice == '4':
            # may not be needed
            pass
        elif user_choice == '5':
            self.startup_menu()
        elif user_choice == '6':
            # exit app
            pass
        else:
            print('')
            print('!! Invalid number. Please try again. !!')
            self.open_catalog_menu()
            
    def create_new_catalog(self):
        """This creates a new catalog file."""
        with open('card_catalog.json', 'w') as outfile:
            outfile.write('')
    
    def open_catalog(self):
        """This opens an existing catalog file for editing."""
        tkinter.Tk().withdraw()  # keeps empty tkinter window from displaying
        self._path_to_catalog = filedialog.askopenfilename()
    
    def close_catalog(self):
        """Closes the currently open catalog file."""
        pass
    
    def display_catalog(self):
        """"""
        # sort in aplhabetical order?
        # should user have option to view based on certain stats (type, name, 
        # mana, etc)?
        pass
    
    
    # may not need:
    # def delete_catalog(self):
    #     """Permanently deletes a catalog file."""
    #     pass
    
    # def save_catalog(self):
    #     """Saves the currently open catalog file."""
    #     pass
    
    def exit_app(self):
        """"""
        pass

class Catalog:
    """Represents a catalog instance."""
    
    def __init__(self):
        # has a card
        self._catalog = []  # [List of card objects]
        self._card_object = Card(name=None, type=None, collector_num=None,
                                mana=None, expansion=None)
    
    def remove_card(self, card):
        """Removes a card from the catalog file."""
        self._catalog.remove(card)
    
    def add_card(self, card):
        """Adds a card to the catalog file."""
        self._catalog.append(card)
    
    
class Card:
    """Represents a card instance."""
    
    def __init__(self, name, type, collector_num, mana, expansion):
        self._name = name
        self._type = type
        self._collector_num = collector_num
        self._mana = mana
        self._expansion = expansion
    
    def get_card_name(self):
        """Returns the name of the card."""
        pass
    
    def set_card_name(self, name):
        """Takes name as a parameter and sets the card name."""
        pass
    
    def get_card_type(self):
        """Returns the card type."""
        pass
    
    def set_card_type(self, type):
        """Takes type as a parameter and sets the card type."""
        pass
    
    def get_collector_number(self):
        """Returns the collector number of the card."""
        pass
    
    def set_collector_number(self, number):
        """Takes number as a parameter and sets the collector number of the 
        card."""
        pass
    
    def get_mana(self):
        """Returns the associated mana for the card."""
        pass
    
    def set_mana(self, mana):
        """Takes mana as a parameter and sets the mana of the card."""
        pass
    
    def get_expansion(self):
        """Retruns the expansion set of the card."""
        pass
    
    def set_expansion(self, expansion):
        """Takes expansion as a parameter and sets the expansion set of the 
        card."""
        pass
        
    

def main():
    """Mainloop."""
    app = Main()
    app.startup_menu()


if __name__ == "__main__":
    main()
