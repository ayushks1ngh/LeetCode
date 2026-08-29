class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # maintain two hash_map 
        # one to store all the elements present in the nums

        present = {}
        for i in range(len(nums)):
            if nums[i] not in present:
                present[nums[i]] = True
        
        # second hash_map checked is used to store the current consecutive subsequence

        max_len = 0
        

        # note that a element can be the first element of a consecutive subsequence only if element - 1 not exist in the hash_map

        for i in range(len(nums)):
            checked = {}
            curr_num = nums[i]
            if curr_num-1 not in present and present[curr_num] == True:
                # now find the length of subsequence
                ele = curr_num
                while True:
                    if ele in present and present[ele]==True:
                        if ele not in checked:
                            checked[ele] = True
                        present[ele] = False
                        ele+=1
                    else:
                        break
                
                max_len = max(len(checked),max_len)

                    
            else:
                continue
        
        return max_len
                