class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        store = defaultdict(int)

        for task in tasks:
            store[task] += 1

        heap = [(-priority, task) for task, priority in store.items()]
        heapq.heapify(heap)

        #Normalize heap
        stack = deque()
        while heap:
            stack.append(heapq.heappop(heap)[1])
        idx = 0
        while stack:
            heapq.heappush(heap,(idx, stack.popleft()))
            idx += 1

        res = []
        idx = 0
        while heap:
            print(heap)
            if heap[0][0] <= idx:
                priority, task = heapq.heappop(heap)
                res.append(task)
                idx += 1
                store[task] -= 1
                if store[task] > 0:
                    heapq.heappush(heap, (priority + n + 1, task))
            else:
                res.append("idle")
                idx += 1
        print(res)
        return len(res)

            
