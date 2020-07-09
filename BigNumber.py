class BigNumber:
    def __init__(self, value):
        self.a = value

    def __add__(self, another_value):
        if len(self.a[::-1]) >= len(another_value[::-1]):
            first_number = self.a[::-1]
            second_number = another_value[::-1]
        else:
            first_number = another_value[::-1]
            second_number = self.a[::-1]
        i = 0
        z = []
        while True:
            if not len(second_number) <= i:
                c = first_number[i] + second_number[i] % 10
                if c >= 10:
                    k = c // 10
                    c = c % 10
                    z.append(c)
                    if first_number[i + 1]:
                        first_number[i + 1] = first_number[i + 1] + k
                    else:
                        first_number.append(k)
                else:
                    z.append(c)
                i = i + 1
            else:
                while len(first_number) >= i+1:
                    z.append(first_number[i])
                    i = i + 1
                break
        j = 0
        while len(z) > j:
            if z[j] >= 10:
                v = z[j] // 10
                n = z[j] % 10
                z[j] = n
                if z[j + 1]:
                    z[j + 1] = z[j + 1] + v
                else:
                    z.append(v)
            j = j + 1
        return z[::-1]

    def __sub__(self, another_value):
        first_value = int("".join(map(str, self.a)))
        second_value = int("".join(map(str, another_value)))
        if first_value >= second_value:
            num = first_value - second_value
            z = list(map(int, str(num)))
        else:
            num = second_value - first_value
            z = list(map(int, str(num)))
            z.insert(0, "-")
        return z

    def __mul__(self, another_value):
        first_value = int("".join(map(str, self.a)))
        second_value = int("".join(map(str, another_value)))
        z = list(map(int, str(first_value * second_value)))
        return z

    def __truediv__(self, another_value):
        first_value = int("".join(map(str, self.a)))
        second_value = int("".join(map(str, another_value)))
        num = str(first_value / second_value)
        z = []
        for i in range(0, len(num)):
            if num[i] == ".":
                z.append(".")
            else:
                z.append(int(num[i]))
        return z


a = BigNumber([1, 8, 3, 1])

print(a+[4, 9, 8, 2])

a = BigNumber([9, 0])

print(a - [1, 2, 3])


a = BigNumber([9, 0])

print(a * [1, 2, 3])


a = BigNumber([9, 0])

print(a / [3, 0])
