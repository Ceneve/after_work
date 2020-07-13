class FirstNumberError(ValueError):
    pass


class NumbersInListError(ValueError):
    pass


class OutOfRangeError(ValueError):
    pass


class BigNumber:

    @staticmethod
    def validate(value):
        if value[0] == 0:
            raise FirstNumberError("First digit cannot be 0")
        if not type(value) == list:
            raise TypeError("The value must be passed in a list")
        for i in range(0, len(value)):
            if not type(value[i]) == int:
                raise NumbersInListError(
                    "The value in the list must be numbers"
                )
            if value[i] not in range(0, 10):
                raise OutOfRangeError(
                    "The value in the list must be in range 0 to 9"
                )

    def __init__(self, value):
        self.validate(value)
        self.digits = value[::-1]

    def __add__(self, other):
        other = other[::-1]
        if len(self.digits) >= len(other):
            first = self.digits
            second = other
        else:
            first = other
            second = self.digits
        i = 0
        result = []
        while True:
            if not len(second) <= i:
                mod = first[i] + second[i] % 10
                if mod >= 10:
                    div = mod // 10
                    mod = mod % 10
                    result.append(mod)
                    if first[i + 1]:
                        first[i + 1] = first[i + 1] + div
                    else:
                        first.append(div)
                else:
                    result.append(mod)
                i = i + 1
            else:
                while len(first) >= i+1:
                    result.append(first[i])
                    i = i + 1
                break
        j = 0
        while len(result) > j:
            if result[j] >= 10:
                div = result[j] // 10
                mod = result[j] % 10
                result[j] = mod
                if result[j + 1]:
                    result[j + 1] = result[j + 1] + div
                else:
                    result.append(div)
            j = j + 1
        return result[::-1]

    def __sub__(self, other):
        other = other[::-1]
        result = []
        if self.digits == other:
            result.append(0)
            return result
        if len(self.digits) > len(other):
            first = self.digits
            second = other
        elif len(self.digits) == len(other):
            for i in range(len(self.digits)-1, -1, -1):
                if self.digits[i] > other[i]:
                    first = self.digits
                    second = other
                elif self.digits[i] == other[i]:
                    pass
                elif self.digits[i] < other[i]:
                    first = other
                    second = self.digits
        else:
            first = other
            second = self.digits
        for i in range(0, len(second)):
            if first[i] >= second[i]:
                result.append(first[i] - second[i])
            else:
                result.append(first[i] + 10 - second[i])
                first[i+1] = first[i+1] - 1

        for i in range(len(result)-1, -1, -1):
            if result[i] == 0:
                result.pop(i)
            else:
                pass

        while len(result) < len(first):
            result.append(first[len(result)])

        if second == self.digits:
            result.insert(len(result) + 1, "-")

        return result[::-1]

    def __mul__(self, other):
        other = other[::-1]
        if len(self.digits) >= len(other):
            first = self.digits
            second = other
        else:
            first = other
            second = self.digits
        result = []
        for i in range(0, len(second)):
            for j in range(0, len(first)):
                if j < len(result) - 1:
                    result[j+1] = result[j+1] + second[i] * first[j]
                else:
                    result.append(second[i] * first[j])
        i = 0
        while len(result) > i:
            if result[i] >= 10:
                div = result[i] // 10
                mod = result[i] % 10
                result[i] = mod
                if len(result) - 1 > i:
                    result[i + 1] = result[i + 1] + div
                else:
                    result.append(div)
            i = i + 1
        return result[::-1]

