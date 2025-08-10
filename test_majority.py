import importlib.util
from pathlib import Path

# Dynamically load the majority module from the Week-4 directory
module_path = Path(__file__).resolve().parent / 'Week-4' / 'majority.py'
spec = importlib.util.spec_from_file_location('majority', module_path)
majority = importlib.util.module_from_spec(spec)
spec.loader.exec_module(majority)


def has_majority(seq):
    return majority.divide_func(seq, 0, len(seq)) != -1


def test_no_majority_two_elements():
    assert has_majority([1, 2]) is False


def test_majority_two_elements():
    assert has_majority([2, 2]) is True

