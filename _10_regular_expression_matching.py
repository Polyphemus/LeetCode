class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # this might be a great candidate for a recursive function.
        # it might make sense to modify p as we go, eg ab*a become aa if there are no b's in s
        if p.isalpha():
            if p == s:
                print('return True base')
                return True
            else:
                print('return False base')
                return False
        else:
            iS = 0  # string index
            iP = 0  # pattern index

            while iP < len(p) and iS < len(s):
                if p[iP].isalpha():
                    if p[iP] == s[iS]:
                        iS += 1
                        iP += 1
                    else:
                        try:  # * representing zero of preceding char
                            print(f'Current s char is {s[iS]}\nCurrent p char is {p[iP]}')
                            print('bad match but checking if next char is * to zero it out')
                            if p[iP + 1] == '*':
                                iP += 2
                            else:
                                print('return False 0')
                                return False
                        except IndexError:
                            print('theres no next char')
                            print('return False 3')
                            return False
                elif p[iP] == '.':
                    iS += 1
                    iP += 1
                else:  # if it's a star
                    print("it's a star")
                    if p[
                        iP - 1] != '.':  # if the previous character isn't a dot, skip in s until it doesn't match anymore.
                        while iS < len(s) and p[iP - 1] == s[iS]:
                            print(f'Skipping {s[iS]}')
                            iS += 1
                        iP += 1
                        while iP < len(p) and p[iP] == s[iS - 1]:
                            iP += 1
                    else:  # if previous char is a dot...
                        if iP == len(p) - 1:  # and nothing follows the *, it's a success
                            print('return True 0')
                            return True
                        # and letters follow the *...
                        print(f'iS = {iS}')
                        iP += 1
                        laterMatches = []
                        remainder = s[iS:]
                        for i in range(len(remainder)):
                            if remainder[i] == p[iP]:
                                laterMatches.append(i + iS)
                        print(laterMatches)
                        for match in laterMatches:
                            if self.isMatch(s[match:], p[iP:]):
                                print('return True 1')
                                return True
                        print('return false 1')
                        return False

        print(f"We've reached the end. iS = {iS}, iP = {iP}")
        if iP == len(p) and iS == len(s):  # if it's indexed through both without errors
            print('return True 2')
            return True
        else:
            print('return False 2')
            return False
