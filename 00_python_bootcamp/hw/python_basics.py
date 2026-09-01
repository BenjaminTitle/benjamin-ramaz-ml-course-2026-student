"""HW00 — Python Bootcamp: Implementation

Complete the functions below. Each function has a docstring describing
what it should do, along with examples. Run `uv run pytest` to check
your work, and `uv run python score.py` to see your current grade.
"""
from __future__ import annotations

from typing import Callable
import math


# ── Part 1: Lists ─────────────────────────────────────────────────────────────


def flatten(nested: list[list]) -> list:
    """Return a single flat list from a list of lists.

    Examples:
        >>> flatten([[1, 2], [3, 4], [5]])
        [1, 2, 3, 4, 5]
        >>> flatten([[], [1]])
        [1]
        >>> flatten([])
        []
    """
    flat_list = []
    for inside_list in nested:
        for element in inside_list:
            flat_list.append(element)

    return flat_list


def most_frequent(items: list) -> object:
    """Return the element that appears most often in items.

    If there is a tie, returning any one of the tied elements is fine.
    Raise ValueError if items is empty.

    Examples:
        >>> most_frequent([1, 2, 2, 3])
        2
        >>> most_frequent(['a', 'b', 'a', 'c', 'a'])
        'a'
    """
    library=[]
    count=[]
    max_index=0
    if len(items) == 0:
        raise ValueError
    for element in items:
        if element not in library:
            library.append(element)
            count.append(1)
        else:
            count[library.index(element)] +=1

    for element in count:
        if element > count[max_index]:
            max_index = count.index(element)

    
    return library[max_index]

    

def running_average(numbers: list[float]) -> list[float]:
    """Return the cumulative average at each position.

    The i-th element of the result is the mean of numbers[0], ..., numbers[i].

    Examples:
        >>> running_average([10.0, 20.0, 30.0])
        [10.0, 15.0, 20.0]
        >>> running_average([4.0])
        [4.0]
        >>> running_average([])
        []
    """
    sum = 0
    length=1
    average_list=[]
    for element in numbers:
        
        sum += element
        average_list.append(sum/length)
        length += 1

    return average_list


def chunk(items: list, size: int) -> list[list]:
    """Split items into sublists of length size.

    The last sublist may be shorter if len(items) is not divisible by size.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk([1, 2, 3], 3)
        [[1, 2, 3]]
        >>> chunk([], 4)
        []
    """
    if size <= 0:
        raise ValueError
    chunked_list=[]
    current_index=0
    loop_amount=math.ceil(len(items)/size)
    for _ in range(loop_amount):
        chunked_list.append(items[(current_index):(current_index+size)])
        current_index += size

    return chunked_list 


def rotate(items: list, k: int) -> list:
    """Rotate items left by k positions.

    A negative k rotates right. If items is empty, return [].
    k larger than len(items) wraps around correctly.

    Examples:
        >>> rotate([1, 2, 3, 4, 5], 2)
        [3, 4, 5, 1, 2]
        >>> rotate([1, 2, 3], -1)
        [3, 1, 2]
        >>> rotate([1, 2, 3], 4)
        [2, 3, 1]
    """
    rotated_list=items[:]
    for element in items:
        rotated_list[(items.index(element) - k)%(len(items))] = element

    return rotated_list



def run_length_encode(items: list) -> list[tuple]:
    """Compress consecutive identical elements into (count, value) tuples.

    Examples:
        >>> run_length_encode(['a', 'a', 'b', 'b', 'b', 'a'])
        [(2, 'a'), (3, 'b'), (1, 'a')]
        >>> run_length_encode([1, 2, 3])
        [(1, 1), (1, 2), (1, 3)]
        >>> run_length_encode([])
        []
    """
    current_index=0
    run_list=[]
    streak=0
    location=0
    for element in items:
        
            if element == items[current_index]:
                streak+=1
                if location == len(items)-1:
                    run_list.append((streak,items[current_index]))
            else:
                run_list.append((streak,items[current_index]))
                current_index+=streak
                streak=1
                if location == len(items)-1:
                    run_list.append((streak,items[current_index]))
                    
            location+=1
                
            
    return(run_list)


def sliding_window(items: list, size: int) -> list[list]:
    """Return all consecutive windows of length size.

    Each window overlaps with the previous one by size-1 elements.
    If len(items) < size, return [].

    Examples:
        >>> sliding_window([1, 2, 3, 4, 5], 3)
        [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        >>> sliding_window([1, 2, 3], 2)
        [[1, 2], [2, 3]]
        >>> sliding_window([1, 2], 3)
        []
        >>> sliding_window([], 2)
        []
    """
    window_list=[]
    loop = 0
    for element in items:
        if loop + size <= len(items):
            temp_list=[]
            for i in range(size):
                temp_list.append(items[loop+i])
            loop+=1
            window_list.append(temp_list)
    return(window_list)


# ── Part 2: Dictionaries ──────────────────────────────────────────────────────


def count_occurrences(items: list) -> dict:
    """Return a dict mapping each unique element to its count in items.

    Examples:
        >>> count_occurrences(['a', 'b', 'a', 'c', 'b', 'b'])
        {'a': 2, 'b': 3, 'c': 1}
        >>> count_occurrences([])
        {}
    """
    count = {}
    for element in items:
        if element in count:
            count[element]+=1
        else:
            count[element]=1

    return(count)


def invert_dict(d: dict) -> dict:
    """Return a new dict with keys and values swapped.

    Examples:
        >>> invert_dict({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
    """
    second_dict={}
    for element in d:
        second_dict[d[element]]= element

    return second_dict


def group_by(items: list[dict], key: str) -> dict[str, list[dict]]:
    """Group a list of dicts by the value at the given key.

    Examples:
        >>> records = [
        ...     {'name': 'Alice', 'dept': 'Eng'},
        ...     {'name': 'Bob', 'dept': 'HR'},
        ...     {'name': 'Carol', 'dept': 'Eng'},
        ... ]
        >>> result = group_by(records, 'dept')
        >>> len(result['Eng'])
        2
        >>> len(result['HR'])
        1
    """
    output_dictionary={}
    for element in items:
        if element[key] not in output_dictionary:
            output_dictionary[element[key]]=[element]
        else:
            output_dictionary[element[key]].append(element)

    return(output_dictionary)


def deep_get(d: dict, path: str, default: object = None) -> object:
    """Retrieve a value from a nested dict using a dot-separated key path.

    Return default if any key along the path is missing.

    Examples:
        >>> deep_get({'a': {'b': {'c': 42}}}, 'a.b.c')
        42
        >>> deep_get({'a': 1}, 'a.b', default=-1)
        -1
        >>> deep_get({'x': 10}, 'y')  # returns None (default)
    """
    keys = path.split(".")
    current_dictionary=d
    for element in keys:
        if not isinstance(current_dictionary, dict):
            return default
        elif element not in current_dictionary:
            return default
        
        else:
            current_dictionary=current_dictionary[element]
    
    return current_dictionary



def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    """Return indices (i, j) where nums[i] + nums[j] == target, with i < j.

    Return None if no such pair exists.

    Hint: There is an elegant O(n) solution using a dict. As you scan through
    nums, ask: "have I already seen the number I need to pair with this one?"

    Examples:
        >>> two_sum([2, 7, 11, 15], 9)
        (0, 1)
        >>> two_sum([3, 2, 4], 6)
        (1, 2)
        >>> two_sum([1, 2, 3], 100)
        None
    """
    count={}
    loop=0
    for element in nums:
        if (target-element) in count:
            return((count[target-element], loop))
        
        else:
            count[element]=loop
            loop +=1

    return(None)


# ── Part 3: Sets ──────────────────────────────────────────────────────────────


def find_duplicates(items: list) -> set:
    """Return the set of elements that appear more than once in items.

    Examples:
        >>> find_duplicates([1, 2, 2, 3, 3, 3, 4])
        {2, 3}
        >>> find_duplicates([1, 2, 3])
        set()
        >>> find_duplicates([])
        set()
    """
    seen=set()
    duplicates=set()
    for element in items:
        if element in seen:
            duplicates.add(element)
        else:
            seen.add(element)

    return(duplicates)



def jaccard_similarity(a: set, b: set) -> float:
    """Return |A intersection B| / |A union B|.

    Return 0.0 if both sets are empty.

    Examples:
        >>> jaccard_similarity({1, 2, 3}, {2, 3, 4})
        0.5
        >>> jaccard_similarity({1, 2}, {3, 4})
        0.0
        >>> jaccard_similarity(set(), set())
        0.0
    """
    intersection=a.intersection(b)
    union=a.union(b)
    if len(union) != 0:
        return(len(intersection)/len(union))
    else:
        return(0.0)


# ── Part 4: Higher-order functions ────────────────────────────────────────────


def apply_twice(f: Callable, x: object) -> object:
    """Apply f to x, then apply f to the result: f(f(x)).

    Examples:
        >>> apply_twice(lambda n: n * 2, 3)
        12
        >>> apply_twice(str.upper, 'hello')
        'HELLO'
    """
    return(f(f(x)))
    
    raise NotImplementedError("Implement apply_twice()")


def make_multiplier(n: float) -> Callable[[float], float]:
    """Return a function that multiplies its argument by n.

    Each call to make_multiplier returns an independent function.

    Examples:
        >>> double = make_multiplier(2)
        >>> double(5)
        10.0
        >>> triple = make_multiplier(3)
        >>> triple(4)
        12.0
    """
    def multiplication(x: int):
        return(n*x)
    return (multiplication)
    raise NotImplementedError("Implement make_multiplier()")


def pipeline(*funcs: Callable) -> Callable:
    """Return a single function that applies each func in sequence (left to right).

    pipeline(f, g, h)(x) is equivalent to h(g(f(x))).
    If no functions are provided, the returned function is the identity: f(x) == x.

    Examples:
        >>> add1 = lambda x: x + 1
        >>> double = lambda x: x * 2
        >>> pipeline(add1, double)(3)
        8
        >>> pipeline()(42)
        42
    """
    def identity(x:int):
        return(x)
    if len(funcs)==0:
        return (identity)
    else:
        def pipelined_function(x:int):
            value = x
            for i in range(len(funcs)):
                value = funcs[i](value)
            return(value)
        return pipelined_function


    raise NotImplementedError("Implement pipeline()")


def memoize(f: Callable) -> Callable:
    """Return a version of f that caches results by argument.

    Calling the memoized function with the same argument a second time
    must return the cached result WITHOUT calling f again.

    Use a closure over a dict to store previously computed results.

    Examples:
        >>> call_count = 0
        >>> def tracked(x):
        ...     global call_count
        ...     call_count += 1
        ...     return x ** 2
        >>> cached = memoize(tracked)
        >>> cached(4)
        16
        >>> cached(4)   # should not increment call_count
        16
    """
    memory={}
    def memoized_function(x:int):
        
        if x in memory:
            return memory[x]
        else:
            memory[x]=f(x)
            return memory[x]
    return memoized_function

# ── Part 5: Classes ───────────────────────────────────────────────────────────


class Student:
    """A student with a name and a list of grades (0-100).

    Supports comparison via average grade, enabling natural sorting.
    """

    def __init__(self, name: str, grades: list[float]) -> None:
        self.name = name
        self.grades = grades

    def average(self) -> float:
        """Return the mean of all grades. Returns 0.0 if grades is empty."""
        sum = 0
        if len(self.grades) == 0:
            return 0.0
        else:
            for element in self.grades:
                sum += element
            return (sum/len(self.grades))

    def highest(self) -> float:
        """Return the highest grade. Returns 0.0 if grades is empty."""
        max = 0
        if len(self.grades) == 0:
            return 0.0
        else:
            for element in self.grades:
                if element > max:
                    max = element
            return max

    def letter_grade(self) -> str:
        """Return the letter grade for this student's average.

        Boundaries: A >= 90, B >= 80, C >= 70, D >= 60, F otherwise.
        """
        grade_average=self.average()
        if grade_average>=90:
            return "A"
        elif grade_average >=80:
            return "B"
        elif grade_average >= 70:
            return "C"
        elif grade_average >= 60:
            return "D"
        else:
            return "F"

    def __repr__(self) -> str:
        """Return a string like: Student('Alice', avg=88.5)"""
        return "Student('" + self.name + "', avg=" + str(self.average()) + ")"

    def __lt__(self, other: "Student") -> bool:
        """Compare students by average grade (enables sorted() and min/max)."""
        return self.average() < other.average()


class Gradebook:
    """Manages a collection of students, keyed by name."""

    def __init__(self) -> None:
        self.students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        """Add a student to the gradebook.

        Raises ValueError if a student with the same name already exists.
        """
        if student.name not in self.students:
            self.students[student.name] = student
        else:
            raise ValueError

    def top_students(self, n: int) -> list[Student]:
        """Return the n students with the highest averages, in descending order."""
        #sorted_grade_list = [0] * n
        #for element in self.students:
        #    for i in range(n):
        #        if element.average() > sorted_grade_list[i]:
        #            sorted_grade_list[i] = element.average()
        #            break
        ranked_students = []
        for element in self.students:
            ranked_students.append(self.students[element])

        ranked_students = sorted(ranked_students, reverse=True)
        return(ranked_students[:n])

    def class_average(self) -> float:
        """Return the mean of all student averages. Returns 0.0 if empty."""
        sum = 0
        class_size = len(self.students)
        if class_size == 0:
            return 0.0
        else:
            for element in self.students:
                sum += self.students[element].average()

        return (sum/class_size)

