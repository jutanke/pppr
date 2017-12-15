import unittest
import sys
sys.path.insert(0,'../')

from pppr import aabb

class Testaabbmetry(unittest.TestCase):

    def test_inside_aabb(self):
        bb = (0, 0, 10, 10)
        self.assertTrue(aabb.is_inside(bb,(5,5)))
        self.assertTrue(aabb.is_inside(bb,(9,9)))
        self.assertTrue(aabb.is_inside(bb,(0,0)))
        self.assertTrue(aabb.is_inside(bb,(0,9)))

        self.assertFalse(aabb.is_inside(bb,(0,-9)))
        self.assertFalse(aabb.is_inside(bb,(-1,-1)))


    def test_inside_negative_aabb(self):
        bb = (-20, -20, 10, 10)
        self.assertFalse(aabb.is_inside(bb,(5,5)))
        self.assertFalse(aabb.is_inside(bb,(9,9)))
        self.assertFalse(aabb.is_inside(bb,(0,0)))
        self.assertFalse(aabb.is_inside(bb,(0,9)))
        self.assertFalse(aabb.is_inside(bb,(0,-9)))
        self.assertFalse(aabb.is_inside(bb,(-1,-1)))

        self.assertTrue(aabb.is_inside(bb,(-15,-15)))
        self.assertTrue(aabb.is_inside(bb,(-19,-19)))
        self.assertTrue(aabb.is_inside(bb,(-11,-15)))
        self.assertTrue(aabb.is_inside(bb,(-20,-19)))

    def test_intersection(self):
        A = (0, 0, 10, 10)
        B = (5, 0, 10, 10)
        int_ab = aabb.intersection(A, B)
        self.assertEqual(int_ab, 5*10)

        A = (0, 0, 10, 10)
        B = (15, 0, 10, 10)
        int_ab = aabb.intersection(A, B)
        self.assertEqual(int_ab, 0)

        int_ab = aabb.intersection(A, A)
        self.assertEqual(int_ab, 10*10)

    def test_iou(self):
        A = (0, 0, 10, 10)
        B = (5, 0, 10, 10)

        #self.assertEqual(aabbmetry.IoU_aabb(A, B), 1/3)

if __name__ == '__main__':
    unittest.main()