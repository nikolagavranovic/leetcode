from solution import Solution
import pytest


s = Solution()


# @pytest.mark.parametrize("test_input,expected", [("3+3", 8), ("2+4", 6), ("6*9", 42)])
# def test_eval(test_input, expected):
#     assert eval(test_input) == expected


def test_words_fail():
    fruits1 = ["banana", "apple", "grapes", "melon", "kiwi"]
    fruits2 = ["banana", "apple", "orange", "melon", "kiwi"]
    assert fruits1 == fruits2


# @pytest.mark.parametrize("test_input,expected", [(19, True), (2, False)])
# def test_eval(test_input, expected):
#     assert s.isHappy(test_input) == expected
