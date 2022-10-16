"""
2353. Design a Food Rating System
Design a food rating system that can do the following:
- Modify the rating of a food item listed in the system.
- Return the highest-rated food item for a type of cuisine in the system.

Implement the FoodRatings class:
- FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
    - foods[i] is the name of the i-th food
    - cuisines[i] is the type of cuisine of the i-th food
    - ratings[i] is the initial rating of the i-th food.
- void changeRated(String, cuisine) Changes the rating of the food item with the name food.
- String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.

Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.

Example1:
Input
["FoodRatings", "highestRated", "highestRated", "changeRating",
    "highestRated", "changeRating", "highestRated"]
[[["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese",
    "korean"], [9, 12, 8, 15, 14, 7]], ["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]
Output
[null, "kimchi", "ramen", null, "sushi", null, "ramen"]

Explanation
FoodRatings foodRatings = new FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);
foodRatings.highestRated("korean"); // return "kimchi"
                                    // "kimchi" is the highest rated korean food with a rating of 9.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); // "sushi" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "sushi"
                                      // "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); // "ramen" now has a rating of 16.
foodRatings.highestRated("japanese"); // return "ramen"
                                      // Both "sushi" and "ramen" have a rating of 16.
                                      // However, "ramen" is lexicographically smaller than "sushi".

Constraints:
1 <= n <= 2 * 10^4
n == foods.length == cuisines.length == ratings.length
1 <= foods[i].length, cuisines[i].length <= 10
foods[i], cuisines[i] consist of lowercase English letters.
1 <= ratings[i] <= 10^8
All the strings in foods are distinct.
food will be the name of a food item in the system across all calls to changeRatings.
cuisine will be a type of cuisine of at least one food item in the system across all calls to highestRated.
At most 2 * 10^4 calls in total will be made to changeRating and highestRated.
"""

"""
Note:
1. SortedList + HashTable:
__init__: O(nlogn) time | O(n) space
changeRating: O(logn) time | O(1) space
highestRated: O(1) time | O(1) space
"""




import unittest
import collections
from sortedcontainers import SortedList
from typing import List
class FoodRatings:
    # __init__ initialized the FoodRatings TC: O(nlogn) SC: O(n)
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisineBST = collections.defaultdict(SortedList)
        self.foodInfos = {}
        self.cuisineHighScoredFood = {}
        for i in range(len(foods)):
            food = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]
            self.foodInfos[food] = (cuisine, rating)
            self.cuisineBST[cuisine].add((-rating, food))

        for cuisine in self.cuisineBST.keys():
            _, food = self.cuisineBST[cuisine][0]
            self.cuisineHighScoredFood[cuisine] = food

    # changeRating change the rating to newRating: TC: O(logn) SC: O(1)

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, oldRating = self.foodInfos[food]
        if newRating == oldRating:
            return
        self.cuisineBST[cuisine].remove((-oldRating, food))
        self.cuisineBST[cuisine].add((-newRating, food))
        self.foodInfos[food] = (cuisine, newRating)

        # get hightest rating foodInfo
        _, food = self.cuisineBST[cuisine][0]
        self.cuisineHighScoredFood[cuisine] = food

    # highestRated return the largest score food's name (if same score, return lexi smallest) TC: O(1) SC: O(1)
    def highestRated(self, cuisine: str) -> str:
        return self.cuisineHighScoredFood[cuisine]


# Unit Tests

classes = [FoodRatings]


class TestFoodRatings(unittest.TestCase):
    def testFoodRatings1(self):
        for myclass in classes:
            foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
            cuisines = ["korean", "japanese", "japanese",
                        "greek", "japanese", "korean"]
            ratings = [9, 12, 8, 15, 14, 7]
            foodRatings = myclass(
                foods=foods, cuisines=cuisines, ratings=ratings)

            # return "kimchi", "kimchi" is the highest rated korean food with a rating of 9.
            self.assertEqual(foodRatings.highestRated("korean"), "kimchi")

            # return "ramen", "ramen" is the highest rated japanese food with a raing of 14.
            self.assertEqual(foodRatings.highestRated("japanese"), "ramen")

            # "sushi" now has a rating of 16.
            foodRatings.changeRating("sushi", 16)

            # return "sushi", "sushi" is the highest rated japanese food with a rating of 16.
            self.assertEqual(foodRatings.highestRated("japanese"), "sushi")

            # "ramen" now has a rating of 16.
            foodRatings.changeRating("ramen", 16)

            # return "sushi", both "sushi" and "ramen" have a rating of 16.
            # However, "ramen" is lexicographically smaller than "sushi".
            self.assertEqual(foodRatings.highestRated("japanese"), "ramen")


if __name__ == "__main__":
    unittest.main()
