X = 0
Y = 1
SIZE = 5

def buildBoard():
    board = []
    for x in range(SIZE):
        for y in range(SIZE):
            square = [x, y]
            board.append(square)
    print(board)
    return board

def buildGraph(board, black):
    graph = {}
    for square in board:
        graph[tuple(square)] = getPosibleMoves(square, black)
    print(graph)
    return graph

def isBlackPiece(square, black):
    for blackPieces in black:
        if square[X] == blackPieces[X] and square[Y] == blackPieces[Y]:
            return True
    return False

def getPosibleMoves(square, black):
    posibleMoves = []
    knigthMoves = [] 
    x = square[X] + 2
    y = square[Y] + 1
    if x < SIZE and y < SIZE:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] + 2
    y = square[Y] - 1 
    if x < SIZE and y >= 0 :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] + 1
    y = square[Y] - 2
    if x < SIZE and y >= 0 :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] - 1 
    y = square[Y] - 2 
    if x >= 0 and y >= 0:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] - 2
    y = square[Y] + 1
    if x >= 0  and y < SIZE:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] - 2
    y = square[Y] - 1 
    if x >= 0  and y >= 0 :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] + 1
    y = square[Y] + 2
    if x < SIZE and y < SIZE :
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    x = square[X] - 1 
    y = square[Y] + 2 
    if x >= 0 and y < SIZE:
        if not isBlackPiece([x, y], black):
            posibleMoves.append([x, y])
    return posibleMoves

def isVisited(square, visited):
    if visited.count(square) > 0:
        return True
    else:
        return False

def DFS(graph, whites, startKnight):
    stack = []
    visited = []
    stack.append(startKnight)
    visited.append(startKnight)
    while len(stack) > 0:
        square = stack[len(stack) - 1]
        stack.pop()
        visited.append(square)
        if isVisited(whites, visited):
            break
        neighboors = graph.get(tuple(square))
        for neighboor in neighboors:
            if not isVisited(neighboor, visited):
                stack.append(neighboor)
    print('Solution')            
    print(visited)

def isSolution(whites, visited):
    for white in whites:
        if visited.count(white) < 1:
            return False
    return True
             

# Using readlines() 
file1 = open("/Users/dario/Documents/test1.txt", "r") 
Lines = file1.readlines() 
  
count = 0
whites = []
black = []
reading = 1

#read file for initialized board
for line in Lines: 
    print("Line{}: {}".format(count, line.strip()))
    if not line.strip():
        reading = reading + 1
        continue
    line = line.replace('\n','')
    coord = list(map(int,line.split(" ")))
    if reading == 1:
        startKnight = coord
    elif reading == 2:
        whites.append(coord)
    else:
        black.append(coord)
print('Knight start position')
print (startKnight)
print('White pieces')
print (whites)
print('Black pieces')
print (black)
board = buildBoard()
graph = buildGraph(board, black)

DFS(graph, whites, startKnight)




