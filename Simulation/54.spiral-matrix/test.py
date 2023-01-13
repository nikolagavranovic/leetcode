from solution import Solution

s = Solution()
testCases = [[[1,2,3],[4,5,6],[7,8,9]], [[1,2,3,4],[5,6,7,8],[9,10,11,12]]]
expectedOutputs = [[1,2,3,6,9,8,7,4,5], [1,2,3,4,8,12,11,10,9,5,6,7]]
n = len(testCases)
for i, test in enumerate(testCases):
    expectedOutput = expectedOutputs[i]
    output = s.spiralOrder(test)
    print(f"test: {test}")
    print(f"expected: {expectedOutput}")
    print(f"output: {output}")
    if output == expectedOutput:
        print("test passed")
    else:
        print("test failed")
        
    if i != n:
        print("------------------------------------------")