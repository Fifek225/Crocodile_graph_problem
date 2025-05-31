## Crocodile_graph_problem
This repo is for a short university project. The task is to find the shortest weighted path for a woman jumpin on Nile crocodiles (don't ask...).


# The task
A theif (you) have been caught stealing from an Egyptian temple. As a punishment you've been put on an island on a Nile river until your exectuion. You see that a lot of crocodiles are sleeping with their heads above the water. You determine that you are able to jump at most 5 meters throught the crocodiles to shore. Now you have to FIND THE SHORTEST PATH TO SHORE, before the priests come back.

# The solution
Dijkstra algorithm has been used as an easy way to solve weighted graph problems with with or without extra conditions. File structure is as follows:
graph.py - contains functions for reading and drawing the graph based on the .txt file with node and edge info. 
dijkstra.py - constains code to find the shortest weighted path with a condition that no weight can be > 5
main.py - main file for running the program
graph.txt - text file containing node and edge info. It has to be filled by the user.

# How to fill the graph.txt file?
The file structure is as follows:
\# NODE

start 0 0

A 1 3

B 2 5
.

.

.
end 9 9

\# EDGE

start A 2

A B 4

.

.

.

D end 5

B H 4

1. \# NODE and \# EDGE keywords are crucial.
2. For node definition you must write: node_ID X_coord y_coord in a single line
3. For edge definition you must write: node_1 node_2 weight in a single line
4. nodes named "start" and "end" do not have to be declared inside the graph.txt file nor does the user have the ability to change their location.
- start is always at (0,0)
- end is always at (9,9)
- The board (river) size is set as a constant 10 by 10 matrix.

An example of a generated graph is presented below.
![ex_graph](https://github.com/user-attachments/assets/e8f1d5c0-923e-4c06-91f1-48e2b4383cca)


Grey areas are spots in the matrix without any crocodiles. Weights and edges that are not part of the shortest path are transparent to imporve visibility.
