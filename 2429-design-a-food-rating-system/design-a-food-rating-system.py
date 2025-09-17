class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):

        self.food_info = {}
        self.cusine_map = defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_info[f] = [c , r]
            heapq.heappush(self.cusine_map[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cusine, _ = self.food_info[food]
        self.food_info[food][1] = newRating
        heapq.heappush(self.cusine_map[cusine], (-newRating, food))        

    def highestRated(self, cuisine: str) -> str:

        while True:
            rating, food = self.cusine_map[cuisine][0]
            if -rating == self.food_info[food][1]:
                return food
            heapq.heappop(self.cusine_map[cuisine])
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)