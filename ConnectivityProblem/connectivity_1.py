# -*- coding: utf-8 -*-
"""
Connectivity problem
====================

+---------------------+------------+-------+------+
| algorithm           | initialize | union | find |
+---------------------+------------+-------+------+
| Quick-find          | N          | N     | 1    |
+---------------------+------------+-------+------+

Given a set of unions:

union(0,2)
union(1,4)
union(3,5)

Are two objects connected?

- We will first of all identify each item as a number

Connections:
- Reflexive: P is connected to P
- Symmetric: P is connected to q and q is connected to p
- Transitive: p is connected to q, q to r, r to p

Connected components: Maximal set of objects mutually connected

{0} {1, 4, 5} {2, 3, 6, 7}

Find query: Check if two objects in the same component

Union command: Replace componentes containing two objects with their union
{1, 4, 5} {3, 6} -> {1, 4, 5, 3, 6}
"""


class UnionFind:
    def __init__(self, n):
        """ In our array each one of the indexes will represent an item and
        the component number its value, so if id[1] and id[3] hace both
        the value 1, we can say that they are connected. At the beginning
        all the items will have its own component.
        """
        self.id = []

        for i in range(n):
            self.id.append(i)

    def union(self, p, q):
        """ We find both components and replace all the items that have the
        second item component id, so now they all belong to the same component.
        """
        pid = self.id[p]
        qid = self.id[q]
        for i in self.id:
            if self.id[i] == qid:
                self.id[i] = pid

    def connected(self, p, q):
        """In order to determine if two items are connected, we'll just
        check if they belong to the same component.
        """
        return self.id[p] == self.id[q]


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

