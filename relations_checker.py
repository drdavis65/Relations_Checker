def is_reflexive(R, X):
    for e in X:
        j = (e, e)
        if j not in R:
            print("R is not reflexive")
            print(f"\te={e}, {j} in R is false\n")
            return False
    print("R is reflexive\n")
    return True


def is_symmetric(R, X):
    for e in X:
        for f in X:
            j = (e, f)
            k = (f, e)
            if j in R and k not in R:
                print(f"R is not symmetric\te={e}, f={f}, {j} in R iff {k} is false\n")
                return False
    print("R is symmetric\n")
    return True


def is_transitive(R, X):
    for e in X:
        for f in X:
            for g in X:
                i = (e, f)
                j = (f, g)
                k = (e, g)
                if i in R and j in R and k not in R:
                    print(f"R is not transitive\te={e}, f={f}, g={g}, ({i} in R and {j} in R) => {k} in R is false\n")
                    return False
    print("R is transitive\n")
    return True


def is_antisymmetric(R, X):
    for e in X:
        for f in X:
            j = (e, f)
            k = (f, e)
            if j in R and k in R and e != f:
                print(f"R is not antisymmetric\te={e}, f={f}, ({j} and {k} => {e}={f}) is false\n")
                return False
    print("R is antisymmetric\n")
    return True


def is_comparable(R, X):
    for e in X:
        for f in X:
            j = (e, f)
            k = (f, e)
            if j not in R and k not in R:
                print(f"R is not comparable\te={e}, f={f}, {j} or {k} in R is false\n")
                return False
    print("R is comparable\n")
    return True


def is_partially_ordered(reflexive_bool, transitive_bool, antisymmetric_bool):
    if reflexive_bool and transitive_bool and antisymmetric_bool:
        print("R is partially ordered\n")
        return True
    print("R is not partially ordered\n")
    return False


def is_totally_ordered(partially_ordered_bool, comparable_bool):
    if partially_ordered_bool and comparable_bool:
        print("R is totally ordered\n")
        return True
    print("R is not totally ordered\n")
    return False


def check_relation_properties(R, X):
    reflexive_bool = is_reflexive(R, X)
    is_symmetric(R, X)
    transitive_bool = is_transitive(R, X)
    antisymmetric_bool = is_antisymmetric(R, X)
    comparable_bool = is_comparable(R, X)
    is_partially_ordered(reflexive_bool, transitive_bool, antisymmetric_bool)
    is_totally_ordered(is_partially_ordered(reflexive_bool, transitive_bool, antisymmetric_bool), comparable_bool)


def main():
    # Input for set X
    x_input = input("Enter a comma-separated list of numbers for set X (e.g., '0,1,2'): ")
    X = {int(i.strip()) for i in x_input.split(",")}

    # Input for set R
    r_input = input("Enter a comma-separated list of tuples for relation R (e.g., '(0,0),(0,1),(1,0)'): ")
    R = {(int(tup.strip().split(",")[0][1:]), int(tup.strip().split(",")[1][:-1])) for tup in r_input.split(",")}

    check_relation_properties(R, X)


main()
