class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["hello", "world"]
        # 5#hello5#world
        ans = ''
        for word in strs:
            ans = ans + (str(len(word)) + "#" + word)
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        if s == '':
            return ans
        i = 0
        # 5#Hello5#World
        while i < len(s):
            j = i
            while s[j] != "#":
                j = j + 1
            print(''.join(s[i:j]))
            len_str = int(s[i:j])
            print(len_str)
            i = j + 1 # To account for extra #
            j = i + len_str
            word = s[i:j]
            print(word)
            ans.append(word)
            i = j
        return ans


