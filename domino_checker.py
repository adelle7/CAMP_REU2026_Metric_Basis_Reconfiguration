# GOAL: For a grid representation of a metric basis (everything in a column or row is adjacent), we
# want to see which polyominoes are valid for a metric basis
# This is done by comparing the possible grid dimensions of these polyominoes to ones that can be constructed 
# using horizontal dominoes. Note that we look at dimensions where width > height to avoid repetition.
# We take the union of the following graphs:
# K1, K2, K3, K4, P2, P3, P4, K3 +v P2

# Can change this depending on how big of a grid we want to test
MAX_WIDTH = 100
MAX_HEIGHT = 100
# graphs with grid representation (height, width)
# K2, K3, K4, P3, P4, K3 +v P2
graphs = [(1, 2), (1, 3), (1, 4), (2, 2), (3, 2), (2, 3)]
#graphs = [(2, 1), (3, 1), (4, 1), (2, 2), (2, 3), (2, 3)]
#graphs_names = {(2,1): 'K2', (3,1):'K3', (4,1):'K4', (2,2):'P3', (2,3):'P4', (3,2):'K3 +v P2'}
graphs_names = {(1, 2): 'K2', (1, 3):'K3', (1, 4):'K4', (2, 2):'P3', (3, 2):'P4', (2, 3):'K3 +v P2'}
domino_dim= []
domino_2_extra_dim = []
graphs_dim = []

# Generate all possible dimensions of a grid created only from dominoes 
def generate_domino_dim():
    for x in range(int(MAX_WIDTH/2)):
        for y in range(int(MAX_HEIGHT/2)):
            m = 2*x + y
            n = 2*y + x
            if (m >= n):
                domino_dim.append((m, n))

# Generate all possible dimension of a grid created by dominoes plus two extra rows and cols
def generate_2_extra_domino_dim():
    for item in domino_dim:
        m = item[0] + 2
        n = item[1] + 2
        domino_2_extra_dim.append((m, n))


# Generate all possible dimensions of a grid created from the union of graphs
def generate_graph_dim(graphs):
    for graph in graphs:   
        width = graph[0]   # one placement of graph in grid
        height = graph[1]

        if (width < MAX_WIDTH and height < MAX_HEIGHT and height < width):
            graphs_dim.append((width, height))
            print("%s : %s" % (graphs_names.get(graph), str((width, height))))

        for g in graphs:    # union each graph with the graph we are currently on
            width_one = width + g[0]
            height_one = height + g[1]  # one placement of graph unioning with
            width_two = width + g[1]
            height_two = width + g[0]   # another placement of graph union with 

            if (width_one < MAX_WIDTH and height_one < MAX_HEIGHT and height_one < width_one):
                graphs_dim.append((width_one, height_one))
                print("%s U %s : %s" %(graphs_names.get(graph), graphs_names.get(g), str((width_one, height_one))))
            
            if (width_two < MAX_WIDTH and height_two < MAX_HEIGHT and height_two < width_two):
                graphs_dim.append((width_two, height_two))
                print("%s U %s : %s" %(graphs_names.get(graph), graphs_names.get(g), str((width_two, height_two))))
                
        width = graph[1]   # another placement of graph in grid (rotated 90 deg)
        height = graph[0]

        if (width < MAX_WIDTH and height < MAX_HEIGHT and height < width):
            graphs_dim.append((width, height))

        for g in graphs:    # union of every g with the graph we are currently on
            width_one = width + g[0]
            height_one = height + g[1]  # one placement of g 
            width_two = width + g[1]
            height_two = height + g[0]   # another placement of g (rotated 90 deg)

            if (width_one < MAX_WIDTH and height_one < MAX_HEIGHT and height_one < width_one):
                graphs_dim.append((width_one, height_one))
                print("%s U %s : %s" %(graphs_names.get(graph), graphs_names.get(g), str((width_one, height_one))))
            
            if (width_two < MAX_WIDTH and height_two < MAX_HEIGHT and height_two < width_two):
                graphs_dim.append((width_two, height_two))
                print("%s U %s : %s" %(graphs_names.get(graph), graphs_names.get(g), str((width_two, height_two))))

# Check if dimensions m >= n >= 3 can have a trinomino or lonely vertex with all K2 as a basis
def contains_trinomino_or_vertex(m, n): 
    print("Graph with dimensions: %s" %(str((m, n))))
    vertex = False
    L_shape = False
    trinomino = False

    # lonely v empty col, lonely v empty row, 
    if (m-2, n-1) or (m-1, n-2) in domino_dim : # there is a lonely vertex
        #print("Can have a lonely vertex.")
        vertex = True
    # 3 vertices in a row trinomino with an empty col and empty row
    if (m-2, n-4) or (m-4, n-2) in domino_dim:    # there is a trinomino
        #print("Can have a vertical trinomino.")
        trinomino = True

    # L shaped trinomino with empty col and empty row
    if (m-3, n-3) in domino_dim:
        L_shape = True
        #print("Can have an L shaped trinomino.")

    return vertex or trinomino or L_shape

# Checks if graph with dimensions m >= n >= 3 can have one tetramino with all other K2 as a basis
def contains_tetramino(m, n):
    K4_block = False
    P4_block = False  # same dimension as K3 +v P2 block

    # K4 tetramino with empty row and empty col
    if (m-2, n-5) or (m-5, n-2) in domino_dim:
        K4_block = True
    
    # P4 tetramino with empty row and empty col
    if (m-3, n-4) or (m-4, n-3) in domino_dim:
        P4_block = True

    return K4_block or P4_block

# Checks if graph with dimensions m >= n >= 3 contains two trinominoes and all K2 as a basis
def contains_two_trinominoes(m, n):
    L_shape = False
    long_blocks = False
    L_long_blocks = False

    # 2 L shaped triominoes (with empty row and col)
    if (m-(2*2+1), n-(2*2+1)) in domino_dim:
        L_shape = True

    # 2 vertical triominoes, 2 horizontal triominoes, 1 vertical 1 horizontal (all with empty row and col)
    if (m-(2*1+1), n-(2*3+1)) or (m-(2*3+1), n-(2*1+1)) or (m-(1+4), n-(1+4)) in domino_dim:
        long_blocks = True

    # L shaped with vertical, L shaped with horizontal (with empty row and col)
    if (m-(1+2+1), n-(1+2+3)) or (m-(1+1+3), n-(1+2+1)) in domino_dim:
        L_long_blocks = True

    return L_long_blocks or L_shape or long_blocks

# Checks if graph with dimensions m >= n >= 3 contains a trinomino or a lonely vertex and all K2 as a basis
def contains_trinomino_and_vertex(m, n):
    horizontal_vertex = False
    L_shape_vertex = False
    vertical_vertex = False

    # 1 L shape 1 lonely vertex 1 empty col, 1 L shape 1 lonely vertex 1 empty row
    if (m-(1+1+2), n-(1+2)) or (m-(1+2), n-(1+1+2)) in domino_dim:
        L_shape_vertex = True
    
    # 1 horizontal block 1 lonely vertex 1 empty col, 1 horizontal 1 lonely 1 empty row
    if (m-(1+3+1), n-(1+1)) or (m-(1+3), n-(1+1+1)) in domino_dim:
        horizontal_vertex = True
    
    # 1 vertical block 1 lonely vertex 1 empty col, 1 vert 1 lonely 1 empty row
    if (m-(1+1+1), n-(1+3)) or (m-(1+1), n-(1+3+1)) in domino_dim:
        vertical_vertex = True

    return horizontal_vertex or L_shape_vertex or vertical_vertex


def main():
    print("Dimensions for dominoes: ")
    generate_domino_dim()
    generate_2_extra_domino_dim()

    for item in domino_2_extra_dim:
        print("Graph dimensions are: %s "% str(item))
        if (item[0] >= item[1] >= 3):
            print(contains_trinomino_and_vertex(item[0], item[1]))

    # print("Dimensions for graph unions:")
    # generate_graph_dim(graphs)
    # for item in graphs_dim:
    #     print(item)

    # print("Dimensions for graph unions that cannot be constructed with dominoes:")
    # domino_dim_set = set(domino_dim)
    # graphs_dim_set = set(graphs_dim)

    # for item in graphs_dim_set - domino_dim_set:
    #     print(item)


if __name__=="__main__":
    main()
