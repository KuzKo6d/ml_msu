def find_modified_max_argmax(L, f):
    return max(((f(v), i) for i, v in enumerate([j for j in L if type(j) is int])), default=())