# You can copy/paste this template to start a new day

"""01: Trebuchet?!"""
import aoc.util
from typing import List


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)

        # optionally do something with self.input, like parsing it to a more
        # useful representation and storing it in the instance

    def part_one(self) -> int:
        sums = 0
        for line in self.input.split("\n"):
            stripped = [i for i in line if i.isdigit()]
            if stripped:
                new_num = f"{stripped[0]}{stripped[-1]}"
                new_num = int(new_num)
                sums += new_num
        return sums

    def replace_word_with_digit(self, text_in:str) -> List[str]:
        words = {
            'one':1,
            'two':2,
            'three':3,
            'four':4,
            'five':5,
            'six':6,
            'seven':7,
            'eight':8,
            'nine':9,
        }
        matches = []
        for k,_ in words.items():
            if k in text_in:
                text_in.index
                match = (k, text_in.index(k))
                matches.append(match)
        matches.sort(key=lambda x: x[1])
        if matches:
            for match,_ in matches:
                text_in = text_in.replace(match,f"{words[match]}",1)

        return "".join([i for i in text_in if i.isdigit()])
    
    def part_two(self) -> int:
        sums = 0
        for line in self.input.split("\n"):
            stripped = self.replace_word_with_digit(line)
            if stripped:
                new_num = f"{stripped[0]}{stripped[-1]}"
                new_num = int(new_num)
                sums += new_num
        return sums
