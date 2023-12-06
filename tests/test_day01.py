import pytest

from aoc.day01 import Solver
from aoc.util import Solution


#############################
# ======= solutons =========#
#############################
EXAMPLE_PART_ONE = 142
EXAMPLE_PART_TWO = 281
PART_ONE = 53080
PART_TWO = 0


#############################
# ========= setup ==========#
#############################
@pytest.fixture
def example_input() -> str:
    with open("inputs/day01_example.txt", "r") as f:
        return f.read()


@pytest.fixture
def example_two_input() -> str:
    with open("inputs/day01_part2_example.txt", "r") as f:
        return f.read()


@pytest.fixture
def real_input() -> str:
    with open("inputs/day01.txt", "r") as f:
        return f.read()


@pytest.fixture
def example_solver(example_input: str) -> Solver:
    return Solver(example_input)


@pytest.fixture
def example_two_solver(example_two_input: str) -> Solver:
    return Solver(example_two_input)


@pytest.fixture
def real_solver(real_input: str) -> Solver:
    return Solver(real_input)


#############################
# === tests for part one ===#
#############################
@pytest.mark.example
def test_example_part_one(example_solver: Solver):
    assert example_solver.part_one() == EXAMPLE_PART_ONE


@pytest.mark.real
def test_real_part_one(real_solver: Solver):
    assert real_solver.part_one() == PART_ONE


#
#############################
# === tests for part two ===#
#############################
@pytest.mark.parametrize(
    argnames=["test_input", "correct_answer"],
    argvalues=[
        ("1sixnine9", "1699"),
        ("1oneoneightwo9", "1189"),
        ("threeccbdtsrfv4drmvqcbdsix7sevenfiven", "346775"),
        ("pbkprbzvs819threeonekjpk7brkmbqbkgroneightb", "8193171"),
    ],
)
def test_replace_word_with_digit(example_two_solver: Solver, test_input, correct_answer):
    assert example_two_solver.replace_word_with_digit(test_input) == correct_answer


@pytest.mark.example
def test_example_part_two(example_two_solver: Solver):
    assert example_two_solver.part_two() == EXAMPLE_PART_TWO


@pytest.mark.real
def test_real_part_two(real_solver: Solver):
    assert real_solver.part_two() == PART_TWO


#############################
# ======= benchmarks =======#
#############################
@pytest.mark.bench
def test_day01(benchmark, real_input: str):
    expected = Solution(part_one=PART_ONE, part_two=PART_TWO)
    result = benchmark(Solver.solve, real_input)

    # let's just leverage the diffs pytest will provide for better output
    assert result.__dict__ == expected.__dict__
