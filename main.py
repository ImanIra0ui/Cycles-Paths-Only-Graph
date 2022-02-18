#IRAOUI Imane

#Assumptions:
#The vertices should numbered starting 1 (not 0)
#A single isolated vertex isn't considered a path
#An edge (i,j): i!=j

import math

#Function to check if the given component is a cycle ------------------------------------------------
def iscycle(AdjMat,edges,verts):
    if edges != verts:
        return 0
        deg2flag = False
    else:
        # check if each vertex has degree 2. If it doesn't it is not a C_n
        deg2flag = True
        for i in range(verts):
            degree = 0
            for j in range(verts):
                degree = degree + AdjMat[i][j]
            if degree != 2:
                return 0
                deg2flag = False
                break

    # now if each vertex has degree 2, we check if it is one big cycle (i.e. C_n) or bunch of smaller cycles
    if deg2flag == True:
        # we will walk along vertex to vertex until we end where we started
        # if we covered n verts along the way, it is a big cycle
        # otherwise not
        numverts_seen = 0
        cycleclosed = False
        for i in range(verts):
            if AdjMat[0][i] == 1:
                next_vert = i
                break
        numverts_seen = 1

        prev_vert = 0
        current_vert = next_vert
        while cycleclosed == False:
            for i in range(verts):
                if AdjMat[current_vert][i] == 1 and i != prev_vert:
                    next_vert = i
                    break
            numverts_seen = numverts_seen + 1
            prev_vert = current_vert
            current_vert = next_vert
            if current_vert == 0:
                cycleclosed = True

        if numverts_seen == verts:
            return 1
        else:
            return 0
    return

#Function to label the vertices in the same component with the same label----------------------------------
def label (i,j):
    temp = arr[j]
    arr[j] = arr[i]
    for k in range(verts):
        if arr[k] == temp:
            arr[k] = arr[i]
    return arr

# this program asks user for number of vertices,
# then asks for number of edges,
# then asks the user to enter the edges in the format "a b" (without quotes),
# one at a time

# ask user for number of vertices
verts = eval(input("enter number of vertices: "))

# ask number of edges
edges = eval(input("enter number of edges: "))

# make Adjacency matrix of the graph
AdjMat = [[0] * verts for i in range(verts)]

# ask the user to enter the edges one by one and enter this info into AdjMat
for i in range(edges):
    a, b = (input("Enter edge: ")).split(" ")
    a = eval(a)
    b = eval(b)
    AdjMat[a - 1][b - 1] = 1
    AdjMat[b - 1][a - 1] = 1

#FINDING COMPONENTS:
#find components by labelling vertices that have an edge in common with the same label

#array of labels
arr = [0] * verts
#initializing label with the number of the vertex
for i in range (verts):
    arr[i] = i;

#label all connected vertices with the same label
for i in range (verts):
    for j in range (verts):
        if AdjMat[i][j] == 1 :
            if arr[i]<arr[j]:
                arr=label(i,j)
            else:
                arr=label(j,i)

#verify for each component if it is a cycle or a path

#keeps track of vertices in components that we already check so that we can loop
#only for n_components times
visited = [0] *verts
#items is used to map each index in the second adjacency matrix to
#its original vertex in the first adjacency matrix
items = {}
output = "This graph has as components:\n"
flag_output = 0

for j in range (verts): #this loop is repeated for each component
    if visited[j]!=1:
        cnt2 = 0
        flag = 1
        for k in range(verts):
            if arr[k]==j:
                visited[k]=1
                cnt2 = cnt2+1
                if (flag==1):
                    arr2 = [k] #puts the vertices that are in the same component in an array
                    flag = 0
                else:
                    arr2.append(k)

        cnt3 = 0
        #adjacency matrix is created for each component
        AdjMat2 = [[0]*cnt2 for i in range (cnt2)]

        #work with adj matrix to find whether the component is a cycle
        flag_cycle = 1

        for z in range (cnt2):
            items[z] = arr2[z]

        #this is to fill the second adjmat with values from the original adjmat
        for a in range (cnt2):
            for b in range (cnt2):
                AdjMat2 [a][b] = AdjMat[items[a]][items[b]]

        #counting the number of edges to use them in the isCycle function
        edges2=0
        for c in range (cnt2):
            for d in range (cnt2):
                if AdjMat2[c][d]==1:
                    edges2 = edges2 +1

        edges2 = edges2//2

        #verify if the component is a cycle
        x=iscycle(AdjMat2,edges2,cnt2)
        if x==1:
            output = output + "A cycle with " + str(cnt2) + " vertices.\n"
        else:
            flag_cycle=0

        #verify if the component is a path
        #general approach: we count number of vertices with degree 1 and those with degree 2
        #in a path only two vertices should have deg1, and all the others should have deg2

        cntdeg1 =0
        cntdeg2=0

        if flag_cycle==0:
            for v in range (cnt2):
                cntv=0
                for w in range (cnt2):
                    if AdjMat2[v][w]==1:
                        cntv = cntv+1
                if cntv==1:
                    cntdeg1 = cntdeg1+1
                if cntv==2:
                    cntdeg2 = cntdeg2+1

            if cntdeg1==2 and cntdeg2==cnt2-2:
                    output = output + "A path with " + str(cnt2) + " vertices.\n"
            else:
                print("The graph is not composed of cycles and paths only")
                flag_output=1
                break

if flag_output==0:
    print (output)

