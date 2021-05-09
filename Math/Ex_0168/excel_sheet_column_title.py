class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result, col = "", columnNumber

        while int(col) != 0:
            result += chr(int((col - 1) % 26) + 65)
            col = (col - 1) / 26

        return result[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(523482374))