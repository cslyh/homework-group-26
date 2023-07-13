import hashlib
import math


def construct_leaf(data):
    return hashlib.sha256(data).digest()


def construct_tree(leaves):
    num_leaves = len(leaves)
    if num_leaves == 0:
        return None
    if num_leaves == 1:
        return leaves[0]

    tree = []
    for i in range(0, num_leaves, 2):
        if i + 1 < num_leaves:
            left = leaves[i]
            right = leaves[i + 1]
            tree.append(hashlib.sha256(left + right).digest())
        else:
            tree.append(leaves[i])

    return construct_tree(tree)


def verify_proof(leaf, proof, root):
    computed_hash = leaf
    for node_hash, direction in proof:
        if direction == 'left':
            computed_hash = hashlib.sha256(computed_hash + node_hash).digest()
        else:
            computed_hash = hashlib.sha256(node_hash + computed_hash).digest()

    return computed_hash == root


# Example usage:
leaves = [construct_leaf(b'leaf1'), construct_leaf(b'leaf2'), construct_leaf(b'leaf3')]
root = construct_tree(leaves)
print("Root:", root.hex())

# Example proof verification: leaf2
leaf2 = construct_leaf(b'leaf2')
proof = [(leaves[0], 'right'), (leaves[2], 'left')]
print("Proof verification:", verify_proof(leaf2, proof, root))