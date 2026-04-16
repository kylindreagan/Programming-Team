from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        # Initialize queue with courses that have no prerequisites
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # Process courses in topological order
        taken = 0
        while q:
            course = q.popleft()
            taken += 1
            # Update dependencies for courses that depend on current course
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return taken == numCourses