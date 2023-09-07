## Given 2 directed Graph's - Find if path exists in between them

customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }

def myGraphRoute(myDict,node1,node2):
    visited=[node1]
    queue =[node1]

    while queue:
        vertex = queue.pop(0)
        for adjacentV in myDict[vertex]:
            if adjacentV not in visited:
                if adjacentV == node2:
                    return "Path Exists"
                else:
                    queue.append(adjacentV)
                    visited.append(adjacentV)
                    
    return "Path DO NOT Exists"   

print(myGraphRoute(customDict,"a","b"))