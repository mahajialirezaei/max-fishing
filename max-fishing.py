maximumOfProblem = 0


def start(grid, m, n):
    for i in range(m):
        for j in range(n):
            visited = set()
            if grid[i][j] != 0:
                visited.add(tuple([i, j]))
                maxFishing(grid, m, n, i, j, visited, grid[i][j])


def check(grid, i, j, visited):
    return i>=0 and j>=0 and i < len(grid) and j < len(grid[i]) and tuple([i, j]) not in visited and grid[i][j]!= 0


def maxFishing(grid, m, n, i, j, visited, cur):
    global maximumOfProblem
    maximumOfProblem = max(maximumOfProblem, cur)
    if check(grid, i + 1, j, visited):
        visited.add(tuple([i + 1, j]))
        cur += grid[i + 1][j]
        maxFishing(grid, m, n, i + 1, j, visited, cur)
        visited.remove(tuple([i + 1, j]))
        cur -= grid[i + 1][j]
    if check(grid, i, j + 1, visited):
        visited.add(tuple([i, j + 1]))
        cur += grid[i][j + 1]
        maxFishing(grid, m, n, i, j + 1, visited, cur)
        visited.remove(tuple([i, j + 1]))
        cur -= grid[i][j + 1]
    if check(grid, i - 1, j, visited):
        visited.add(tuple([i - 1, j]))
        cur += grid[i - 1][j]
        maxFishing(grid, m, n, i - 1, j, visited, cur)
        visited.remove(tuple([i - 1, j]))
        cur -= grid[i - 1][j]
    if check(grid, i, j - 1, visited):
        visited.add(tuple([i, j - 1]))
        cur += grid[i][j - 1]
        maxFishing(grid, m, n, i, j - 1, visited, cur)
        visited.remove(tuple([i, j - 1]))
        cur -= grid[i][j - 1]



grid = [
[0, 2, 1, 0],
[4, 0, 0, 3],
[1, 0, 0, 4],
[0, 3, 2, 0]
]

m = 4
n = 4
start(grid, m, n)
print(maximumOfProblem)