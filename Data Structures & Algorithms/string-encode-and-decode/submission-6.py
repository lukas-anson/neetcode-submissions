class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello","World"]
        # "5&Hello5&wWorld"
        # [5,5]
        # "HellowWorld"
        encoded_string = ""
        word_length = []

        for word in strs:
            word_length.append(len(word))
        
        for index, length in enumerate(word_length):
            encoded_string += (str(length) + "&" + strs[index])
        
        print(encoded_string)

        return encoded_string
        

    def decode(self, s: str) -> List[str]:

        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "&":
                j += 1
            length = int(s[i:j])

            i = j + 1
            j = i + length

            decoded_list.append(s[i:j])
            i = j
        return decoded_list
