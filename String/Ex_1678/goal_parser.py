class Solution:
    def interpret(self, command: str) -> str:
        result, i = [], 0
        while i < len(command):
            if command[i] == 'G':
                result += ["G"]
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                result += ["o"]
                i += 2
            else:
                result += ["al"]
                i += 4
        return "".join(result)

if __name__ == "__main__":
    s = Solution()
    print(s.interpret("G()()()()(al)"))
    print(s.interpret("(al)G(al)()()G"))