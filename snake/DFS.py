from Algorithm import Algorithm


class DFS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        if len(self.path) != 0:
            path = self.path.pop()
            if not self.inside_body(snake, path):
                return path
            else:
                self.path = []



        self.path = []
        self.explored_set = []

        self.frontier = []
        init, final = self.get_initstate_and_goalstate(snake)


        self.frontier.append(init)
        return self.recursive_DFS(snake,final,init)

    def recursive_DFS(self, snake, final, in_node):

        if in_node in self.explored_set:
            return None

        if in_node.equal(final):
            return self.get_path(in_node)

        self.explored_set.append(in_node)
        n = self.get_neighbors(in_node)
        for i in n:
            if not self.inside_body(snake,i) and not self.outside_boundary(i) and i not in self.explored_set:
                i.parent = in_node
                res = self.recursive_DFS(snake, i, final)
                if res is not None:
                    return res
        return None
