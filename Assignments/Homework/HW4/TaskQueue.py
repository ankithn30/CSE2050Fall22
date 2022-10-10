class Task:

    def __init__(self, id, cycles_left):


      self.id = id

      self.cycles_left = cycles_left

      self.prev = None

      self.next = None

    

    def reduce_cycles(self, cycles):

        self.cycles_left -= cycles



class TaskQueue:

    def __init__(self, cycles_per_task = 1):
        self.current = None
        self.cycles_per_task = cycles_per_task
        self._len = 0




    def add_task(self, task:Task):   

        if self.is_empty():

           self.current = task

           self.current.next = task

           self.current.prev = task



        else:

            self.current.prev.next = task

            task.prev = self.current.prev

            task.next = self.current

            self.current.prev = task


        self._len += 1

            

           

    def remove_task(self,id_num):

        current_item = self.current

        if self.is_empty() or (self._len == 1 and self.current.id != id_num):

            raise RuntimeError("id " + str(id_num) + " not in TaskQueue")


        i=0


        while i != self._len:

            if  current_item.id ==id_num:

                current_item.prev.next = current_item.next

                current_item.next.prev = current_item.prev4

                if (current_item == self.current):

                    if (current_item == current_item.next):

                        self.current = None
                    else:
                        self.current = self.current.next

                self._len -= 1
                return

            else:

                current_item = current_item.next 

                i +=1
        else:

            raise RuntimeError("id " + str(id_num) + " not in TaskQueue")


    def is_empty(self):

        return len(self)==0


    def __len__(self):

        return self._len


    def execute_tasks(self):

        current_item = self.current

        counter = 0


        while(self.is_empty() != True):

            if current_item.cycles_left >= self.cycles_per_task:

                current_item.reduce_cycles(self.cycles_per_task)

                counter += self.cycles_per_task

            else:

                counter += current_item.cycles_left

                print("Finished task " + str(current_item.id) + " after " + str(counter) + " clock cycles")

                self.remove_task(current_item.id)


            current_item = current_item.next


        return counter
