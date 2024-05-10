def make_change(total):
    coin_value = [1, 5, 10, 25, 100]
    
    def find_combinations(current_sum, index, current_combination, all_combinations):
        if current_sum == total:
            all_combinations.append(current_combination.copy())
            return
        if current_sum > total or index >= len(coin_value):
            return
        
        # Include current coin and recurse
        current_combination.append(coin_value[index])
        find_combinations(current_sum + coin_value[index], index, current_combination, all_combinations)
        
        # Exclude current coin and recurse
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

samplekv = KVTree("us", 4.6)
pa = KVTree("pa", 1.9)
samplekv.add_child(pa)
pa.add_child(KVTree("Pittsburgh", 0.3))
pa.add_child(KVTree("Philadelphia", 1.6))
il = KVTree("il", 2.7)
samplekv.add_child(il)
il.add_child(KVTree("Chicago", 2.7)
             

def treemap(func, node):
    new_key, new_value = func(node.key, node.value)
    node.key = new_key
    node.value = new_value
    
    for child in node.children():
        treemap(func, child)
        
    


class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (varibale is None and threhold is None and lessequal is None and greater is None and outcome is not None) or \
           (variable is not None and threhold is not None lessequal is not None and greater is not None and outcome is None):
            self.variable = variable
            self.threhold = threhold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError

    def



    def find_outcome(self, tup):
        if self.outcome is not None:
            return self.outcome
        elif tup[self.variable] <= self.threhold:
            return self.lessequal.find_outcome(tup)
        else:
            return self.greater.find_outcome(tup)