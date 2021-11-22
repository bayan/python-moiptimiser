\ Objective function sense defines the sense of multiple objectives
Minimize multi-objectives

OBJ1: Priority=4 Weight=1 AbsTol=0 RelTol=0
3 X1X1 + 2 X1X2 + 4 X1X3 + 4 X1X4 + 3 X1X5 +
5 X2X1 + 4 X2X2 + 3 X2X3 + 4 X2X4 + 3 X2X5 +
3 X3X1 + 1 X3X2 + 5 X3X3 + 3 X3X4 + 4 X3X5 +
5 X4X1 + 5 X4X2 + 4 X4X3 + 5 X4X4 + 3 X4X5 +
1 X5X1 + 1 X5X2 + 1 X5X3 + 1 X5X4 + 3 X5X5

OBJ2: Priority=3 Weight=1 AbsTol=0 RelTol=0
2 X1X1 + 1 X1X2 + 3 X1X3 + 2 X1X4 + 2 X1X5 +
3 X2X1 + 5 X2X2 + 5 X2X3 + 1 X2X4 + 1 X2X5 +
4 X3X1 + 3 X3X2 + 4 X3X3 + 1 X3X4 + 5 X3X5 +
4 X4X1 + 5 X4X2 + 5 X4X3 + 2 X4X4 + 4 X4X5 +
3 X5X1 + 4 X5X2 + 1 X5X3 + 5 X5X4 + 5 X5X5

OBJ3: Priority=2 Weight=1 AbsTol=0 RelTol=0
2 X1X1 + 5 X1X2 + 5 X1X3 + 4 X1X4 + 4 X1X5 +
4 X2X1 + 2 X2X2 + 4 X2X3 + 2 X2X4 + 5 X2X5 +
4 X3X1 + 1 X3X2 + 2 X3X3 + 4 X3X4 + 3 X3X5 +
4 X4X1 + 4 X4X2 + 1 X4X3 + 3 X4X4 + 1 X4X5 +
4 X5X1 + 3 X5X2 + 5 X5X3 + 4 X5X4 + 1 X5X5

OBJ4: Priority=1 Weight=1 AbsTol=0 RelTol=0
2 X1X1 + 5 X1X2 + 4 X1X3 + 5 X1X4 + 2 X1X5 +
2 X2X1 + 4 X2X2 + 1 X2X3 + 2 X2X4 + 2 X2X5 +
3 X3X1 + 3 X3X2 + 2 X3X3 + 4 X3X4 + 1 X3X5 +
1 X4X1 + 3 X4X2 + 4 X4X3 + 3 X4X4 + 5 X4X5 +
2 X5X1 + 2 X5X2 + 1 X5X3 + 3 X5X4 + 1 X5X5


s.t.

\ Row assignment constraints
X1X1 + X1X2 + X1X3 + X1X4 + X1X5 = 1
X2X1 + X2X2 + X2X3 + X2X4 + X2X5 = 1
X3X1 + X3X2 + X3X3 + X3X4 + X3X5 = 1
X4X1 + X4X2 + X4X3 + X4X4 + X4X5 = 1
X5X1 + X5X2 + X5X3 + X5X4 + X5X5 = 1

\ Column assingment constraints
X1X1 + X2X1 + X3X1 + X4X1 + X5X1 = 1
X1X2 + X2X2 + X3X2 + X4X2 + X5X2 = 1
X1X3 + X2X3 + X3X3 + X4X3 + X5X3 = 1
X1X4 + X2X4 + X3X4 + X4X4 + X5X4 = 1
X1X5 + X2X5 + X3X5 + X4X5 + X5X5 = 1

\ Binary constraints
BINARY
X1X1
X1X2
X1X3
X1X4
X1X5
X2X1
X2X2
X2X3
X2X4
X2X5
X3X1
X3X2
X3X3
X3X4
X3X5
X4X1
X4X2
X4X3
X4X4
X4X5
X5X1
X5X2
X5X3
X5X4
X5X5
END
