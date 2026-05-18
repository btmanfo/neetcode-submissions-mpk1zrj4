class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        #None veux dire quon est pas encore passer la pour le calculer
        dp = [None] *n
        dp[n-1] = True

        def dfs(i):
            if dp[i] is not None:
                return dp[i]
            # Car on supose que pour linstant on ne sais pas si on peut aller jusqua la
            dp[i] = False
            #Toujours verifier pour la premier iteration
            for j in range(i+minJump, min(n, i+maxJump+1)):
                #Au debut on va voyager jusqua la fin et on a mis que dp[n-1] = True. Donc ca va fonctionner
                if s[j] == '0' and dfs(j):
                    dp[i] = True
                    return True
            return dp[i]
        if s[-1] == '1':
            return False
        return dfs(0)