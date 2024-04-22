# mock router program

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

description = """
MockRouterApp API is a stimulation of router activities in a simple network.

## Endpoints

**/addrouter:** this function supports the adding of router names to the network.

  The user inputs a name to be associated with a router and returned is a success response indicating they have created a new router to be added to the network.

**/connect:** this function creates a connection between two routers.

  The user inputs the name of the router they wish to be connected with the current router, and a cost to be associated with the 'edge' or connection that runs between them.

**/removerouter:** this function deletes routers from the network.

  The user inputs the name of the router they wish to remove from the network and in response the name of he deleted router is returned indicating success of removal.

**/removeconnection:** this function deletes the connection between two routers.

  The user inputs the location of the connection stored in a variable name and in response they get a success status which indicates the deletion of the connection. 

**/route:** this function uses Dijkstra's algorithm to get the shortest path consisting of connections to the desired location.

  The user inputs the name of the router and a destination and in response the graph is analyzed and the shortest path node points are returned.

## Classes
* Router(): this class holds all functionality of the routers in the network and information such as names associated to each one.
* Graph(): this class holds all functionality of the connections between routers and information such as cost of connections which contribute to paths.

## References / Sources
(Also included at end of file)
* "what is routing?" - https://www.cloudflare.com/en-gb/learning/network-layer/what-is-routing/
* 'graphs in python' - https://www.tutorialspoint.com/python_data_structure/python_graphs.htm
* 'Dijsktra's algorithm' - https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/?ref=rp
"""

app = FastAPI(
title="MockRouterApp",
    description=description,
    version="1.0.0",
)

@app.get("/")
def home():
    return{"Home": {"project": "Mock Router"}}

# creating a router
# router has a name and connection to a network on the graph
class Router():
    routerName: object
    # stores the cost of distance between current router and another
    distanceCost = []
    # stores elements popped from the list
    removed = []
    # the connector joins nodes on a graph;
    # this list will store the cost associated with each connection
    connectionCost = []
    # stores Dijsktra's chosen path
    pathD = []

    def __init__(self, routerName, networkConnection):
        self.routerName = routerName
        self.networkConnection = networkConnection

    @app.post("/addRouter")
    # add router endpoint
    # adding a router to the graph
    async def addRouter(self, routerName):
        # initializes the node
        # adds it to the graph
        # if the graph has no root, the created one is set
        if self.routerName:
            self.addRouter(self.routerName)
        else:
            # if already exists, pass the name to the graph
            graph[router] = self.routerName
        return {"addRouter": {"status": "success"}}

    # uses Dijstkra to get distance and path taken
    # between current router and named router
    def distance(self, router, network):
        # displaying router & network info
        display = ""
        display += f"router name: {self.routerName}\n"
        display += f"network connection: {self.networkConnection}\n"

        # defining start and end of path
        print("Start: " + self.routerName)
        print("End: " + router)
        # path and cost
        # path is added to list when Dijsktra runs
        print("Path: " + self.pathAndCost[0])
        # then remove so no build-up occurrs
        # and so we can access cost
        self.pathAndCost.pop(0)
        print("Cost: " + self.pathAndCost[0])
        # stopping build-up by removing from list when printed
        self.pathAndCost.pop(0)
        # path list
        # remove elements so we can use later
        self.p.pop(0)
        # cost list
        # remove elements so we can use later
        self.c.pop(0)

        return display

    # shortest path endpoint
    # Dijsktra's algorithm gets shortest path
    @app.post("/route")
    async def dijkstra(self, graph, origin, stop, passed=[], dist={}, oldNodes={}):
        # quit if:
        if origin == stop:
            pathD = []
            n = stop

            while n != None:
                pathD.append(n)
                n = oldNodes.get(n, None)

                readable = pathD[0]
                for i in range (1, len(pathD)):
                    readable = pathD[i] + '=' + readable

                    self.pathD.append(str(readable))
                    self.distanceCost.append(str(dist[stop]))

        else:
            if not passed:
                dist[origin] = 0

            for x in graph[origin]:
                if x not in passed:
                    newD = dist[origin] + graph[origin][x]

                    if newD < dist.get(x, float('inf')):
                        dist[x] = newD
                        self.connectionCost[x] = newD
                        oldNodes[x] = origin

            passed.append(origin)

            unpassed = {}

            for pnt in graph:
                if pnt not in passed:
                    unpassed[pnt] = dist.get(pnt, float('inf'))

            m = min(unpassed, key=unpassed.get, default="f")
            self.dijsktra(graph, m, origin, passed, dist, oldNodes)

    # remove router endpoint
    # function to remove router
    @app.post("/removerouter")
    async def remove(self, router):
        i = 0
        while i < len(Graph.conections):
            if len(self.distanceCost) != 0:
                # need to empty list every time so its ready to use
                self.distanceCost.pop(0)
            i += 1

        # deleting router name from dictionary where its stored
        if router in Graph.graph:
            del Graph.graph[router]

        for pnt, dict in Graph.graph.items():
            # creating a copy of values in dict to avoid RunTimeError due to changing dictionary size
            recordVals = dict.copy()

            # removing the router name from copy dict too
            for key in recordVals:
                if key == router:
                    del dict[router]

        # length of original graph
        # need this to know how many elements to remove from pathD
        # before an element is popped, it is placed here
        graphLen = len(Graph.connections)

        # removing router name from edges list
        i = 0
        while i < len(graph.connections):
            if Graph.connections[i] == router:
                Graph.connections.pop(i)
            i += 1

        if router in self.edgeCost:
            del self.connectionCost[router]

        i = 0
        if len(self.pathD) != 0:
            while i < graphLen:
                self.pathD.pop(0)
                i += 1
        return {"removerouter": {"name": "A"}}


# graphs are made up of points called nodes
# these nodes are joined together by lines called edges (connectors)
# in this graph, the nodes are routers
# the edges are pieces of the path (the connection)
# each edge / connection has a value called a cost
# so the edges with the smallest costs in total will make up the shortest path
class Graph():
    # graph is made up of edges joining routers
    graph = {}
    # contains edges on graph
    # when a new one is created it is appended to this list
    connections = []

    # connection endpoint
    # function to add a connection onto graph
    # going from current router to named router
    @app.post("/connect")
    async def addConnection(self, routerName, router, cost):
        # cost is the int value attached to the connection

        # if current router is not found in graph
        if routerName not in Graph.graph:
            # put its name in a seperate dictionary
            Graph.graph[routerName] = {}
            return {"connect": {"status": "updated"}}

        # if it is found
        # attach the name to the router and assign a cost
        Graph.graph[routerName][router] = int(cost)

        if router not in Graph.connections:
            # if router isnt in connections list put it in
            Graph.connections.append(router)
            return {"connect": {"status": "success"}}

        return {"connect": {"status": "Error, router does not exist"}}

    # remove connection endpoint
    @app.post("/removeconnection")
    async def removeConnection(self, networkConnection, ntwk):
        i = 0
        while i < len(Graph.connections):
            if len(self.networkConnection) != 0:
                self.networkConnection.pop(0)
            i +=1

        if ntwk in connections:
            connections.pop(networkConnection)
        return {"removeconnection": {"status": "success"}}



'''
# main function
# remove comments to test
def main() -> object:
    newG = Graph()
    newG.addConnection("a", "b", 5)
    newG.addConnection("a", "c", 7)
    newG.addConnection("a", "g", 9)
    newG.addConnection("a", "d", 11)
    newG.addConnection("a", "e", 13)

    newR = Router("a", newG)
    print("Part 1")
    #newR.distance("d")
    #print("\n")

if __name__=="__main__":
    main()
'''

# references / sources:
# "what is routing?" - https://www.cloudflare.com/en-gb/learning/network-layer/what-is-routing/
# 'graphs in python' - https://www.tutorialspoint.com/python_data_structure/python_graphs.htm
# 'Dijsktra's algorithm' - https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/?ref=rp
