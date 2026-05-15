class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        lower_word = s.lower()
        for letter in lower_word:
            if not letter.isalnum():
                continue
            word.append(letter)
        print(word) 

        for i in range(len(word)//2):
            p1 = word[i]
            p2 = word[len(word)- 1 - i]
            if p1 != p2:
                return False
        return True          


          
