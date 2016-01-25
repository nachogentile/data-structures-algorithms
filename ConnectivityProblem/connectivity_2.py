# -*- coding: utf-8 -*-
"""
Connectivity problem
====================

+---------------------+------------+-------+------+
| algorithm           | initialize | union | find |
+---------------------+------------+-------+------+
| Quick-union         |            |       |      |
+---------------------+------------+-------+------+

- Similar data structure, but now we have a tree.
- Each value points to its father.

Now the array looks like this

0  1  2  3  4  5  6  7  8  9
-----------------------------
0  9  6  5  4  2  6  1  0  5

Root = top parent node

- The root of 3 is 6
- The root of 7 is 6

"""


class UnionFind:
    def __init__(self, n):
        """ Create a list where each item is parent of itself.
        Same as before, but different interpretation.
        """
        self.id = []

        for i in range(n):
            self.id.append(i)

    def root(self, i):
        """ Retrieve the parent node until we find a root.
        The root will have a reflexive reference.
        """
        while i != self.id[i]:
            i = self.id[i]
        return i

    def union(self, p, q):
        """ Change root of p to point to root of q (depth
        of p and q array accesses).
        """
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def connected(self, p, q):
        """ Check if p and q have the same root (depth
        of p and q array accesses).
        """
        return self.root(p) == self.root(q)


if __name__ == '__main__':
    input = open('input', 'r')
    file_len = int(input.readline())
    uf = UnionFind(file_len)
    for i in range(file_len):
        line = input.readline().split(' ')
        p, q = [int(j) for j in line]
        if not uf.connected(p, q):
            uf.union(p, q)
            print "{} {}".format(p, q)
