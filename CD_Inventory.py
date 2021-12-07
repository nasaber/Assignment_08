#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# NSaber, 2021-Dec-05, Added Code and Functionality
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    def __init__(self, cd_id, cd_title, cd_artist):
        self.__cd_id = cd_id 
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
        
        
    @property
    def cd_id(self):
        
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if str(value).isnumeric():
            
            self.cd_id = value
        else:
            raise Exception('CD ID can\'t be alphabetic')
            
    @property
    def cd_title(self):
        
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        if str(value).isnumeric():
            raise Exception('CD Title can\'t be cryptic')            
        else:
            
            self.cd_title = value
    
   
    @property
    def cd_artist(self):
        
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        if str(value).isnumeric():
            raise Exception('CD Artist can\'t be cryptic')            
        else:
            
            self.cd_artist = value    
   
    def __str__(self):
        return self.cd_id, self.cd_title, self.cd_artist

   
  
        
   

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # TODone Add code to process data from a file
    

    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of objects

        Reads the data from file identified by file_name into a 2D table
        one line in the file represents one one CD object row in table.

        Args:
            file_name (string): name of file used to read the data from
            
        Returns:
            None.
        """
        table = []
        table.clear()  # this clears existing data and allows to load data from file
        try:
            with open(file_name, 'r') as f:
               rows = [r.strip().split(',') for r in f.readlines()]
               table = [CD(*row) for row in rows]
            
            
        except FileNotFoundError as e:
                        print('Text file does not exist!')
                        print('Build in error info:')
                        print(type(e), e, sep='\n')
        return table
        
    
    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        # TODone Add code here
        """Function to write the data in list of objects to a text file

        Writes the data to file identified by file_name from a 2D table
        one line in the file represents one CD object row in table.

        Args:
            file_name (string): name of file used to write the data to
            lst_Inventory (list of objects): 2D data structure that holds the data during runtime

        Returns:
            None.
        """
        try:
            objFile = open(file_name, 'w')
            for obj in lst_Inventory:
                objFile.write(','.join(obj.__str__())+ '\n')
            objFile.close()
        except IOError as e:
                        print('Text file does not exist or cannot be created!')
                        print('Build in error info:')
                        print(type(e), e, sep='\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Handling input/output:

    properties:

    methods:
        print_menu(): -> Print out menu options
        menu_choice(): -> (user's choice, string)
        show_inventory(table) -> None
        user_input() -> (CD data input by user)

    """    
    
    
    
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
  
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID, CD Title, Artist\n')
        for obj in table:
            print(','.join(obj.__str__()))
        print('======================================')
    # TODone add code to get CD data from user
    @staticmethod
    def user_input():
        """Gets user input for CD

        Args:
            None.

        Returns:
            strID (string): CD ID input by the user
            strTitle (string): Title of the CD input by the user
            stArtist (string): Artist name input by the user
        """
        while True:
            strID = input('Enter ID: ').strip()
            strTitle = input('What is the CD\'s title? ').strip()
            stArtist = input('What is the Artist\'s name? ').strip()
            
            print()  # Add extra space for layout
            if strID.isnumeric():
                break
            print('CD ID should be an integer! Enter the data again:\n')
        return strID, strTitle, stArtist

# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)

while True:
# Display menu to user
     IO.print_menu()
     strChoice = IO.menu_choice()
    # show user current inventory
     if strChoice == 'i':
         IO.show_inventory(lstOfCDObjects)
         continue  # start loop back at top.
    # let user add data to the inventory
     if strChoice == 'a': 
        strID, strTitle, stArtist = IO.user_input()
        cd = CD(strID, strTitle, stArtist)
        lstOfCDObjects.append(cd)
    # let user save inventory to file
     if strChoice == 's': 
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            # TODone move processing code into function
            FileIO.save_inventory(strFileName, lstOfCDObjects)
    # let user load inventory from file
     if strChoice == 'l':
            print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
            strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
            if strYesNo.lower() == 'yes':
                print('reloading...')
                lstOfCDObjects = FileIO.load_inventory(strFileName)
                IO.show_inventory(lstOfCDObjects)
            else:
                input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
                IO.show_inventory(lstOfCDObjects)
                continue  # start loop back at top.
    # let user exit program
     elif strChoice == 'x':
        break

