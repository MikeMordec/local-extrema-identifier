'''
Created on May 7, 2022

@author: michaelmordec
'''
import random
from xmlrpc.client import MAXINT

NORTH = -1
EAST = 1
SOUTH = 1
WEST = -1

global minList
minList = []
global maxList
maxList = []

def getCell(b,x,y):
    result = []
    if x < 0: 
        return result
    if x > 3: 
        return result
    if y < 0: 
        return result
    if y > 3: 
        return result
    result.append(b[y][x])
    return result

def getNeigh(b,x,y):
    result = []
    #north
    result.extend(getCell(b,x,y+NORTH))
    #north east
    result.extend(getCell(b,x+EAST,y+NORTH))
    #east
    result.extend(getCell(b,x+EAST,y))
    #south east
    result.extend(getCell(b,x+EAST,y+SOUTH))
    #south
    result.extend(getCell(b,x,y+SOUTH))
    #south west
    result.extend(getCell(b,x+WEST,y+SOUTH))
    #west
    result.extend(getCell(b,x+WEST,y))
    #north west
    result.extend(getCell(b,x+WEST,y+NORTH))
    return result
        
def getMax(b,x,y):
    target = b[y][x]
    neigh = getNeigh(b,x,y)
    #print(neigh)
    
    for n in neigh:
        if n > target:
            return
    print("Peak max: "+str(target)+", found at: ("+str(y)+", "+str(x)+")")
    maxList.append(target)
            
def getMin(b,x,y):
    target = b[y][x]
    neigh = getNeigh(b,x,y)
    for n in neigh:
        if n < target:
            return
    print("Peak min: "+str(target)+", found at: ("+str(y)+", "+str(x)+")")
    minList.append(target)
    
def getMaxMin(b,x,y):
    getMax(b,x,y)
    getMin(b,x,y)
  
def main():
    ROWS = 4   #update to a 20 x 20 after testing, otherwise 20 x 20 is too difficult to verify correctness
    COLS = 4
    NUMBERS = 100
    '''
    board = [[4, 6, 7, 23],
             [7, 6, 3, 2],
             [45, 6, 12, 4],
             [12, 3, 2, 7]];
    
    #OR
    '''
    board = []
    for i in range(0, ROWS):
        newRow = []
        for j in range(0, COLS):
            item = random.randint(0, MAXINT) % NUMBERS + 1
            newRow.append(item)
            print(f"{item:3.0f}", end="")
        board.append(newRow)
        print()
    
    print("CORNERS")   #The corners are compound conditional/if statements for the min/max.
    #Top-left Max
    getMax(board,0,0)

    #Top-right Max
    getMax(board,3,0)

    #Bottom-left Max
    getMax(board,0,3)

    #Rottom-right Max
    getMax(board,3,3)

    #Top-left Min
    getMin(board,0,0)
    
    #Top-right Min
    getMin(board,3,0)

    #Bottom-left Min
    getMin(board,0,3)

    #Rottom-right Min
    getMin(board,3,3)

    print("NON-CORNER EDGE")   #The non-corner edges are for loops using compound conditional statements for the min/max.
    #Top edge
    getMaxMin(board,0,1)
    getMaxMin(board,0,2)
    
    #Bottom edge
    getMaxMin(board,3,1)
    getMaxMin(board,3,2)
    
    #Left edge: max, min
    getMaxMin(board,1,0)
    getMaxMin(board,2,0)
    
    #Right edge
    getMaxMin(board,1,3)
    getMaxMin(board,2,3)


    print("INSIDE (NON-EDGE/NON-CORNER)")   #The inside is a double-for loop using compound conditional statements for the min/max.
    getMaxMin(board,1,1)
    getMaxMin(board,1,2)
    getMaxMin(board,2,1)
    getMaxMin(board,2,2)
    
    print("Mins in order:")
    minList.sort()
    for num in minList:
        print(str(num)+" ",end="")
    print()
    
    print("Maxes in order:")
    maxList.sort()
    for num in maxList:
        print(str(num)+" ",end="")
    print()    
if __name__ == '__main__':
    main()
    
    

