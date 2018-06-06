a = b = c = None
        for n in nums:
            if n > a:
                a, b, c = n, a, b
            elif a > n > b:
                b, c = n, b
            elif b > n > c:
                c = n
        return c if c is not None else a