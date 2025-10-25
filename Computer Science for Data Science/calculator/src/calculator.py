class Calculator:
    def __init__(self):
        self.number_mappings = {
            'english': {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9},

            'german': {'null': 0, 'eins': 1, 'zwei': 2, 'drei': 3, 'vier': 4,
                       'fünf': 5, 'sechs': 6, 'sieben': 7, 'acht': 8, 'neun': 9},

            'spanish': {'cero': 0, 'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4,
                        'cinco': 5, 'seis': 6, 'siete': 7, 'ocho': 8, 'nueve': 9},

            'russian': {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4,
                        'пять': 5, 'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9},

            'chinese': {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4,
                        '五': 5, '六': 6, '七': 7, '八': 8, '九': 9},
        }

        # Create a unified lookup dictionary with case-insensitive support
        self.unified_mapping = {}
        for lang_dict in self.number_mappings.values():
            self.unified_mapping.update(lang_dict)

        # Add Latin numerals separately since they need special handling
        self.latin_numerals = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5,
                               'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9}

    def _parse_latin_numeral(self, value):
        """Parse Roman numerals (case-insensitive)"""
        roman_map = {'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 'd': 500, 'm': 1000}

        value_lower = value.lower()
        result = 0
        prev_value = 0

        for char in reversed(value_lower):
            current_value = roman_map.get(char, 0)

            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value

            prev_value = current_value

        return result

    def _parse_input(self, value):
        """Convert any supported input to number (case-insensitive)"""
        # If it's already a number, return as-is (your simple approach)
        if isinstance(value, (int, float)):
            return value

        if isinstance(value, str):
            # First try to parse as a number (int or float)
            try:
                # Try int first
                return int(value)
            except ValueError:
                try:
                    # Then try float
                    return float(value)
                except ValueError:
                    pass

            # Convert to lowercase for case-insensitive lookup
            value_lower = value.lower()

            # Check if it's in our unified mapping (case-insensitive)
            if value_lower in self.unified_mapping:
                return self.unified_mapping[value_lower]

            # Check if it's a Latin numeral from our basic set
            if value_lower in self.latin_numerals:
                return self.latin_numerals[value_lower]

            # Try to parse as Roman numeral
            try:
                roman_value = self._parse_latin_numeral(value)
                if roman_value > 0 and roman_value <= 100:
                    return roman_value
            except:
                pass

            # Special handling for Chinese and Russian - check original case
            if value in self.unified_mapping:
                return self.unified_mapping[value]

        raise ValueError(f"Cannot parse input: {value}")

    def add(self, x, y):
        """Add two numbers, supporting multiple formats and cases"""
        x_num = self._parse_input(x)
        y_num = self._parse_input(y)
        return x_num + y_num

    def sub(self, x, y):
        """Subtract two numbers, supporting multiple formats and cases"""
        x_num = self._parse_input(x)
        y_num = self._parse_input(y)
        return x_num - y_num

    def mul(self, x, y):
        """Multiply two numbers, supporting multiple formats and cases"""
        x_num = self._parse_input(x)
        y_num = self._parse_input(y)
        return x_num * y_num

    def div(self, x, y):
        """Divide two numbers, supporting multiple formats and cases"""
        x_num = self._parse_input(x)
        y_num = self._parse_input(y)
        if y_num == 0:
            raise ValueError("Cannot divide by zero")
        return x_num / y_num

    def factorize(self, n):
        """
        Factorize a number into its prime factors.
        Supports multiple input formats and cases.
        Only works with integers.
        """
        number = self._parse_input(n)

        # Ensure we have an integer for factorization
        if isinstance(number, float):
            if number.is_integer():
                number = int(number)
            else:
                raise ValueError("Factorization only works with integers")

        if number < 2:
            return []

        factors = []
        divisor = 2

        while divisor * divisor <= number:
            while number % divisor == 0:
                factors.append(divisor)
                number //= divisor
            divisor += 1

        if number > 1:
            factors.append(number)

        return factors