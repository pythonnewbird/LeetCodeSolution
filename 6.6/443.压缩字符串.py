class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        last, n, y = chars[0], 1, 0
        for x in range(1, len(chars)):
            c = chars[x]
            if c == last: n += 1
            else:
                
                for ch in last + str(n > 1 and n or ''):
                    chars[y] = ch
                    y += 1
                last, n = c, 1
        for ch in last + str(n > 1 and n or ''):
            chars[y] = ch
            y += 1
        while len(chars) > y: chars.pop()
        return y