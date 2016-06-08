a = int(input("Please Enter any Number: "))
r = 0
while(a > 0):
    Reminder = a %10
    r = (r *10) + Reminder
    a = a //10
print("\n reversed num:",r)
