from collections import deque, defaultdict

class Solution:
    def hasPath(self, maze: list[list[int]], start: list[int], destination: list[int]) -> bool:
        queue = deque()
        queue.append(tuple(start))  
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = defaultdict(bool)  

        while queue:
            row, col = queue.popleft()
            for direction in dirs:
                new_row, new_col = row, col
                while 0 <= new_row + direction[0] < len(maze) and 0 <= new_col + direction[1] < len(maze[0]) and maze[new_row + direction[0]][new_col + direction[1]] != 1:
                    new_row += direction[0]
                    new_col += direction[1]

                new_pos = (new_row, new_col)
                if new_pos == tuple(destination):
                    return True
                if not visited[new_pos]:
                    visited[new_pos] = True
                    queue.append(new_pos)

        return False
