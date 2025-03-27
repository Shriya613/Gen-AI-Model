# Markov chain

import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list) # dictionary that produces lists for the graph

# Gets rid of punctuation and numbers, replaces new lines with spaces, and splits the text into a list of words
    def _tokenize(self, text):
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split(" ")
        )
#builds the graph for generation
    def train(self, text):
        tokens = self._tokenize(text)
        for i, token in enumerate(tokens): #looping through tokens using enumerate [i is counter for next token]
            if (len(tokens) - 1) == i: #for the last token, break the loop
                break
            self.graph[token].append(tokens[i+1])  # else look up the key for the token, if there's nothing, it will give an empty list which will have the next token appended to it   


    def generate(self, prompt, length=10):
        # get the lask token from the prompt
        current = self._tokenize(prompt)[-1]
        # initialize the output
        output = prompt
        for i in range(length):
            # look up the options in the graph dictionary
            options = self.graph.get(current, [])
            if not options:
                continue
            # use random.choice method to pick a current option
            current = random.choice(options)
            # add the random choice to the output string
            output += " " + current
        return output