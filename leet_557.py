class Solution:
    def reverseWords(self, s: str) -> str:
        
        str_list = s.split(" ")
        
        for i in range(0,len(str_list)):
            tryreverse = str_list[i]
            reverseChar = tryreverse[::-1]
            str_list[i] = reverseChar
            
        result = " ".join(str_list)
        return result
