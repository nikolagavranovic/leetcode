from solution import Solution

class Test(object):
    def compare(self, input, expected):
        s = Solution()
        output = s.longestPalindrome(input)
        if output == expected:
            print(f"Input {input}")
            print(f"Expected {expected}")
            print(f"Test passed!")
            print('-'*20)
        else:
            print(f"Input {input}")
            print(f"Expected {expected}")
            print(f"Test failed!")
            print('-'*20)



if __name__ == '__main__':

    t = Test()
    test = ["lc","cl","gg"]
    expected = 6
    t.compare(test, expected)
    test = ["ab","ty","yt","lc","cl","ab"]
    expected = 8
    t.compare(test, expected)
    test = ["cc","ll","xx"]
    expected = 2
    t.compare(test, expected)
    test = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]
    expected = 22
    t.compare(test, expected)
    test = ["em","pe","mp","ee","pp","me","ep","em","em","me"]
    expected = 14
    t.compare(test, expected)
   
    