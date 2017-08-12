def main():
    fat_grams = int(input("How many grams of fat do you consume a day? "))
    carb_grams = int(input("How many grams of carbs do you consume a day? "))

    fat_calories, carb_calories = calorie_calculator(num1=fat_grams, num2=carb_grams)

    print("The total amount of calories from fat are", fat_calories, "and the total amount of calories" 
                                                                     " from carbs are", carb_calories)

def calorie_calculator(num1, num2):
    fat_calories = num1 * 9
    carb_calories = num2 * 4

    return fat_calories, carb_calories

main()