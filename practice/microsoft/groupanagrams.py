class Solution(object):

    def groupAnagrams(self, strs):
        grouped_anagrams_dict = {}
        for curr in strs:
            sortedString = str(sorted(curr))
            # print(sortedString,"<>",grouped_anagrams_dict.get(sortedString,[]),"<>",curr)
            grouped_list = grouped_anagrams_dict.get(sortedString,[])
            grouped_list.append(curr)
            grouped_anagrams_dict[sortedString] = grouped_list

        return [value for _,value in grouped_anagrams_dict.items()]

if __name__ == "__main__":
    import time
    start = time.time()
    solution = Solution()
    strs = ["ddddddddddg","dgggggggggg"]
    print(solution.groupAnagrams(strs))
    end = time.time()
    print("time taken ",(end-start))