# FILE NAME - grade_converter.py

# NAME: Antonio Santiago
# DATE: 10/1/2025
# BRIEF DESCRIPTION: Program that converts user number grade into a letter grade



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

def main():
    convert_grade()

def convert_grade():
   print('===== Grade Converter =====')
   num_grade = int(input('Enter a numerical grade (1-100): '))

   if num_grade > 100:
      print('A+')
   elif 90 <= num_grade <= 100:
      print('A')
   elif 80 <= num_grade < 90:
      print('B')     
   elif 70 <= num_grade < 80:
      print('C')
   elif 65 <= num_grade < 70:
      print('D')
   else:
      print('F') 

main()








########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?
Look into using range for this lab instead of using greater than and less than if statements.






'''
