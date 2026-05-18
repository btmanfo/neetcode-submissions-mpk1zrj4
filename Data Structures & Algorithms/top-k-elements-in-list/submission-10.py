class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        frequencyTable = [[] for _ in range(len(nums))]
        for i,j in frequency.items():
            frequencyTable[j-1].append(i)
        print(frequencyTable)
        res= []
        for i in range(len(frequencyTable)-1, -1, -1):
            print(i)
            for j in frequencyTable[i]:
                res.append(j)
                print(j)
                if len(res) == k:
                    return res