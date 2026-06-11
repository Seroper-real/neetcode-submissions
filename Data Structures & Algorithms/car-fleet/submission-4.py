class Solution:    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(cars,key=lambda x: x[0])
        #Use float division, the division carry give us 1 extra info other than the step needed:
        #It tell us if 2 car arrives at the same time or not.
        #I.E. k=10, pos=8, v=4 is not fleet with k=10, pos=9, v=4
        times = [(target - car[0]) / car[1] for car in cars]
        mx, count = None,0
        for time in reversed(times):
            if mx == None or time > mx:
                mx = time
                count+=1
        return count