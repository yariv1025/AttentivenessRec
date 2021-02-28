import unittest
# from solutions import Collection


# Example:

class MyTestCase(unittest.TestCase):

    def test_first(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.first(), 3)

    def test_last(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.last(), 9)

    def test_take(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertTupleEqual(c.take(2).values(), (3, 4))

    def test_append(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.append(10,11,12), Collection((3, 4, 5, 7, 8, 9, 10 ,11, 12)))

    def test_prepend(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.prepend(0, 1, 2), Collection((0,1,2,3,4,5,7,8,9)))

    def test_filter(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.filter(lambda x: x % 2 == 0).Iterable,(4,8))

    def test_map(self):
        c = Collection((3,4,5,7,8,9))
        self.assertEqual(c.map(lambda x: x + 2).Iterable, (5, 6, 7, 9, 10, 11))

    def test_reduce(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.reduce(lambda x,y: x + y, 0), 36)

    def test_sort(self):
        c1 = Collection((1, 2, 3, 4))
        self.assertEqual(c1.sort(key = lambda x: x + 2 , reversed = False), Collection(3,4,5,6))
        #TODO: FIX : Sort by index and not by lambda!

    def test_set(self):
        c = Collection((3, 4, 5, 7, 8, 9))
        self.assertEqual(c.set(3,{'a' : 1, 'b' : 2}).values(), (3, 4, 5, {'a' : 1, 'b' : 2}, 8, 9))

    def test_pluck(self):
        c = Collection([{'name': 'Joe', 'age': 20}, {'name': 'Jane', 'age': 13}])
        self.assertEqual(c.pluck('age'), (20,13))

    def test_values(self):
        c = Collection(('a', 'b', 'c', 'd'))
        self.assertEqual(c.values(), ('a', 'b', 'c', 'd'))

    def test_unique(self):
        c1 = Collection((4,3,4,5,5,7,8,9))
        self.assertTupleEqual((c1.unique()).values(), (4, 3, 5, 7, 8, 9))

    def test_tap(self):
        c = Collection((1,2,3,4))
        callback = lambda x : x + 2
        self.assertEqual(c.tap(callback),None)

    def test_getitem(self):
        c = Collection(("A", "B", "C"))
        self.assertEqual(c.__getitem__(1), 'B')

    def test_add(self):
        c = Collection((1,2,3,4))
        b = Collection(('abcd'))
        self.assertEqual(c.__add__(b), Collection((1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')))

    def test_sub(self):
        c = Collection((1,2,3,4))
        self.assertEqual(c.__sub__((3,4,5,6)), (1,2))

    def test_len(self):
        c = Collection((1,2,3,4))
        self.assertEqual(len(c), 4)

    def test_contains(self):
        c = Collection(('a', 'b', 'c'))
        self.assertEqual(c.__contains__('a'), True)

    def test_eq(self):
        c = Collection((1,2,3,4))
        self.assertEqual(c.__eq__((1,2,3,4)), True)

    def test_ne(self):
        #self.assertEqual(not(TESTEQ.test_eq((1,2,3,4,5))) , False)
        c = Collection((1,2,3,4,5))
        self.assertEqual(c.__ne__((1,2,3,4,5)) , False)

    def test_str(self):
        c = Collection(('a', 'b', 'c', 'd'))
        self.assertEqual(c.__str__(), ('a', 'b', 'c', 'd'))

    def test_repr(self):
        c = Collection((1,2,3,4))
        self.assertEqual(repr(c), "Collection(1,2,3,4)")


if __name__ == '__main__':
    unittest.main()
