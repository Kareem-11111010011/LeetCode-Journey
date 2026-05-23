class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        values = [val for val in range(1, 27)]
        letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        alphabet = dict(zip(letters, values))
        for char in columnTitle:
            result = result*26 + alphabet[char]
        return result
                
            
                
            
                
            
