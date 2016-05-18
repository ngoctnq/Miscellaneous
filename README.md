# Miscellaneous
Small chunks of codes solving small problems

<i>GameCard.java</i>    
The solution of a game I was challenged through bruteforce. Rules are simple: you have 2 Aces, 2 Kings, 2 Queens, and 2 Jacks. Place it in the below board such that any Aces must be next to a King, any Kings must be next to a Queen, any Queen must be next to a Jack, Queens and Aces cannot be adjacent, and no two cards of same number are adjacent. Just to spoil the game, the only solution is this:
```
        +---+
        | K |
+---+---+---+
| Q | J | Q |
+---+---+---+---+
    | A | K | A |
    +---+---+---+
        | J |
        +---+
```

<i>ABCEndView.py</i>    
The rules of the game can be found here: http://www.janko.at/Raetsel/Abc-End-View/index.htm. Similar to Sudoku solvers, the program removes impossible choices for each square, then bruteforce on the most promising route.

To input the problem, change the `constraint` and `choices` variables. As commented on the code, for `constraint`, it's a 3-dimensional array:
```
# params: rows/columns, count, head/tail
```
and for `choices`, it's a string of all the possible characters to fill in.

<i>Update:</i> Now allows you to uncomment the GUI part of the code and insert problem with a Tkinter interface.
