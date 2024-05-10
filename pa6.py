def make_change(total):
    coin_value = [1, 5, 10, 25, 100]
    
    def find_combinations(current_sum, index, current_combination, all_combinations):
        if current_sum == total:
            all_combinations.append(current_combination.copy())
            return
        if current_sum > total or index >= len(coin_value):
            return
        
        current_combination.append(coin_value[index])
        find_combinations(current_sum + coin_value[index], index, current_combination, all_combinations)
        
        current_combination.pop()
        find_combinations(current_sum, index + 1, current_combination, all_combinations)
    
    all_combinations = []
    find_combinations(0, 0, [], all_combinations)
    return all_combinations
        

def dic_filter(check_function, dict):
    rv_dict = {}
    for key, value in dict.items():
        if check_function(key, value):
            rv_dict[key] = value
    
    return rv_dict

def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"


class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
             
def treemap(func, node):
    new_key, new_value = func(node.key, node.value)
    node.key = new_key
    node.value = new_value
    
    for child in node.children:
        treemap(func, child)
        
    

class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is None and threshold is None and lessequal is None and greater is None and outcome is not None) or \
           (variable is not None and threshold is not None lessequal is not None and greater is not None and outcome is None):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError

    def tuple_atleast(self):
        num = set()
        def collect_indices(self, node):
            if node.variable is not None:
                num.add(node.variable)
            if node.lessequal is not None:
                self.collect_indices(node.lessequal)
            if node.greater is not None:
                self.collect_indices(node.greater)

        collect_indices(self)
        return max(num) + 1 if num else 1


    def find_outcome(self, tup):
        if self.outcome is not None:
            return self.outcome
        elif tup[self.variable] <= self.threhold:
            return self.lessequal.find_outcome(tup)
        else:
            return self.greater.find_outcome(tup)

    def no_repeats(self):
        def helper(node, seen):
            if node.variable is None:  
                return True
            if node.variable in seen:
                return False
      
            seen.add(node.variable)
       
            lessequal_result = helper(node.lessequal, seen.copy()) if node.lessequal else True
            greater_result = helper(node.greater, seen.copy()) if node.greater else True
            return lessequal_result and greater_result
        

        return helper(self, set())