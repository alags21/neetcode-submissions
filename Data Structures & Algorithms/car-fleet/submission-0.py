class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        
        cars.sort(reverse=True)

        fleets = 0
        fleet_time = 0

        for car in cars:
            start = car[0]
            velocity = car[1]
            arrival = (target-start) / velocity

            if arrival > fleet_time:
                fleets += 1
                fleet_time = arrival

        return fleets