n, m = map(int, input().split())

cidades = list(map(int, input().split()))
torres = list(map(int, input().split()))

j = 0 
max_distancia = 0
for c in cidades:
    while j + 1 < m and abs(c - torres[j]) >= abs(c - torres[j + 1]):
        j += 1
    
    distacia = abs(c - torres[j])
    max_distancia = max(max_distancia, distacia)

print(max_distancia)

# This code is solving a problem where we have two lists: `cidades` (cities) and `torres` (towers). The goal is to find the maximum distance from any city to the nearest tower. The code iterates through each city and uses a while loop to find the closest tower by comparing the distances to the current tower and the next tower. It keeps track of the maximum distance found and prints it at the end.
# The variable `j` is used to keep track of the current tower being compared, and `max_distancia` is updated whenever a greater distance is found. Finally, the code outputs the maximum distance from any city to the nearest tower.