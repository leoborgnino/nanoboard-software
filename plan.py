class plan:
			
	self.steering_noise    = 0.1
	self.distance_noise    = 0.03
	self.measurement_noise = 0.3

	def __init__(self, grid, init,goal, cost = 1):
	        self.cost = cost
	        self.grid = grid
	        self.init = init
	        self.goal = goal
	        self.make_heuristic(grid, goal, self.cost)
	        self.path = []
	        self.spath = []
		    self.action = []

    # --------
    #
    # Crea la funcion heuristica para el grid
       
	def make_heuristic(self, grid, goal, cost):
		self.heuristic = [[0 for row in range(len(grid[0]))] 
			for col in range(len(grid))]
	        for i in range(len(self.grid)):    
	            for j in range(len(self.grid[0])):
	                self.heuristic[i][j] = abs(i - self.goal[0]) + \
	                    abs(j - self.goal[1])
	


    # ------------------------------------------------
    # 
    # A* para buscar el camino al objetivo
    #
    #

	def astar(self):


	        if self.heuristic == []:
	            raise ValueError, "Heuristica debe estar definida para ejecutar A*"

        # Movimientos del robot
	        delta = [[-1,  0], # go up
	                 [ 0,  -1], # go left
	                 [ 1,  0], # go down
	                 [ 0,  1]] # do right


        # Elementos de la lista open son del tipo: [f, g, h, x, y]

	        closed = [[0 for row in range(len(self.grid[0]))] 
	                  for col in range(len(self.grid))]
	        self.action = [[0 for row in range(len(self.grid[0]))] 
	                  for col in range(len(self.grid))]

	        closed[self.init[0]][self.init[1]] = 1


	        x = self.init[0]
	        y = self.init[1]
	        h = self.heuristic[x][y]
	        g = 0
	        f = g + h

	        open = [[f, g, h, x, y]]

	        found  = False # flag que es verdadera cuando la busqueda se completo
	        resign = False # flag que es verdadera cuando no se puede expandir mas
	        count  = 0
	
	
	        while not found and not resign:
	
	            # Chequeamos si todavia hay elementos en la lista open
	            if len(open) == 0:
	                resign = True
	                print '###### Busqueda terminada pero fallida'
	                
	            else:
	                # removemos un nodo de la lista
	                open.sort()
	                open.reverse()
	                next = open.pop()
	                x = next[3]
	                y = next[4]
	                g = next[1]
	
	            # chequeamos si encontramos el objetivo
	
	            if x == goal[0] and y == goal[1]:
	                found = True
	                # print '###### A* Busqueda Realizada'
	
	            else:
	                # Expandimos el elemento seleccionado y anadimos a la lista
	                for i in range(len(delta)):
	                    x2 = x + delta[i][0]
	                    y2 = y + delta[i][1]
	                    if x2 >= 0 and x2 < len(self.grid) and y2 >= 0 \
	                            and y2 < len(self.grid[0]):
	                        if closed[x2][y2] == 0 and self.grid[x2][y2] == 0:
	                            g2 = g + self.cost
	                            h2 = self.heuristic[x2][y2]
	                            f2 = g2 + h2
	                            open.append([f2, g2, h2, x2, y2])
	                            closed[x2][y2] = 1
	                            self.action[x2][y2] = i
	
	            count += 1
	
	        # extraemos el camino
	
		#for i in self.action:
		#	print i
	
	        invpath = []
	        x = self.goal[0]
	        y = self.goal[1]
	        invpath.append([x, y])
	        while x != self.init[0] or y != self.init[1]:
	            x2 = x - delta[self.action[x][y]][0]
	            y2 = y - delta[self.action[x][y]][1]
	            x = x2
	            y = y2
	            invpath.append([x, y])
	
	        self.path = []
	        for i in range(len(invpath)):
	            self.path.append(invpath[len(invpath) - 1 - i])
		    #print self.path[i]
