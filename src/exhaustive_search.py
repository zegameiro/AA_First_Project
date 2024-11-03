from graph import Graph
from utils import get_all_cut_combinations, calculate_cost

class ExhaustiveSearch:

    def __init__(self, nodes, edges, counter) -> None:
        self.nodes = nodes
        self.edges = edges
        self.graph = Graph(nodes=nodes, edges=edges)

        # Draw the graph
        self.graph.draw_graph(counter=counter)

        # Build the adjency matrix
        self.adjency_matrix = self.graph.build_adjency_matrix()

        # All possible combinations for a cut
        self.all_combinations = None
    
    def solve_problem(self):
        """
            Solve a problem
            - combination -> a list of nodes that are cut([1, 2, 3])
        """

        min_cost = 400
        best_sub_set_a = ""
        best_sub_set_b = ""
        counter = 0
        n_solutions = 0

        all_nodes_list = [chr(i) for i in range(97, 97 +self.graph.nodes_number)]

        self.all_combinations = get_all_cut_combinations(
            nodes=all_nodes_list
        )

        for sub_set_a in self.all_combinations:
            counter += 1
            sub_set_b = [chr(j) for j in range(97, 97 + self.graph.nodes_number) if chr(j) not in sub_set_a]
            x = calculate_cost(conj_a=sub_set_a, conj_b=sub_set_b, connections=self.graph.edge_positions)

            if x < min_cost:
                min_cost = x
                best_sub_set_a = sub_set_a
                best_sub_set_b = sub_set_b
            elif x == min_cost:
                n_solutions += 1

        return min_cost, best_sub_set_a, best_sub_set_b, counter, n_solutions