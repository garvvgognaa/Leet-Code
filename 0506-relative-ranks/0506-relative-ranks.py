class Solution(object):
    def findRelativeRanks(self, score):
        # Step 1: sort scores in descending order
        sorted_scores = sorted(score, reverse=True)
        
        # Step 2: create a dictionary for ranks
        rank_map = {}
        
        for i in range(len(sorted_scores)):
            if i == 0:
                rank_map[sorted_scores[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_scores[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_scores[i]] = "Bronze Medal"
            else:
                rank_map[sorted_scores[i]] = str(i + 1)
        
        # Step 3: build result using original order
        result = []
        for s in score:
            result.append(rank_map[s])
        
        return result