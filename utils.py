import copy
import numpy as np
import json

class Node:

    def __init__(self, state, parent, idx, parent_idx):
        self.state = state
        self.parent = parent
        self.idx = idx
        self.parent_idx = parent_idx

    def __repr__(self):
        return "Node : " + str(self.state) + " idx : " + str(self.idx) + " parent_idx : " + str(self.parent_idx)

    def find_zero(self):
        mat = self.state
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j]==0:
                    return [i,j]

    def ActionMoveUp(self, z_pos):
        x = z_pos[0]
        y = z_pos[1]
        if x == 0:
            return None

        else:
            up_node = Node(copy.deepcopy(self.state), Node(self.state, self.parent, self.idx, self.parent_idx), None, self.idx)
            up_node.state[x][y], up_node.state[x-1][y] = up_node.state[x-1][y], up_node.state[x][y]

        return up_node
    
    def ActionMoveDown(self, z_pos):
        x = z_pos[0]
        y = z_pos[1]
        if x == (len(self.state) - 1):
            return None

        else:
            down_node = Node(copy.deepcopy(self.state), Node(self.state, self.parent, self.idx, self.parent_idx), None, self.idx)
            down_node.state[x][y], down_node.state[x+1][y] = down_node.state[x+1][y], down_node.state[x][y]

        return down_node
    
    def ActionMoveLeft(self, z_pos):
        x = z_pos[0]
        y = z_pos[1]
        if y == 0:
            return None

        else:
            left_node = Node(copy.deepcopy(self.state), Node(self.state, self.parent, self.idx, self.parent_idx), None, self.idx)
            left_node.state[x][y], left_node.state[x][y-1] = left_node.state[x][y-1], left_node.state[x][y]

        return left_node

    def ActionMoveRight(self, z_pos):
        x = z_pos[0]
        y = z_pos[1]
        if y == (len(self.state) - 1):
            return None

        else:
            right_node = Node(copy.deepcopy(self.state), Node(self.state, self.parent, self.idx, self.parent_idx), None, self.idx)
            right_node.state[x][y], right_node.state[x][y+1] = right_node.state[x][y+1], right_node.state[x][y]

        return right_node

    def gen_neighbours(self, z_pos, visited):
        neighbour = []

        left = self.ActionMoveLeft(z_pos)
        if left:
            if left.state not in visited:

                neighbour.append(left)
        
        up = self.ActionMoveUp(z_pos)
        if up:
            if up.state not in visited:
                neighbour.append(up)
        
        right = self.ActionMoveRight(z_pos)
        if right:
            if right.state not in visited:

                neighbour.append(right)

        down = self.ActionMoveDown(z_pos)
        if down:
            if down.state not in visited:

                neighbour.append(down)
        
        return neighbour

    def row2col(self):

        m = np.array(self.state)
        output = m.T
        output_str= str(output.tolist())

        output_str = output_str.replace("[","")
        output_str = output_str.replace("]","")
        output_str = output_str.replace(",","")

        return output_str

    


def parse_config(path):
    with open('input_config.json', 'r') as f:
        data = json.load(f)
    test_cases=[]
    if data["i_1"]:
        if data["g_1"]:
            print("FIRST TEST CASE FOUND")
            test_cases.append([data["i_1"], data["g_1"]])

    if data["i_2"]:
        if data["g_2"]:
            print("SECOND TEST CASE FOUND")
            test_cases.append([data["i_2"], data["g_2"]])

    if data["i_3"]:
        if data["g_3"]:
            print("THIRD TEST CASE FOUND")
            test_cases.append([data["i_3"], data["g_3"]])
    
    if data["i_4"]:
        if data["g_4"]:
            print("FOURTH TEST CASE FOUND")
            test_cases.append([data["i_4"], data["g_4"]])
    
    return test_cases
