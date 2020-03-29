class Maze:
	
	def __init__(self):

		self.solution = dict()	
		self.frontier_dfs = list()
		self.start = list()
		self.end = list()
		self.visited = list()
		self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]	# Down, Right, Up, Left

	def create_maze(self):
		
		maze = []
		maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
		maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
		maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
		maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
		maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
		maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
		maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
		maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
		maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

		return maze

	def findStart(self, maze): 

		for i, row in enumerate(maze):
			for j, col in enumerate(row):
				if maze[i][j] == 'O':
					self.start = [i,j]
					print(self.start)
					return 1

	def findEnd(self, maze):

		for i, row in enumerate(maze):
			for j, col in enumerate(row):
				if maze[i][j] == 'X':
					self.end = [i, j]
					print(self.end)
					return 1

	def exploreNeighbours(self, pos, maze):

		for i in self.directions:
			next_mov = list(map(sum, zip(pos, i)))
			x = next_mov[0]
			y = next_mov[1]

			if x < 0 or y < 0:
				continue
			if x >= len(maze[0]) or y >= len(maze):
				continue
			if next_mov in self.visited:
				continue
			if maze[x][y] == '#':
				continue

			self.visited.append(next_mov)
			self.frontier_dfs.append(next_mov)
			self.solution[x, y] = pos[0], pos[1] 


	def solve(self):
		maze = self.create_maze()

		self.findStart(maze)
		self.findEnd(maze)
		self.frontier_dfs.append(self.start)

		while len(self.frontier_dfs) > 0:

			pos = self.frontier_dfs.pop()
			self.exploreNeighbours(pos, maze)

		self.backRoute(maze)
		self.printMaze(maze)

	def backRoute(self, maze):
		
		x, y = self.end[0], self.end[1]
		while (x, y) != (self.start[0], self.start[1]):
			maze[x][y] = '+'
			x, y = self.solution[x, y]

	def printMaze(self, maze):

		for i, row in enumerate(maze):
			for j, col in enumerate(row):
				print(maze[i][j], end = "")
			print()	  

mazesolver = Maze()
mazesolver.solve()