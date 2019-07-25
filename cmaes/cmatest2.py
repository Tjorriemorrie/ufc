import cma as cma
import numpy as np

es = cma.CMAEvolutionStrategy(10 * [0.2], 0.5, {'bounds': [0, np.inf]})

while not es.stop():
    fit, X = [], []
    while len(X) < es.popsize:
        curr_fit = None
        while curr_fit in (None, np.NaN):
            x = es.ask(1)[0]
            curr_fit = cma.ff.somenan(x, cma.ff.elli)  # might return np.NaN
        X.append(x)
        fit.append(curr_fit)
    es.tell(X, fit)
    es.logger.add()
    es.disp()

a = 1
