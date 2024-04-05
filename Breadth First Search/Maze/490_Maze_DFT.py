from collections import defaultdict
class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        stack = []
        stack.append(start)
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = defaultdict()
        visited[str(start)] = True
        while stack:
            pos = stack.pop()
            row = pos[0]
            col = pos[1]
            for direction in dirs:
                new_row = row
                new_col = col
                while new_row + direction[0] >= 0 and new_col + direction[1] >= 0 and new_row + direction[0] < len(maze) and new_col + direction[1] < len(maze[0]) and maze[new_row + direction[0]][new_col + direction[1]] != 1:
                    new_row = new_row + direction[0]
                    new_col = new_col + direction[1]

                new_pos = [new_row,new_col]
                if new_pos[0] == destination[0] and new_pos[1] == destination[1]:
                    return True
                if str(new_pos) not in visited:
                    visited[str([new_row, new_col])] = True
                    stack.append(new_pos)
        return False
