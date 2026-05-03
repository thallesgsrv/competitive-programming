def solve():
    n = int(input())
    parent = [0] * (n + 1)
    
    for i in range(1, n + 1):
        parent[i] = int(input())
    
    dp = [-1] * (n + 1)
    
    for i in range(1, n + 1):
        if dp[i] != -1:
            continue
        
        path = []
        curr = i
        
        while curr != -1 and dp[curr] == -1:
            path.append(curr)
            curr = parent[curr]
        
        if curr == -1:
            val = 0
        else:
            val = dp[curr]
        
        for node in reversed(path):
            val += 1
            dp[node] = val
    
    print(max(dp[1:]))

if __name__ == "__main__":
    solve()

# This code is solving a problem where we have `n` nodes, and each node has a parent node. The input consists of `n` integers, where the `i`-th integer represents the parent of the `i`-th node. The code calculates the depth of each node in the tree formed by these parent-child relationships and finds the maximum depth among all nodes.
# The code uses a dynamic programming approach to store the depth of each node in the `dp` array. It iterates through each node, and if the depth of that node has not been calculated yet (i.e., `dp[i] == -1`), it follows the parent pointers until it reaches a node whose depth is already known or reaches the root (where the parent is -1). It then backtracks through the path taken, updating the depth of each node along the way. Finally, it prints the maximum depth found among all nodes.
# For example, if we have `n = 5` and the parent array is `[-1, 1, 1, 2, 2]`, the tree structure would be:
# - Node 1 is the root (parent is -1)
# - Nodes 2 and 3 are children of Node 1
# - Nodes 4 and 5 are children of Node 2
# The depths would be:
# - Node 1: depth 1
# - Node 2: depth 2
# - Node 3: depth 2
# - Node 4: depth 3
# - Node 5: depth 3
# The maximum depth in this case would be 3, which is the output of the code.
