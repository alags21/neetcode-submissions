class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for i in range(numCourses)]
        for e in prerequisites:
            # index = course number
            # elements = all prereqs
            
            courses[e[1]].append(e[0])

        explored = set()
        currpath = set()
        def explore(i):
            # if i is in currpath, cycle found - return False
            if i in currpath:
                return False
            
            # if i already explored, return true
            if i in explored:
                return True
            
            # mark it as explored
            # if not, add it to the current path
            currpath.add(i)
            for pre in courses[i]:
                if not explore(pre):
                    return False
            # course i path has been fully explored
            # remove from currpath
            explored.add(i)

            currpath.remove(i)
            return True
        # now i have a list of the prereqs for each course, where the course number corresponds to its index i

        for i in range(len(courses)):
            if i in explored:
                continue
            else:
                for j in courses[i]:
                    if not explore(j):
                        return False
            
        return True
