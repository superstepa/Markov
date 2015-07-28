import random
import sys


class Markov(object):
    def __init__(self, f):
        self.chain = {}
        self.file = f
        self.words = self.file_to_words()
        self.generate_chain()

    def file_to_words(self):
        with open(self.file, "r") as text:
            return text.read().split()

    def generate_trigrams(self):
        if len(self.words) < 3:
            return
        for i in range(len(self.words) - 2):
            yield (self.words[i], self.words[i+1], self.words[i+2])

    def generate_chain(self):
        for w1, w2, w3 in self.generate_trigrams():
            key = (w1, w2)
            if key in self.chain:
                self.chain[key].append(w3)
            else:
                self.chain[key] = [w3]

    def generate_text(self, size=100):
        rng = random.randint(0, len(self.words) - 3)
        word1, word2 = self.words[rng], self.words[rng+1]
        text = []
        for i in range(size):
            text.append(word1)
            word1, word2 = word2, random.choice(self.chain[(word1, word2)])
        text.append(word2)
        text[0].upper()
        return ' '.join(text)

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        raise ValueError("Usage: markov.py <inputfile> <length>")
    markov = Markov(str(sys.argv[1]))
    with open("out.txt", "w+") as file:
        file.write(markov.generate_text(int(sys.argv[2])))
