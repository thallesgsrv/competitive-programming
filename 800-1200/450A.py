n, m = map(int, input().split())
a = list(map(int, input().split()))

max_rodadas =0
ultimo = 0
for i in range(n):
    rodadas = (a[i] + m - 1) // m
    if rodadas >= max_rodadas:
        max_rodadas = rodadas
        ultimo = i + 1 
print(ultimo)

# This code is solving a problem where we have `n` integers representing the number of rounds needed for each player, and a parameter `m` representing the maximum number of rounds that can be played in one turn. The code calculates the number of turns (rodadas) needed for each player by dividing their respective integer by `m` and rounding up. It keeps track of the maximum number of turns needed and the index of the last player who requires that many turns. Finally, it prints the index of the last player who requires the maximum number of turns.
# The logic behind this is that for each player, we need to determine how many turns they will take based on their required rounds and the maximum rounds per turn. By using integer division and adjusting for rounding up, we can calculate the number of turns for each player. The code then compares these values to find the maximum and keeps track of the last player who reaches that maximum. This allows us to determine which player will be the last one to finish their required rounds.
# For example, if we have `n = 3`, `m = 2`, and the list of rounds is `[3, 4, 5]`, the code will calculate the turns for each player as follows:
# - Player 1: (3 + 2 - 1) // 2 = 2 turns
# - Player 2: (4 + 2 - 1) // 2 = 3 turns
# - Player 3: (5 + 2 - 1) // 2 = 3 turns
# The maximum number of turns is 3, and the last player to reach that maximum is Player 3, so the output will be 
# `3`.