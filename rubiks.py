__author__ = 'Selwyn Jacob'

from aiSearch import *

class RubiksGraphNode(GraphNode):
    def __int__(self, top, front, left, right, back, bottom):
        """
        Corner Block - It has three color faces and three adjacent pieces
        that it will share a side with at any time.

        Edge Block - It has two color faces and has 4 adjacent pieces that
        it will share a side with at any time. In 3x3 blocks it always has
        2 center pieces and 2 corner pieces.

        Center block - In a 3x3 cube this piece is not movable, however it
        can be rotated. It will always have 4 adjacent edge blocks. In
        larger cubes there are multiple center blocks that could share with
        another center block or an edge piece. Center blocks never are
        adjacent to a corner block.

        USE 6 Multi-Dimensional Lists

                 TOP
                |WWW|   |1|2|3|
                |WWW|   |4|5|6|
                |WWW|   |7|8|9|

         LEFT   FRONT   RIGHT   BACK
        |RRR|   |BBB|   |OOO|   |GGG|
        |RRR|   |BBB|   |OOO|   |GGG|
        |RRR|   |BBB|   |OOO|   |GGG|

                BOTTOM
                |YYY|
                |YYY|
                |YYY|
        """

        GraphNode.__init__(self)

        """
        1 = white
        2 = blue
        3 = red
        4 = orange
        5 = green
        6 = yellow



        program inputs values into top,front,left,right,back,bottom
        """
        self.top = top[1,1,1,1,1,1,1,1,1]
        self.front = front[2,2,2,2,2,2,2,2,2]
        self.left = left[3,3,3,3,3,3,3,3,3]
        self.right = right[4,4,4,4,4,4,4,4,4]
        self.back = back[5,5,5,5,5,5,5,5,5]
        self.bottom = bottom[6,6,6,6,6,6,6,6,6]

    def prettyPrint(self):

        print "TOP: " + self.top
        print "FRONT:" + self.front
        print "LEFT:" + self.left
        print "RIGHT:" + self.right
        print "BACK:" + self.back
        print "BOTTOM:" + self.bottom

    def __eq__(self, other):
        """
        checks if state has reached goal state
        """
        if self.top == other.top and self.front == other.front and self.left == other.left and self.right == other.right and self.back == other.back and self.bottom == other.bottom:
            return True
        return False

    def  expand(self, graphNode):
        nextStateList = []
        """
        program selects one of the following moves
        """
        faceMoves = ['F', 'L', 'R', 'U', 'D', 'B']

        for moves in faceMoves:
            if moves == 'F':
                """
            self.top = [1,1,1,1,1,1,**3,3,3**]                   SWAP VALUES 7-9 WITH LEFT
            self.front = [2,2,2,2,2,2,2,2,2]
            self.left = [3,3,3,3,3,3,**6,6,6**]                 SWAP VALUES 7-9 WITH BOTTOM
            self.right = [4,4,4,4,4,4,**1,1,1**]               SWAP VALUES 7-9 WITH TOP
            self.back = [5,5,5,5,5,5,5,5,5]
            self.bottom = [6,6,6,6,6,6,**4,4,4**]             SWAP VALUES 7-9 WITH RIGHT
                """
                self.top[6] = self.left[6]
                self.top[7] = self.left[7]
                self.top[8] = self.left[8]

                self.left[6] = self. bottom[6]
                self.left[7] = self.bottom[7]
                self.left[8] = self.bottom[8]

                self.right[6] = self.top[6]
                self.right[7] = self. top[7]
                self.right[8] = self.top[8]

                self.bottom[6] = self.right[6]
                self.bottom[7] = self.right[7]
                self.bottom[8] =self.right[8]

                nextStateList.append(self.top,self.left,self.right,self.bottom)


            if moves == 'L':
                """
            self.top = [**5**,1,1,**5**,1,1,**5**,1,1]           SWAP VALUES 1,4,7 WITH BACK
            self.front = [**1**,2,2,**1**,2,2,**1**,2,2]       SWAP VALUES 1,4,7 WITH TOP
            self.left = [3,3,3,3,3,3,3,3,3]
            self.right = [4,4,4,4,4,4,4,4,4]
            self.back = [**6**,5,5,**6**,5,5,**6**,5,5]         SWAP VALUES 1,4,7 WITH BOTTOM
            self.bottom = [**2**,6,6,**2**,6,6,**2**,6,6]     SWAP VALUES 1,4,7 WITH FRONT
                """
                self.top[0] = self.back[0]
                self.top[3] = self.back[3]
                self.top[6] = self.back[6]

                self.front[0] = self.top[0]
                self.front[3] = self.top[3]
                self.front[6] = self.top[6]

                self.back[0] = self.bottom[0]
                self.back[3] = self.bottom[3]
                self.back[6] = self.bottom[6]

                self.bottom[0] = self.front[0]
                self.bottom[3] = self.front[3]
                self.bottom[6] = self.front[6]

                nextStateList.append(self.top,self.front,self.back,self.bottom)

            if moves == "R":
                """
            self.top = [1,1,**5**,1,1,**5**,1,1,**5**]           SWAP VALUES 3,6,9 WITH BACK
            self.front = front[2,2,**1**,2,2,**1**,2,2,**1**]       SWAP VALUES 3,6,9 WITH TOP
            self.left = left[3,3,3,3,3,3,3,3,3]
            self.right = right[4,4,4,4,4,4,4,4,4]
            self.back = back[5,5,**6**,5,5,**6**,5,5,**6**]         SWAP VALUES 3,6,9 WITH BOTTOM
            self.bottom = bottom[6,6,**2**,6,6,**2**,6,6,**2**]     SWAP VALUES 3,6,9 WITH FRONT
                """
                self.top[2] = self.back[2]
                self.top[5] = self.back[5]
                self.top[8] = self.back[8]

                self.front[2] = self.top[2]
                self.front[5] = self.top[5]
                self.front[8] = self.top[8]

                self.back[2] = self.bottom[2]
                self.back[5] = self.bottom[5]
                self.back[8] = self.bottom[8]

                self.bottom[2] = self.front[2]
                self.bottom[5] = self.front[5]
                self.bottom[8] = self.front[8]
                """
                update cube by adding to nextstate list
                """
                nextStateList.append(self.top,self.front,self.back,self.bottom)

            if moves == "U":
                """
            self.top = [1,1,1,1,1,1,1,1,1]
            self.front = [**4,4,4**,2,2,2,2,2,2]               SWAP VALUES 1-3 WITH RIGHT
            self.left = [**2,2,2**,3,3,3,3,3,3]                 SWAP VALUES 1-3 WITH FRONT
            self.right = [**5,5,5**,4,4,4,4,4,4]               SWAP VALUES 1-3 WITH BACK
            self.back = [**3,3,3**,5,5,5,5,5,5]                 SWAP VALUES 1-3 WITH LEFT
            self.bottom = [6,6,6,6,6,6,6,6,6]
                """
                self.front[0] = self.right[0]
                self.front[1] = self.right[1]
                self.front[2] = self.right[2]

                self.left[0] = self.front[0]
                self.left[1] = self.front[1]
                self.left[2] = self.front[2]

                self.right[0] = self.back[0]
                self.right[1] = self.back[1]
                self.right[2] = self.back[2]

                self.bottom[0] = self.left[0]
                self.bottom[1] = self.left[1]
                self.bottom[2] = self.left[2]

                nextStateList.append(self.front,self.left,self.right,self.bottom)

            if moves == "D":
                """
            self.top = [1,1,1,1,1,1,1,1,1]
            self.front = [2,2,2,2,2,2,2,**3,3,3**]              SWAP VALUES 7-9 WITH LEFT
            self.left = [3,3,3,3,3,3,**5,5,5**]                 SWAP VALUES 7-9 WITH BACK
            self.right = [4,4,4,4,4,4,**2,2,2**]                SWAP VALUES 7-9 WITH FRONT
            self.back = [5,5,5,5,5,5,**4,4,4**]                 SWAP VALUES 7-9 WITH RIGHT
            self.bottom = [6,6,6,6,6,6,6,6,6]
                """
                self.front[6] = self.left[6]
                self.front[7] = self.left[7]
                self.front[8] = self.left[8]

                self.left[6] = self.back[6]
                self.left[7] = self.back[7]
                self.left[7] = self.back[8]

                self.right[6] = self.back[6]
                self.right[7] = self.back[7]
                self.right[8] = self.back[8]

                self.back[6] = self.back[6]
                self.back[7] = self.back[7]
                self.back[8] = self.back[8]

                nextStateList.append(self.front,self.left,self.right,self.back)

            if moves == "B":
                """
            self.top = [**3,3,3**,1,1,1,1,1,1]                  SWAP VALUES 1-3 WITH LEFT
            self.front = [2,2,2,2,2,2,2,2,2,2]
            self.left = [**6,6,6**,3,3,3,3,3,3]                 SWAP VALUES 1-3 WITH BOTTOM
            self.right = [**1,1,1**,4,4,4,4,4,4]                SWAP VALUES 1-3 WITH TOP
            self.back = [5,5,5,5,5,5,5,5,5]
            self.bottom = [**4,4,4**,6,6,6,6,6,6]               SWAP VALUES 1-3 WITH RIGHT
                """
                self.top[0] = self.left[0]
                self.top[1] = self.left[1]
                self.top[2] = self.left[2]

                self.left[0] = self.bottom[0]
                self.left[1] = self.bottom[1]
                self.left[2] = self.bottom[2]

                self.right[0] = self.bottom[0]
                self.right[1] = self.bottom[1]
                self.right[2] = self.bottom[2]

                self.bottom[0] = self.right[0]
                self.bottom[1] = self.right[1]
                self.bottom[2] = self.right[2]
                nextStateList.append(self.top,self.left,self.right,self.bottom)


    def goalTest(self, graphNode):
        """
        compare solved rubiks cube goal state to current state
        """
        if (graphNode == self.goalState):
            return True
        else:
            return False

    def heuristic(self, graphNode):
        hval = 0
        """
        # of pieces out of place
        """
        for t in range(1,9):
            """
            increments through each piece on each face
            """
            if self.top[t] == self.top[5]:
                return True
            else:
                hval += 1
            if self.front[t] == self.front[5]:
                return True
            else:
                hval+= 1
            if self.left[t] == self.left[5]:
                return True
            else:
                hval+= 1
            if self.right[t] == self.right[5]:
                return True
            else:
                hval += 1
            if self.back[t] == self.back[5]:
                return True
            else:
                hval += 1
            if self.bottom[t] == self.bottom[5]:
                return True
            else:
                hval += 1
        return hval

    def cost(self, graphNode):
        return 1