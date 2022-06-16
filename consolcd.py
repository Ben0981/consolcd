from os import system


class Screen:
    def __init__(self, size, placeholder=' '): #Creates the self.max variable used in the clean function
                              #Creates the self.size dictionary used to assign symbols to positions
                              #Placeholder for empty postions can be set. Default is empty string
        self.max = size
        self.size = {}
        for Y in range(size[1]):
            for X in range(size[0]):
                self.size[X,Y] = str(placeholder[0])
            self.size[X+1,Y] = '\n'
            
    def _set(self, pos, text): #Sets a position in the dictionary to the given symbol
                               #If the given symbol is a string only the first symbol is used
        if pos[0] <= [*self.size.keys()][-1][0] and pos[1] <= [*self.size.keys()][-1][1]:
            self.size[pos[0],pos[1]] = text[0]
        else:
            raise ValueError('Index not in screen size')
    
    def console_print(self): #Packs the dictionary containing all symbols and their position to string
                             #Then prints the created string
        screen_print = ''
        for key in self.size:
            screen_print += self.size[key]
        print(screen_print)
    
    def clear(self): #Clears the terminal using a function from the os library
        system('cls' if os.name=='nt' else 'clear')
    
    def clean(self): #Cleans the screen by moving the printed lines out of the way by spamming new lines
                     #Good for when you're not using the terminal but for example Thonny or another interpreter
        print('\n'*(self.max[1]-1)*10)
        
    
screen = Screen((16,2), "-")
screen._set((3,0), 'A')
screen._set((15,0), 'A')
screen._set((9,1), 'A')
screen._set((0,1), 'A')
screen.console_print()
