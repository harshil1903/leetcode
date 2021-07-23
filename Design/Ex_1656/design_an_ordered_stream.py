
# 1656. Design an Ordered Stream
#
# Source : https://leetcode.com/problems/design-an-ordered-stream/
#
# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1 and n and value is a string. No two pairs have
# the same id.
#
# Design a stream that returns the values in increasing order of their IDs by returning a chunk (list) of values after each insertion. The concatenation of all
# the chunks should result in a list of the sorted values.
#
# Implement the OrderedStream class:
#
# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream, then returns the largest possible chunk of currently inserted values
# that appear next in the order.



from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.stream = [""] * n
        self.ptr = 0
        self.max = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value

        if self.stream[self.ptr]:
            st = []

            while self.stream[self.ptr]:
                st.append(self.stream[self.ptr])
                self.ptr += 1
                if self.ptr >= self.max:
                    break

            return st

        return []

    def insert1(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value
        result = []
        key = self.ptr

        if key != idKey:
            return result
        while key < len(self.stream) and self.stream[key] is not None:
            result.append(self.stream[key])
            key += 1

        self.ptr = key
        return result

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

# Input :
# ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

# Output :
# [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]