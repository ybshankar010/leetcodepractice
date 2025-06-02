class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        # print(words)
        i, j = 0, len(words)-1

        while i < j:
            temp = words[i]
            words[i] = words[j]
            words[j] = temp

            i += 1
            j -= 1

        return " ".join(words)


if __name__ == "__main__":
    solution = Solution()
    sentence = "a good   example"
    print(solution.reverseWords(sentence))