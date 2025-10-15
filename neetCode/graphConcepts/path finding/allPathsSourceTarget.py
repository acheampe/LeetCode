import unittest

class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        # we use backtracking approach here because we have to explore all paths
        # worst case TC is if each node connects to last node via its individual path O(2^n * n)
        # worst SC O(h)
        
        # length of graph
        m = len(graph) 
        # initiate resultList: list[list[int]
        resultList: list[list[int]] = []
        
        def backtracking(currNode, currList):
            
            updatedCurrList: list[int] = currList + [currNode]
            
            # base case
            if updatedCurrList[-1] == m - 1:
                resultList.append(updatedCurrList)
                return # to back track
            
            # currList.append(currNode)
            for nextNode in graph[currNode]:
                backtracking(nextNode, updatedCurrList)
            
            # currList.pop()
        
        backtracking(0, [])
        
        return resultList
        
        #backtracking dfs with node and currlist as inputs

            # append currlist to node
            
            # base case is if node == m - 1
                # append currlist to resultList
                # return
            
            # for nextNode in graph[node]:
            
                # backtracking with nextNode and currlist
        
    
        # initiate call to backtracking with node 0 as input
        # 
        # return resultList
    
class TestAllPathsSourceTarget(unittest.TestCase):
    def test_example_1(self):
        graph = [[1,2],[3],[3],[]]
        expected = [[0,1,3],[0,2,3]]
        result = Solution().allPathsSourceTarget(graph)
        self.assertCountEqual(result, expected)

    # def test_example_2(self):
    #     graph = [[4,3,1],[3,2,4],[3],[4],[]]
    #     expected = [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    #     result = Solution().allPathsSourceTarget(graph)
    #     self.assertCountEqual(result, expected)

    # def test_linear_path(self):
    #     graph = [[1],[2],[3],[]]
    #     expected = [[0,1,2,3]]
    #     result = Solution().allPathsSourceTarget(graph)
    #     self.assertEqual(result, expected)

    # def test_two_paths_same_length(self):
    #     graph = [[1,2],[3],[3],[]]
    #     expected = [[0,1,3],[0,2,3]]
    #     result = Solution().allPathsSourceTarget(graph)
    #     self.assertCountEqual(result, expected)

    # def test_large_branch(self):
    #     graph = [[1,2,3],[4],[4],[4],[]]
    #     expected = [
    #         [0,1,4],
    #         [0,2,4],
    #         [0,3,4]
    #     ]
    #     result = Solution().allPathsSourceTarget(graph)
    #     self.assertCountEqual(result, expected)

if __name__ == "__main__":
    unittest.main()