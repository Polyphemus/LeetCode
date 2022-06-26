class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if divisor == 1:
            ans = dividend
        elif divisor == -1:
            ans = 0 - dividend

        else:
            # account for negatives
            if divisor > 0 and dividend < 0:
                Negs = True
                dividend = 0 - dividend
            elif divisor < 0 and dividend > 0:
                Negs = True
                divisor = 0 - divisor
            elif divisor < 0 and dividend < 0:
                Negs = False
                divisor = 0 - divisor
                dividend = 0 - dividend
            else:
                Negs = False

            strDiv = str(dividend)
            strProd = ''
            remainder = ''
            for char in strDiv:
                j = 0
                prod = 0
                while prod <= int(remainder + char):
                    prod += divisor
                    j += 1
                strProd += str(j - 1)
                remainder = str(int(remainder + char) - (prod - divisor))

            if Negs:
                ans = 0 - int(strProd)
            else:
                ans = int(strProd)

        # to account for very large numbers
        if ans < -2 ** 31:
            return -2 ** 31
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return ans