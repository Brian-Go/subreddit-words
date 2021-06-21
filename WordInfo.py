class WordInfo:
    def __init__(self, word):
        self.word = word
        self.count = 0
        self.found_in = {}
        self.unique = 0
        self.value = 0
    
    def __str__(self):
        return str([self.word, self.count, self.unique, self.value])

    def __repr__(self):
        return str([self.word, self.count, self.unique, self.value])

    def add_instance(self, post, comment):
        self.count +=1
        if not post in self.found_in:
            self.unique +=1
            self.found_in[post] = [comment]
        else:
            self.found_in[post] += [comment]
        self.value = self.count * self.unique


