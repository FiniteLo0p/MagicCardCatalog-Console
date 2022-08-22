# Author: Jason Smith
# August 21, 2022


class Catalog:
    """Represents a catalog instance."""
    
    def __init__(self):
        self.card_object = Card(name=None, type=None, collector_num=None, mana=None, 
                         expansion=None)
    
    def create_new_catalog(self):
        """This creates a new catalog (.txt) file."""
        pass
    
    def open_catalog(self):
        """This opens an existing catalog file for editing."""
        pass
    
    def close_catalog(self):
        """Closes the currently open catalog file."""
        pass
    
    def delete_catalog(self):
        """Permanently deletes a catalog file."""
        pass
    
    def save_catalog(self):
        """Saves the currently open catalog file."""
        pass
    
    def remove_card(self):
        """Removes a card from the catalog file."""
        pass
    
    def add_card(self):
        """Adds a card to the catalog file."""
        pass
    
    
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
    print('')
    print(' -- MAGIC CARD CATALOG --')
    print('')
    print('Press the number of the option below:')
    print('')
    print('1. Create New Catalog')
    print('2. Open Existing Catalog')
    print('3. Exit')
    print('')


if __name__ == "__main__":
    main()
