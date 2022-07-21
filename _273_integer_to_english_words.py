# Convert a non-negative integer num to its English words representation.

class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        else:
            ones = ['', ' One', ' Two', ' Three', ' Four', ' Five', ' Six', ' Seven', ' Eight', ' Nine']
            teens = [' Ten', ' Eleven', ' Twelve', ' Thirteen', ' Fourteen', ' Fifteen', ' Sixteen', ' Seventeen', ' Eighteen', ' Nineteen']
            tens = ['', '', ' Twenty', ' Thirty', ' Forty', ' Fifty', ' Sixty', ' Seventy', ' Eighty', ' Ninety']
            illions = ['', ' Thousand', ' Million', ' Billion', ' Trillion']
            digits = list(str(num))

    ## prepends 0's until divisible by 3
            if len(digits) % 3 != 0:
                digits = (3 - (len(digits) % 3))*['0'] + digits

    ## populates list of 3-digit lists
            chunks = []
            for i in range(len(digits)//3):
                temp = []
                for j in range(3):
                 #   print(j)
                    temp = [digits[len(digits) - 3*i - j - 1]] + temp
                chunks = [temp] + chunks

    # translates 3 digit chunks to words, adds thousand, million, etc if chunk isn't ['0', '0', '0']
            ans = ''
            for k in range(len(chunks)):
                if chunks[k][0] != '0':
                    ans += ones[int(chunks[k][0])]
                    ans += ' Hundred'
                if chunks[k][1] == '1':
                    ans += teens[int(chunks[k][2])]
                else:
                    ans += tens[int(chunks[k][1])]
                    ans += ones[int(chunks[k][2])]
                    print(ans)

                if chunks[k] != ['0','0','0']:
                    ans += illions[len(chunks) - k - 1]
    #returns answer without leading space
            return(ans[1:])
