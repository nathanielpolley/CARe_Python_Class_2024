import math
final=input("enter final count=")
init= input("enter initial input=")
time= input("enter time input=")

if final.isdigit() and init.isdigit() and time.isdigit():
    final=int(final)
    init=int(init)
    time=int(time)

    if final >init:
       calculation= (math.log(final)-math.log(init))/time
       print(f"cell growth rate is: {round(calculation,4)}")
    else:
        print("please input final count greater than initial")
else:
      print("please use valid numerical input (no negatives or decimals")

