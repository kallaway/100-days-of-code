"""
Complete the function/method (depending on the language) to return true/True when its argument is an array that
has the same nesting structures and same corresponding length of nested arrays as the first array.

should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

should return False
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
"""


def deep_lists_checker(lista: list) -> list:
    result = []
    for item in lista:
        if isinstance(item, list):
            result.append(len(item))
            result.append(deep_lists_checker(item))
        else:
            result.append(None)
    return result


def same_structure_as(original, other):
    # if isinstance(original, list) and isinstance(other, list):
    #     origin = deep_lists_checker(original)
    #     other = deep_lists_checker(other)
    #     return origin == other
    # else:
    #     return False
    return deep_lists_checker(original) == deep_lists_checker(other) if isinstance(original, list) and isinstance(other, list) else False


if __name__ == "__main__":
    original= [ [ [ ], [ ] ] ]
    other = [ [ [ ], [ 2] ] ]
    print(same_structure_as(original, other))