# Requirements

- Packages
    - Pygame
    - Unittest

- Entities
    - game board
        - 4x8 grid
        - Two grid spaces must always be empty
        
    - blocks
        - blocks can be different sizes
        - How should they be created?
            - matrix? create shapes from a library?
            - remember, with sudoku, you technically didn't have to make a board. Your were still technically using computer logic. 
                - Does that mean I should focus on the computer logic first before making the shapes?
                    - probably not, since this is a game of shapes, where the rules are bound by the dimensions and visuals. 
                        - so maybe you should focus on the visual aspect of the game first before you think of the computing logic. 

    

-  Methods
    - move_block
        - Translate block along x or y axis
        - block cannot move to said direction if another block is in its path

