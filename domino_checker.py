# Checks if the union of the following graphs produces a valid polyomino for a metric basis
# K1, K2, K3, K4, P2, P3, P4, K3 +v P2

MAX_WIDTH = 10
MAX_HEIGHT = 10
# graphs with grid representation (height, width)
# K2, K3, K4, P3, P4, K3 +v P2
graphs = [(1, 2), (1, 3), (1, 4), (2, 2), (3, 2), (2, 3)]
horiz_domino_dim= []
combo_domino_dim = []
graphs_dim = []

# Generate all possible dimensions of a grid created only from dominoes 
def generate_domino_dim():
    width = 0
    height = 0

    # all horizontal dominoes
    while (width < MAX_WIDTH and height < MAX_HEIGHT):
        width += 2
        height += 1
        if (height < width):
            horiz_domino_dim.append((width, height))

    # combo of horizontal and vertical dominoes 
    for i in range(int(MAX_WIDTH/2)):
        width = 0
        height = 0
        for j in range(i): # place first i num of horizontal dominoes
            width += 2
            height += 1
        while (width < MAX_WIDTH and height < MAX_HEIGHT): # fill the rest with vertical dominoes
            width += 1
            height += 2
            if (height < width):
                combo_domino_dim.append((width, height)) 

# Generate all possible dimensions of a grid created from the union of graphs
def generate_graph_dim(graphs):
    for graph in graphs:   
        width = graph[0]   # one placement of graph in grid
        height = graph[1]

        if (width < MAX_WIDTH and height < MAX_HEIGHT and height < width):
            graphs_dim.append((width, height))

        for g in graphs:    # union each graph with the graph we are currently on
           # print("Union of graphs: ", graph, g)
            width_one = width + g[0]
            height_one = height + g[1]  # one placement of graph unioning with
            width_two = width + g[1]
            height_two = width + g[0]   # another placement of graph union with 

            if (width_one < MAX_WIDTH and height_one < MAX_HEIGHT):
                graphs_dim.append((width_one, height_one))
                #print("added dim for graphs: ", (width_one, height_one), graph, g)
            
            if (width_two < MAX_WIDTH and height_two < MAX_HEIGHT):
                graphs_dim.append((width_two, height_two))
                #print("added dim for graphs: ", (width_two, height_two), graph, g)


        width = graph[1]   # another placement of graph in grid (rotated 90 deg)
        height = graph[0]

        if (width < MAX_WIDTH and height < MAX_HEIGHT and height < width):
            graphs_dim.append((width, height))

        for g in graphs:    # union of every g with the graph we are currently on
            #print("Union of graphs: ", graph, g)
            #print("width: %d height: %d" % (width, height))
            width_one = width + g[0]
            height_one = height + g[1]  # one placement of g 
            width_two = width + g[1]
            height_two = height + g[0]   # another placement of g (rotated 90 deg)

            if (width_one < MAX_WIDTH and height_one < MAX_HEIGHT and height_one < width_one):
                graphs_dim.append((width_one, height_one))
               # print("added dim for graphs: ", (width_one, height_one), graph, g)
            
            if (width_two < MAX_WIDTH and height_two < MAX_HEIGHT and height_two < width_two):
                graphs_dim.append((width_two, height_two))
               # print("added dim for graphs: ", (width_two, height_two), graph, g)        

def main():
    print("Dimensions for dominoes: ")
    generate_domino_dim()

    for item in horiz_domino_dim:
        print(item)
    for item in combo_domino_dim:
        print(item)

    print("Dimensions for graph unions:")
    generate_graph_dim(graphs)

    union_dim = set(graphs_dim)
    for item in union_dim:
        print(item)




if __name__=="__main__":
    main()
