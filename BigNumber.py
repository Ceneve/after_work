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


a = BigNumber([1, 8, 3, 1])

print(a+[4, 9, 8, 2])
