class TLT():
    def __init__(self):
        self.grid_size = 0
        self.grid = []
        self.possible_words = []
        self.existing_possible_words = []
        self.prefix = []
        self.true_words = []

    def begin(self, filename):
        self.retrieve_grid(filename)
        self.retrieve_possible_words(filename)
        for i in self.possible_words:
            for k in self.prefixes(i):
                self.prefix.append(k)

    def retrieve_grid(self, file_name):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            self.grid_size = int(lines[0])

            for i in lines[2:3 + self.grid_size]:
                a = i.split(',')
                if (len(a) > 1):
                    a[-1] = a[-1].strip()
                    self.grid.append(a)

    def retrieve_possible_words(self, file_name):
        if self.grid_size == 0:
            self.retrieve_grid(file_name)
        with open(file_name, 'r') as f:
            lines = f.readlines()

            for i in lines[3 + self.grid_size:]:
                a = i.split(' ')
                if len(a) > 0:
                    for k in a:
                        self.possible_words.append(k.strip())

    def prefixes(self, word):
        out = []
        for i in range(2, len(word)):
            out.append(word[0:i])
        return out

    def neighbors(self, pos):
        x, y = pos[0], pos[1]
        for nx in range(max(0, x - 1), min(x + 2, len(self.grid[0]))):
            for ny in range(max(0, y - 1), min(y + 2, len(self.grid))):
                yield nx, ny

    def find_words_rec(self, pref, path):

        if pref in self.possible_words and pref not in self.true_words :
            self.true_words.append(pref)
            yield pref

        for (nx, ny) in self.neighbors(path[-1]):
            if (nx, ny) not in path:
                prefix1 = pref + self.grid[nx][ny]
                if prefix1 in self.prefix:
                    for result in self.find_words_rec(prefix1, path + ((nx, ny),)):
                        yield result

    def find_all_the_words(self):
        res = []
        for y, row in enumerate(self.grid):
            for x, letter in enumerate(row):
                for result in self.find_words_rec(letter, ((x, y),)):
                    res.append(result)
        return res





x = TLT()
x.begin('grid_1.txt')
a = x.find_all_the_words()
print(f"allowable words: {x.possible_words}")
print(f"right words: {a}")
