1.Rewrite your pay computation
to give the employee 1.5 times
the hourly rate for hours worked
above 40 hours.
#######
hours =input('Enter Hours: ')
rate =input('Enter Rate: ')
if hours > 40:
extra_time = float(hours) - 40
else:
extra_time = 0
extra_pay = 0.5 * float(rate) * extra_time
pay = float(hours) * float(rate) + extra_pay
print ('Pay: '),
print(pay)

2.Rewrite your pay program using try and
except so that your program handles
non-numeric input gracefully by printing
a message and exiting the program. 
The following shows two executions of
the program:
#############
hours=input("enter hours")
try:
input(hours)
r=input("enter rate")
int(r)
pay=hours*r
int(pay)
print("pay ",pay)
except:
print("enter a valid input")


Write a program to prompt for a score between
0.0 and 1.0. If the score is out of range,
print an error message. If the score 
is between 0.0 and 1.0, print a grade 
using the following table:
########
input_score = raw_input('Enter a score between 0.0 and 1.0: ')
try:
  if (float(input_score) >= 0) and ( float(input_score) <= 1 ):
    print('valid input, thanks!')
  else:
    print (error_msg_invalid)
    input_score = raw_input('Enter a score between 0.0 and 1.0: ')
except:
  print (error_msg_invalid)
  input_score = raw_input('Enter a score between 0.0 and 1.0: ')
input_score = float(input_score)
if input_score < 0.6:
  print ('F')
elif input_score >= 0.9:
  print ('A')
elif input_score >= 0.8:
  print ('B')
elif input_score >= 0.7:
  print('C')
elif input_score >= 0.6:
  print('D')
else:
  print ('enter valid score')
