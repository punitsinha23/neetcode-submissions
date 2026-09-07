class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 0
        lastTime = 0

        cars = [(p,s) for p,s in zip(position, speed)]
        for car in sorted(cars, reverse=True):
            time = (target - car[0])/car[1]
            if time > lastTime:
                fleet += 1
                lastTime = time

        return fleet