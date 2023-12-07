# You can copy/paste this template to start a new day

"""01: Trebuchet?!"""
import aoc.util
import regex
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

    def replace_word_with_digit_from_start(self, text_in: str) -> List[str]:
        words = {
            "one": 1,
            "two": 2,
            "three": 3,
            "four": 4,
            "five": 5,
            "six": 6,
            "seven": 7,
            "eight": 8,
            "nine": 9,
        }

        word_stack = ""
        digit_pattern = r"[0-9]+|one|two|three|four|five|six|seven|eight|nine"
        matches = regex.findall(pattern=digit_pattern, string=text_in, overlapped=True)
        if matches:
            for match in matches:
                if match.isnumeric():
                    word_stack += match
                else:
                    word_stack += f"{words[match]}"

        # word_stack = regex.sub(pattern=digit_pattern, repl=lambda grp: f"{words[grp[0]]}", string=text_in,)
        number_str = "".join([i for i in word_stack if i.isdigit()])
        new_num = f"{number_str[0]}{number_str[-1]}"
        return int(new_num)

    def part_two(self) -> int:
        sums = 0
        for line in self.input.split("\n"):
            stripped = self.replace_word_with_digit_from_start(line)
            sums += stripped
        return sums
