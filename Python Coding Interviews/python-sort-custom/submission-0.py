from typing import List

def get_str_length(characters: str) -> int:
    return len(characters)

def get_int_length(nums: int) -> int:
    return abs(nums)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=get_str_length, reverse=True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_int_length)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
