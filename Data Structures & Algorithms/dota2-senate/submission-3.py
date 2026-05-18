class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        # on ne peux pas mettre n = len(senate) car il va rester figer a la valeur initial, mais la taille va changer
        while True:
            i = 0
            while i<len(s):
                if 'R' not in s:
                    return "Dire"
                if 'D' not in s:
                    return "Radiant"
                if s[i] == 'R':
                    j = (i+1) % len(s)
                    while s[j] == "R":
                        j = (j+1) % len(s)
                    s.pop(j)
                    #quand on va pop la valeur j notre i va etre out of range (des fois) so on doit le decaler sa valeur
                    if j < i:
                        i-=1
                else:
                    j = (i+1) % len(s)
                    while s[j] == "D":
                        j = (j+1) % len(s)
                    s.pop(j)
                    if j < i:
                        i-=1
                i+=1