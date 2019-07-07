import cma


es = cma.CMAEvolutionStrategy(12 * [0], 0.5)

while not es.stop():
    solutions = es.ask()
    func_vals = [cma.ff.rosen(x) for x in solutions]
    es.tell(solutions, func_vals)
    es.logger.add()  # write data to disc to be plotted
    es.disp()

es.result_pretty()
