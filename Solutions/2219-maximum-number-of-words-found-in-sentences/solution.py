class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        msf = 0

        for sentence in sentences:
            if len(sentence.split()) > msf:
                msf = len(sentence.split())
                
        return msf
