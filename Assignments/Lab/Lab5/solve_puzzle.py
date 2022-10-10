def solve_puzzle(lst, idx=0, visited = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    # 1) Base case: have you found a valid solution?

    # 2) Find all valid next-steps

    # 3) Return True if any valid solution is found

    if visited is None:
       visited = set()

    if idx in visited:
        return False

    #sgoes through the steps 
    if lst[idx]== 0 and (idx == len(lst) - 1):
        return True 
    elif lst[idx] == 0 and (idx != len(lst) - 1):
        return False

    else:
        #decides whether to go either left or right depending on the siuation
        steps = lst[idx]
        right = (idx + steps + len(lst))% len(lst)
        left = (idx - steps + len(lst)) % len(lst)

    visited.add(idx)
    #this is what it returns 
    return solve_puzzle(lst, right, visited) or solve_puzzle(lst, left, visited)
