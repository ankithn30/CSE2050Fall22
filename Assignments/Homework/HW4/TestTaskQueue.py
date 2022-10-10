from TaskQueue import Task, TaskQueue
import unittest
class testUnitTask(unittest.TestCase):
    def test_init(self):
        T = Task(50,650)
        self.assertEqual(T.id, 50)
        

        T.reduce_cycles(50)
        self.assertEqual(T.cycles_left,600)
         
        
        T2 = Task(10,90)
        self.assertEqual(T2.id,10)

        T2.reduce_cycles(10)
        self.assertEqual(T2.cycles_left,80)

class TestUnitTaskQueue(unittest.TestCase):
    
    def test_init(self):
        T = Task(50,650)
        T2 = Task(10,90)
        TQ = TaskQueue(19)
        TQ = TaskQueue(15)
        TQ = TaskQueue()
        TQ.add_task(T)
        TQ.add_task(T2)
       

unittest.main()