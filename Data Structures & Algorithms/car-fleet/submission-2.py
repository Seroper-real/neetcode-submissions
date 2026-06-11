class Solution:    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(cars,key=lambda x: x[0])
        times = []
        for car in cars:
            a = target - car[0]
            b = car[1]
            times.append(a/b)
        mx, count = None,0
        print(cars,times)
        for time in reversed(times):
            if mx == None or time > mx:
                mx = time
                count+=1
        return count