import math

def percentage_mod(number: float, percentage: float, pow:float = 1) -> float:
    return pow(number * (1 + (percentage / 100)), pow)

def find_percentage_mod(nb1: float, nb2: float) -> float:
    return 100 * ((nb2 - nb1) / nb1)

def multiplication_coeficient(evolution_percentage):
    return 1 + (evolution_percentage / 100)

def ex_1_and_2():
    evolution_lst = [0,5,-3,7,4,-2,6,3,2,-5,4,3,-1,6,3,-2,5,4,2,3,-1,5,4,3,4,2]
    evolution_global = 0
    
    CM_lst = []
    CM_global = 0

    # Iterates through list to find coeficients.. puts them in the evolution_list array
    for evolution in evolution_lst:
        CM_lst.append(multiplication_coeficient(evolution))

    # Prods the CM_lst to find the global CM
    CM_global = math.prod(CM_lst)

    # finds the evolution_global accordingly
    evolution_global = (CM_global - 1) * 100

    # Prints the results
    print("# EX. 1 + 2")

    print(f"Evolution list : {evolution_lst}")
    print(f"CM list : {CM_lst}\n")

    print(f"Global Evolution : {evolution_global}")
    print(f"Global CM : {CM_global}")


if (__name__ == '__main__'):
    ex_1_and_2()




    