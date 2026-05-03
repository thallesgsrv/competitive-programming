n, t = map(int, input().split())
Ni = list(map(int, input().split()))

j = 0
soma = 0
max_livros = 0

for i in range(n):
    if j < i:
        j = i
        soma = 0         
    while j < n and soma + Ni[j] <= t:
        soma += Ni[j]
        j += 1               
    
    max_livros = max(max_livros, j - i)
    soma -= Ni[i]
print(max_livros)

# This code is solving a problem where we have `n` books, each with a certain reading time, and a total available time `t`. The goal is to find the maximum number of books that can be read within the given time `t`. The code uses a two-pointer technique to efficiently calculate the sum of reading times for a contiguous sequence of books. It iterates through the list of book reading times, adjusting the pointers and keeping track of the maximum number of books that can be read without exceeding the total time `t`.
# The variable `j` is used to expand the window of books being considered, while `soma` keeps track of the total reading time for the current window. The code updates the maximum number of books whenever a valid window is found, and it ensures that the window does not exceed the total time `t`. Finally, it prints the maximum number of books that can be read.