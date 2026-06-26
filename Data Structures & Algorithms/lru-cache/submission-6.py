class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.mp: Dict(int, Node) = {}
        self.ll_begin = None
        self.ll_end = None
        self.size = 0

    def get(self, key: int) -> int:
        #print(f"--- INIT GET: {self.print_ll(self.ll_begin)}")
        if key not in self.mp: return -1
        existing_node = self.shift_existing(key)
        #print(f"--- FIN  GET {key}: {self.print_ll(self.ll_begin)}")
        return existing_node.val

    def put(self, key: int, value: int) -> None:
        #print(f"--- INIT PUT: {self.print_ll(self.ll_begin)}")
        if key not in self.mp:
            new_node = self.Node(key,value)
            self.mp[key] = new_node
            
            if self.ll_begin == None:
                self.ll_begin = new_node
            
            if self.ll_end == None:
                self.ll_end = new_node
            else:
                self.ll_end.next = new_node
                new_node.prev = self.ll_end
                self.ll_end = new_node
            self.size += 1

            while self.size > self.cap:
                self.size -= 1
                to_remove = self.ll_begin
                self.mp.pop(to_remove.key, None)    
                self.ll_begin = to_remove.next
                if self.ll_begin: self.ll_begin.prev = None
                to_remove.next = None
                to_remove.prev = None
        else:
            existing_node = self.shift_existing(key)
            existing_node.val = value
        #print(f"--- FIN  PUT {key},{value}: {self.print_ll(self.ll_begin)}")
    
    def shift_existing(self, key: int) -> Optional[Node]:
        existing_node = self.mp[key]
        if existing_node.next == None: #Case if node is already in tail
            return existing_node 


        if existing_node.prev == None: #Case if node is the head of the list
            self.ll_begin = existing_node.next #Shift head of the list
            self.ll_begin.prev = None
            

        else: #Case if node is between 2 or more nodes
            prev_node = existing_node.prev
            prev_node.next = existing_node.next # Bypass existing_node
            existing_node.next.prev = prev_node

        #Put existing_node at the end of the list 
        self.ll_end.next = existing_node
        existing_node.prev = self.ll_end
        self.ll_end = existing_node
        self.ll_end.next = None

        return existing_node

    def print_ll(self, ll: Optional[Node]) -> str:
        s = ""
        while ll:
            s+= f"[{ll.key}, {ll.val}]->"
            ll = ll.next
        return s[:len(s)-2]

    class Node:
        def __init__(self, key: int = None, val: int = None, next: Optional[Node] = None, prev: Optional[Node] = None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev
