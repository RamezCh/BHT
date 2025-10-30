class Expressions:
    """"
    Fill in one-line expressions (no own functions) to initialize attributes
    self.b .. self.k with specified values.

    Use Python built-in functions, list expressions and list comprehension,
    but NOT own functions.

    Complete tasks one after another. Once you are done with one task,
    uncomment test cases in test_expressions.py. Remove comments for
      # Test_case_b = Test_case
      # Test_case_c = Test_case
      # Test_case_d = Test_case
      # ...
    Run tests in IDE and in a terminal:
      python test_expressions.py
      python -m unittest
    """

    default_numbers=[4, 12, 3, 8, 17, 12, 1, 8, 7]

    def __init__(self, _numbers=default_numbers):
        """
        Constructor to initialize member variables.
        """
        self.numbers = _numbers

        # a) initialize with number of numbers: 9
        self.a = len(self.numbers)    # <-- given solution, insert one-line expressions below

        # b) initialize with first three numbers: [4, 12, 3]
        self.b = [*_numbers[:3]]      # <-- write expression here

        # c) initialize with last three numbers: [1, 8, 7]
        self.c = [*_numbers[-3:]]

        # d) initialize with last three numbers reverse: [7, 8, 1]
        self.d = [*_numbers[-3:][::-1]]

        # e) initialize with odd numbers: [3, 17, 1, 7]
        self.e = [num for num in _numbers if num % 2 != 0]

        # f) initialize with number of odd numbers: 4
        self.f = sum(num % 2 for num in _numbers) # remember modulus gets remainder so for odd it is 1 and even 0

        # g) initialize with sum_ of odd numbers: 28
        self.g = sum(num for num in _numbers if num % 2 != 0)

        # h) duplicate numbers removed: [4, 12, 3, 8, 17, 1, 7]
        self.h = list(dict.fromkeys(_numbers))

        # i) number of duplicate numbers: 2
        self.i = len(_numbers) - len(self.h)

        # j) ascending list of squared numbers with no duplicates: [1, 9, 16, 49, 64, 144, 289]
        self.j = [num * num for num in sorted(self.h)]

        # k) initialize with "ODD_LIST", "EVEN_LIST" or "EMPTY_LIST" depending on numbers length
        self.k ="EMPTY_LIST" if not _numbers else "EVEN_LIST" if len(_numbers) % 2 == 0 else "ODD_LIST"


    def print_results(self):
        print(f'\nnumbers: {self.numbers}\n#')
        fmt = {
            # key: (value, output string)
            'a': (self.a, 'number of numbers'),
            'b': (self.b, 'first three numbers'),
            'c': (self.c, 'last three numbers'),
            'd': (self.d, 'last three numbers reverse'),
            'e': (self.e, 'odd numbers'),
            'f': (self.f, 'number of odd numbers'),
            'g': (self.g, 'sum of odd numbers'),
            'h': (self.h, 'duplicate numbers removed'),
            'i': (self.i, 'number of duplicate numbers'),
            'j': (self.j, 'ascending, de-dup (n^2) numbers'),
            'k': (self.k, 'length'),
        }
        # format output, e.g.: "b) first three numbers: [1, 4, 6]"
        for k in sorted(fmt.keys()):
            print(f'{k}) {fmt[k][1]}: {fmt[k][0]}')