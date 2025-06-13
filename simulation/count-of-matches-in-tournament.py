class Solution:
    def numberOfMatches(self, n: int) -> int:
               # Return the total number of matches that will be played.
        # Since each match eliminates one team, and we start with n teams,
        # the number of matches required to get to 1 winner is n - 1.
        
        return n-1
