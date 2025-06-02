class Solution(object):
    def __init__(self):
        self.min_val = -2**31
        self.max_val = (2**31)-1
        self.capped_max = self.max_val//10

    def myAtoi(self, s):
        final_num = 0
        isneg, encountered_digit,encountered_sign,overflow = False, False, False, False

        for idx in range(len(s)):
            if s[idx].isalpha() or s[idx] =='.':
                break

            if (encountered_digit or encountered_sign) and s[idx] == ' ' :
                break

            if overflow:
                break
            
            if s[idx] == '-' or s[idx] == '+':
                if encountered_digit or encountered_sign:
                    break

                if s[idx] == '-':
                    encountered_sign = True
                    isneg = True
                
                if s[idx] == '+':
                    encountered_sign = True
                    isneg = False

            if s[idx].isdigit():
                encountered_digit = True
                curr_digit = int(s[idx])
                if final_num == self.capped_max:
                    if isneg and curr_digit > 8:
                        curr_digit = 8
                    elif not isneg and curr_digit > 7:
                        curr_digit = 7
                elif final_num > self.capped_max:
                    return self.min_val if isneg else self.max_val
                final_num = final_num * 10 + curr_digit 
        
        if isneg: final_num *= -1
        
        return final_num

if __name__ == "__main__":
    solution = Solution()
    strs = ["1337wc09","      -     1a42","0-1","-042","   +0 123","-2147483647","-2147483648","2147483648","-91283472332","91283472332","21474836460"]
    # strs = ["-21474836479"]
    for s in strs:
        print(s,"<<>>",solution.myAtoi(s))