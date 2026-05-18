class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rvote = 0
        Dvote = 0
        n= len(senate)
        for vote in senate:
            if vote == "R":
                Rvote +=1
            if vote == "D":
                Dvote +=1
        dp = [True] * n
        while Rvote> 0 and Dvote>0:
            for i in range(len(senate)):
                for j in range(len(senate)):
                    if senate[i] != senate[j] and dp[j] == True:
                        dp[j] == False
                        if senate[j] == 'R':
                            Rvote -=1
                        if senate[j] == 'D':
                            Dvote -=1
                        
                        if Rvote == 0:
                            return "Dire"
                        if Dvote == 0:
                            return 'Radiant'
