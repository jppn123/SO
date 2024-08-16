class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Queue:
    def __init__(self):
        self.ini = None

    def len(self):
        curr = self.ini
        ln = 0
        while curr:
            ln += 1
            curr = curr.next
        
        return ln 
    
    def printQueue(self):
        if self.len() == 0:
            print("no data")
        curr = self.ini
        data = ""
        while curr:
            data += str(curr.data) + ","
            curr = curr.next
        if data != "" and data != None:
            print(data[:-1])

    def push(self, data):
        node = Node(data)
        if self.len() == 0:
            self.ini = node
        else:
            curr = self.ini
            
            while curr.next != None:
                curr = curr.next
            curr.next = node
    
    def remove(self):
        if self.len() == 0:
            return "no data"
        else:
            data = self.ini.data
            if self.len() == 1:
                self.ini = None
            else:
                self.ini = self.ini.next
        return data
        
    def isInQueue(self, pName):
        curr = self.ini
        flag = 0
        while curr:
            if curr.data == pName:
                flag = 1
            curr = curr.next
        if flag == 0:
            return False
        return True
                
                
        


