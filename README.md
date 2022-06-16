# consolcd
A simple tool which lets you use your terminal or interpreter shell in the same way as an lcd screen.<br />
It uses a simple dictionary to address any position in a given terminal or interpreter shell. <br />
This tool is by no means optimized and I am sure there is either a faster way to create this or there is already a faster program which I couldn't find.

# How to use
The program includes 4 functions:<br />
  - _set which is used to give a position (x,y) a string value<br />
  - console_print is used to print everything in terminal or interpreter shell<br />
  - clear which simply removes everything from the terminal<br />
  - clean which removes everything from the terminal or interpreter shell by printing new  lines<br />
  
# Example
This program would be used to print "Hello World" in what would be the first line of a 1602 lcd screen and the clear it.
```ruby
  screen = Screen((16,2))

  screen._set((0,0), 'H')
  screen._set((1,0), 'e')
  screen._set((2,0), 'l')
  screen._set((3,0), 'l')
  screen._set((4,0), 'o')
  screen._set((6,0), 'W')
  screen._set((7,0), 'o')
  screen._set((8,0), 'r')
  screen._set((9,0), 'l')
  screen._set((10,0), 'd')

  screen.console_print()
  
  screen.clear() #in terminal
  screen.clean() #in interpreter shell
```
