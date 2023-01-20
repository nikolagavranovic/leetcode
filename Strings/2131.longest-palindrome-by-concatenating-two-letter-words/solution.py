# You are given an array of strings words. Each element of words consists of two lowercase English letters.

# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

# A palindrome is a string that reads the same forward and backward.

 

# Example 1:

# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
# Note that "clgglc" is another longest palindrome that can be created.
# Example 2:

# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
# Example 3:

# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is "xx".

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        total_counter = 0
        # count all words
        words_counter = {}
        unique_words = list(set(words))
        for w in unique_words:
            words_counter[w] = words.count(w)
        
        # for each word find if there is any other coresponding reversed,
        # so that they can create a palindrome
        middle_palindrome_inserted = False
        for i, w1 in enumerate(unique_words):
            for j in range(i + 1, len(unique_words)):
                # if one string is reversed to the other, that means that they can make palindrom
                if w1 == unique_words[j][::-1]:
                    total_counter += min(words_counter[w1], words_counter[unique_words[j]]) * 2 * 2
                    
        
        # check for palindromes
        for i, w1 in enumerate(unique_words):
            if self.isPalindrome(w1):
                # if count od palindromes is odd number
                if words_counter[w1] % 2 != 0:
                    # only first time can be inserted (in the middle) odd palindrome
                    if not middle_palindrome_inserted:
                        total_counter += words_counter[w1]*2
                        middle_palindrome_inserted = True
                    else:
                        total_counter += (words_counter[w1] - 1)*2
                    # if count od palindromes is even number the can form final palindrom
                else:
                    total_counter += words_counter[w1]*2 

        return total_counter

    def isPalindrome(self, word):
        i = 0
        j = len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True
     
