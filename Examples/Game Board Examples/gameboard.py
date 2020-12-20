grid = [ [-1]*8  for n in range(8)] # list comprehension
grid[0][0] = 1
grid[7][7] = 1

w = 70 # width of each cell

def setup():
    size(800,600)
    
def draw():
    
    x,y = 0,0 # starting position

    for row in grid:
        for col in row:
          if col == 1:
              fill(250,0,0)
          else:
              fill(255)
          rect(x, y, w, w)
          x = x + w  # move right
        y = y + w # move down
        x = 0 # rest to left edge
        
        
def mousePressed():
    grid[mouseY/w][mouseX/w] = -1 * grid[mouseY/w][mouseX/w]  
    # integer division is good here!
