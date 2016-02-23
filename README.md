# Miscellaneous
Small chunks of codes solving small problems

GameCard.java: solving a game I was challenged through bruteforce. Rules are simple: you have 2 Aces, 2 Kings, 2 Queens, and 2 Jacks. Place it in the below board such that any Aces must be next to a King, any Kings must be next to a Queen, any Queen must be next to a Jack, Queens and Aces cannot be adjacent, and no two cards of same number are adjacent. Just to spoil the game, the only solution is this:
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
