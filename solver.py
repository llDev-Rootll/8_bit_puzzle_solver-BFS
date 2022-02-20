import copy
import os
import shutil
from utils import Node, parse_config


if __name__=="__main__":
    

    config_path = "input_config.json"

    test_cases = parse_config(config_path)
    for tc_i, tc in enumerate(test_cases):
        directory = "TEST_CASE_" + str(tc_i+1)
        if os.path.isdir(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)
        shutil.copy('plot_path.py', directory)
        Nodes_file = open(os.path.join(directory, "Nodes.txt"), 'w')
        nodePath_file = open(os.path.join(directory, "nodePath.txt"), 'w')
        NodesInfo_file = open(os.path.join(directory, "NodesInfo.txt"), 'w')
        NodesInfo_file.write("Node_index   Parent_Node_index   Cost"+ "\n")
        src = tc[0]

        goal = tc[1]
        
        start_node = Node(src, None, None, 0)
        visited = []
        idx = 1
        queue = [start_node]
        path = []

        while queue:
            # if idx == 8:
            #     break
            current_node = queue.pop(0)
            current_node.idx = idx
            idx+=1
            current_node_str = current_node.row2col()
            Nodes_file.write(current_node_str+ "\n")
            NodesInfo_file.write(str(current_node.idx)+" "+str(current_node.parent_idx)+" 0"+ "\n")
            # exit(0)
            if current_node.state == goal:
                path.append(current_node)
                print("SOLUTION FOUND FOR TEST CASE ", (tc_i+1), " : ")
                temp_node = copy.deepcopy(current_node)
                while temp_node.state != src:
                    
                    temp_node = temp_node.parent
                    path.append(temp_node)
                
                path.reverse()
                for i in path:
                    nodePath_file.write(i.row2col() + "\n")
                    print(i)
                break
                
            
            if current_node.state not in visited:
                visited.append(current_node.state)
                neighbours = current_node.gen_neighbours(current_node.find_zero(), visited)
                for nr in neighbours:
                    queue.append(nr)
        Nodes_file.close()
        NodesInfo_file.close()
        nodePath_file.close()
