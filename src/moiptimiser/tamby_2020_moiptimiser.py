from moiptimiser.moiptimiser import *

class Tamby2020MOIPtimiser(MOIPtimiser):

    def __init__(self, model):
        super().__init__(model)

    def _update_search_region(self):
        pass

    def _find_non_dominated_objective_vectors(self):
        nds = set()
        return nds

    def find_non_dominated_objective_vectors(self):
        nds = self._find_non_dominated_objective_vectors()
        return nds
