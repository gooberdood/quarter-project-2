from assets import *

"""
spawn is column 1,2 from top left
air = 0
wall front = 1
wall top = 2
wall top bottom left corner = 3
wall top bottom right corner = 4
wall front bottom left corner = 5
wall front bottom right corner = 6
wall top vertical (left/right side) = 7
wall top turn right 1 = 8
wall top turn right 2 = 9
wall top turn left 1 = 10
wall top turn left 2 = 11
wall top t south = 12
wall top t west = 13
wall top t east = 14
wall top t north = 15
wall front t south = 16
wall front sign = 17
wall front shop bar = 18
floor shop bar = 19
wall top shop bar = 20
wall front left of gate = 21
wall front right of gate = 22
wall top left of gate = 23
wall top right of gate = 24
"""

#sign text [[x, y, line1, line2, line3]]
signText = [[5, 5, "This is a testing dialogue.", "If you are reading this,", "you are a certified sigma."],
            [3, 2, "Welcome to MazeGame!", "Your goal is to escape the", "maze."],
            [4, 2, 'Press ESC to pause, and', 'H for help. Go pick up', "that key with X to continue."]]

#dialogue text [[portrait to use, x, y, line1, line2, line3

"""
#maze maps
maze1 = [[9 ,2 ,2 ,2 ,2 ,2 ,11],
         [8 ,1 ,17,17,1 ,1 ,10],
         [7 ,0 ,0 ,0 ,0 ,0 ,7 ],
         [7 ,0 ,0 ,0 ,0 ,0 ,7 ],
         [7 ,0 ,0 ,0 ,0 ,0 ,7 ],
         [7 ,0 ,0 ,0 ,0 ,0 ,7 ],
         [3 ,2 ,23,0 ,24,2 ,4 ],
         [5 ,1 ,21,0 ,22,1 ,6 ],]
"""
"""
keyObj = 0
closedGateBottom = 1
closedGateTop = 2
openGateBottom = 3
openGateTop = 4
"""
maze1Objects = []
#objects [[x, y, object type]]
maze1Objects = [[6, 3, keyObj],
                [4, 7, closedGateTopObj],
                [4, 8, closedGateBottomObj]]

#TEST MAP:
maze1 = [[1 ,0 ,2 ,0 ,3 ,0 ,4 ,0 ,5 ,0 ,6 ,0 ,7 ],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [8 ,0 ,9 ,0 ,10,0 ,11,0 ,12,0 ,13,0 ,14],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [15,0 ,16,0 ,17,0 ,18,0 ,19,0 ,20,0 ,21],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [22,0 ,23,0 ,24,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],
         [0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ],]
