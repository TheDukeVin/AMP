def bfs(graph, root):
    visited=set()
    queue = [root]
    visited.add(root)

    while queue:
        vertex = queue.pop(0)
        print(f"{str(vertex)} ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

def bfs_path(graph, root, target):
    queue = [[root]]
    
    while queue:
        old_path = queue.pop(0)
        last_node = old_path[-1]

        for neighbour in graph[last_node]:
            if neighbour not in old_path:
                new_path = list(old_path)
                new_path.append(neighbour)
                queue.append(new_path)
        
            if neighbour == target:
                return new_path
            
if __name__ == "__main__":

    friends1 = {
        'Alice':['Bob'],
        'Bob':['Alice', 'Eve'],
        'Eve':['Bob']
    }
    bfs(friends1, 'Alice')
    print()

    friends2 = {
        'Asa':[], 
        'Bear':['Cate'],
        'Cate':['Bear', 'Dave'],
        'Dave':['Cate','Eve'], 
        'Eve':['Dave'], 
        'Finn':['Ginny', 'Haruki', 'Ivan'], 
        'Ginny':['Finn','Haruki'], 
        'Haruki':['Ginny'], 
        'Ivan':['Finn']
    }
    bfs(friends2, 'Bear')
    print()
    bfs(friends2, 'Finn')
    print() 

    test = {
        'a': ['b', 'c'],
        'b': ['d', 'e', 'f', 'a'],
        'c': ['a'],
        'd': ['b'],
        'e': ['b'],
        'f': ['b']
    }
    #bfs(test, 'a')
    #bfs(test, 'e')
    print(bfs_path(test,'c', 'e'))
    print() 