class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        #return word.islower() or word.isupper() or word.istitle()
        return word.lower() == word or word.upper() == word or word.lower().capitalize() == word
