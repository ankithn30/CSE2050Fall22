from LinearADTs import Stack_Wrapper, Queue_Wrapper, Deque_Wrapper
import unittest

class TestStackWrapper(unittest.TestCase):
    def test_init(self):
        Q = Queue_Wrapper()
        self.assetEqual(len(Q),0)

    def  test_push_pop(self):
        Q = Queue_Wrapper()
        n=10
        for i in range(n):
            self.assertEqual(len(Q),i)
            S.push(i)

        for i in range(n):
            self.assertEqual(len(Q),n-i)
            self.assertEqual(Q.dequeue), i)
class TestQueueWrapper(unittest.TestCase):
    pass

class TestDequeWrapper(unittest.TestCase):
    pass

unittest.main()
