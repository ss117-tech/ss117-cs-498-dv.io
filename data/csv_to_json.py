import csv
from collections import defaultdict


def ctree():
    return defaultdict(ctree)


def build_leaf(name, leaf):
    """ Recursive function to build desired custom tree structure

    """
    res = {"name": name}

    # add children node if the leaf actually has any children
    if len(leaf.keys()) > 0:
        res["children"] = [build_leaf(k, v) for k, v in leaf.items()]

    return res


def main():
    """ The main thread composed from two parts.

    First it's parsing the csv file and builds a tree hierarchy from it.
    Second it's recursively iterating over the tree and building custom
    json-like structure (via dict).

    And the last part is just printing the result.

    """
    tree = ctree()
    # NOTE: you need to have test.csv file as neighbor to this file
    with open('sunburst.csv') as csvfile:
        reader = csv.reader(csvfile)
        for rid, row in enumerate(reader):
            if rid == 0:
                continue
            leaf = tree[row[0]]
            for cid in range(1, len(row)):
                leaf = leaf[row[cid]]

    # building a custom tree structure
    res = []
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf))

    # printing results int a json file
    import json
    with open ('sunburst.json', 'w') as f:
        json.dump(res, f)


main()
