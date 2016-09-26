import numpy as np
import pandas as pd

class CHAIDRules(object):
    """
    A class that manages the rules of a tree

    Parameters
    ----------
    tree : CHAIDTree
        a tree object
    """
    def __init__(self, tree):
        self.rules(tree)
        self.node_definitions = {}

    def rules(self, tree):
        """
        Calculates the row criteria that give rise
        to a particular terminal node
        """
        rules = pd.DataFrame()
        unique_set = map(lambda x: set(x), tree.ind_v.T)
        for node in tree:
            if node.is_terminal:
                sliced_arr = tree.ind_v[node.indices].astype(float)
                # get the indexes that define that node
                import ipdb; ipdb.set_trace()
                # get just the indexes here
                parent_indexes = self.parent_indexes(tree, node)

                row_defined = sliced_arr.T[parent_indexes]
                row_unique = map(lambda x: set(x), row_defined)

                # slice those indexes out

                # fill in the other indexes with all values


                unique_set = np.vstack({ tuple(row) for row in sliced_arr })
                index = pd.MultiIndex.from_arrays(np.transpose(unique_set))
                if rules.empty:
                    rules = pd.DataFrame([[node.node_id, node.predict]] * len(index), index=index)
                else:
                    rules = rules.append(pd.DataFrame([[node.node_id, node.predict]] * len(index), index=index))
        rules.columns = ['node_id', 'prediction']
        import ipdb; ipdb.set_trace()
        return rules

    def parent_indexes(self, tree, node, store=None):
        if store is None: store = []
        parent = tree.get_node(node.parent)
        split = parent.split
        # store both the name of the column, and the index
        store.append((split.column_id, split.split_name))
        if parent.node_id != 0:
            self.parent_indexes(tree, parent, store)
        return store

    def rules_predictions(self):
        assert False
        return 1
