class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): 
            return False

        left_pointer = 0
        right_pointer = len(s1)
        s1_dic = {}
        window_dic = {}

        for letter in s1:
            s1_dic[letter] = 1 + s1_dic.get(letter, 0)

        for i in range(len(s1) - 1):
            window_dic[s2[i]] = 1 + window_dic.get(s2[i], 0)

        for index in range(right_pointer - 1, len(s2)):
            window_dic[s2[index]] = 1 + window_dic.get(s2[index], 0)
            if s1_dic == window_dic:
                return True
            else:
                window_dic[s2[left_pointer]] -= 1
                if window_dic[s2[left_pointer]] == 0:
                    del window_dic[s2[left_pointer]]
                left_pointer += 1
        return False



        