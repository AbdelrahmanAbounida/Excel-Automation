def findWordsUtil(self, visited, i, j, Str):
    # Mark current cell as visited and
    # append current character to str
    visited[i][j] = True
    Str = Str + self.grid[i][j]
    M, N = len(self.grid), len(self.grid[0])
    # If str is present in dictionary,
    # then print it
    if (Str in self.possible_words):
        print(Str)

    # Traverse 8 adjacent cells of boggle[i,j]
    row = i - 1
    while row <= i + 1 and row < M:
        col = j - 1
        while col <= j + 1 and col < N:
            if (row >= 0 and col >= 0 and not visited[row][col] and Str in self.prefix):
                self.findWordsUtil(visited, row, col, Str)
            col += 1
        row += 1

    # Erase current character from string and
    # mark visited of current cell as false
    Str = "" + Str[-1]
    visited[i][j] = False


# Prints all words present in dictionary.
def findWords(self):
    # Mark all characters as not visited
    M, N = len(self.grid), len(self.grid[0])
    visited = [[False for i in range(N)] for j in range(M)]

    # Initialize current string
    Str = ""

    # Consider every character and look for all words
    # starting with this character
    for i in range(M):
        for j in range(N):
            self.findWordsUtil(visited, i, j, Str)