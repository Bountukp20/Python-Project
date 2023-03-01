class Solution:
    def solve(self, s):
        acronyms=s.split()
        string=""
        for word in acronyms:
            if word != "and":
                string += str(word[0])
        return string.upper()
ob = Solution()
print(ob.solve(input("please write a sentence: ")))