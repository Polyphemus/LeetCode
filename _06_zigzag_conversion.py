#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
#A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str

        """
        if numRows == 1:
            return (s)

        # s iterator
        l = 0

        zigzag = []

        if len(s) % ((numRows - 1) * 2) == 0:
            a = 0
        elif len(s) % ((numRows - 1) * 2) > numRows:
            a = len(s) % ((numRows - 1) * 2) - numRows + 1
        elif len(s) % ((numRows - 1) * 2) <= numRows:
            a = 1

        print(a)

        for i in range(len(s) // ((numRows - 1) * 2) * (numRows - 1) + a):
            temp = []
            if i % (numRows - 1) == 0:
                for j in range(numRows):  # populate next numRows letters
                    if l < len(s):
                        temp.append(s[l])
                        l += 1
                    else:
                        temp.append("")
                zigzag.append(temp)

            else:
                for j in range(numRows):
                    if j == numRows - 1 - i % (numRows - 1):
                        if l < len(s):
                            temp.append(s[l])
                            l += 1
                        else:
                            temp.append("")
                    else:
                        temp.append("")

                zigzag.append(temp)

        ans = []
        for m in range(numRows):
            for n in range(len(zigzag)):
                ans.append(zigzag[n][m])

        return (''.join(ans))
