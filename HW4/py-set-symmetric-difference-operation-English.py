#  English newspaper ***********************************************************

english_newspaper_number = int(input())  # Number of students who have subscribed to the English newspaper
students_subscribed_english = set(input().split())  # List of student roll numbers who have subscribed to the English newspaper

#  French newspaper ************************************************************

french_newspaper_number = int(input())  # Number of students who have subscribed to the French newspaper
students_subscribed_french = set(input().split())  # List of student roll numbers who have subscribed to the French newspaper

# Result **********************************************************************

print(len(students_subscribed_english.symmetric_difference(students_subscribed_french)))
