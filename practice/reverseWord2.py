class Solution(object):
    def reverseWords(self, s):
                
        i, j = 0, len(s)-1

        while i <= j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

            i += 1
            j -= 1

        start = 0
        while start < len(s)-1:
            end = start
            while end < len(s) and s[end] != " ":
                end += 1
            
            i, j = start, end-1
            while i<=j :
                temp = s[i]
                s[i] = s[j]
                s[j] = temp

                i += 1
                j -=1
            
            start = end+1

        return s
        
if __name__ == "__main__":
    solution = Solution()
    str_to_reverse =["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    print(solution.reverseWords(s=str_to_reverse))