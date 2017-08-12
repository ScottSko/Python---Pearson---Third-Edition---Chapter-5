def main():
    test_score_1 = int(input("What is your first test score? "))
    test_score_2 = int(input("What is your second test score? "))
    test_score_3 = int(input("What is your third test score? "))
    test_score_4 = int(input("What is your fourth test score? "))
    test_score_5 = int(input("What is your fifth test score? "))

    print("On the first test, you received a(n):",determine_grade(test_score_1))
    print("On the second test, you received a(n):",determine_grade(test_score_2))
    print("On the third test, you received a(n):",determine_grade(test_score_3))
    print("On the fourth test, you received a(n):",determine_grade(test_score_4))
    print("On the fifth test, you received a(n):",determine_grade(test_score_5))

    print("Your average was", calc_average(test_score_1, test_score_2, test_score_3, test_score_4, test_score_5))

def calc_average(score_1, score_2, score_3, score_4, score_5):
    return (score_1 + score_2 + score_3 + score_4 + score_5) / 5

def determine_grade(test_score):
    if test_score >= 90:
        return "A"
    if test_score >= 80 and test_score <= 89:
        return "B"
    if test_score >= 70 and test_score <= 79:
        return "C"
    if test_score >= 60 and test_score <= 69:
        return "D"
    if test_score <= 60:
        return "F"

main()