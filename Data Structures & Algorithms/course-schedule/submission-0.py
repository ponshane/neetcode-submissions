class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # build a prerequisite map for every course (i.e., i)
        preMap = {i: [] for i in range(numCourses)}
        for pair in prerequisites:
            preMap[pair[0]].append(pair[1])
        
        visitedSet = set()

        def dfs(course):
            if course in visitedSet:
                return False
            
            if len(preMap[course]) == 0:
                return True
            
            visitedSet.add(course)

            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            # reuse for the other dfs call
            visitedSet.remove(course)
            # we know this course is clear and is finishable
            preMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            