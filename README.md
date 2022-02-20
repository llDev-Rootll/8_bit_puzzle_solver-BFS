
# 8_bit_puzzle_solver-BFS

A breadth first search implementation to solve the 8 bit puzzle.

## Requirements

 - numpy

Other libraries used are from the python standard libraries.

## Input Format
The project contains a configuration json named `input_config.json` which can be configured with 4 different test cases, 1 initial state & 1 goal state for each test case.
The file can been pre-configured with two existing test cases:

    {
	"i_1": [
		[1, 4, 7],
		[5, 0, 8],
		[2, 3, 6]
	],
	"i_2": [
		[4, 7, 0],
		[1, 2, 8],
		[3, 5, 6]
	],
	"i_3": [],
	"i_4": [],
	"g_1": [
		[1, 4, 7],
		[2, 5, 8],
		[3, 6, 0]
	],
	"g_2": [
		[1, 4, 7],
		[2, 5, 8],
		[3, 6, 0]
	],
	"g_3": [],
	"g_4": []
	}
Here `i_1` and `g_1`refers to initial state and the goal state of the first test case and so on for all four test cases.
The solver program can automatically parse the json for valid sets of test cases. 

**For each test case, it generates a folder named "TEST_CASE_<test_case_number>"  which contains all the required .txt files and a copy of the `plot_path.py`**

**Note: The solver will only be able to parse test cases in the above given format.**
## Steps to run the program

After successful configuration of the JSON file, run the following command to generate the results:

    python3 solver.py
To visualize each solution, run `plot_path.py` for each test case by entering the following commands:

    cd ./TEST_CASE_<test_case_number>
    python3 plot_path.py

The `utils.py` contains the python implementation of a Node class and other helper functions which are consumed by `solver.py`.