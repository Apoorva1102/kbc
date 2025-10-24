print("KAUN BANEGA CROREPATI")
q1=["what is the capital of india?"]
op1=["mumbai","new delhi","pune","chennai"]
q2=["how many states are there in india"]
op2=[23,28,27,29]
q3=["who is the prime minister of india"]
op3=["me","narendra modi","putin","donald trump"]

print("question 1, for $10,000 on your screen", q1)
print(op1)
answer=input("enter the answer")
if answer=="new delhi":
   print("correct answer! you win $10,000")   
   print("question 2, for $20,000 on your screen", q2)
   print(op2)
   answer=input("enter the answer")
   if int(answer)==28:
       print("correct answer! you win $20,000")
       print("question 3, for $30,000 on your screen", q3)
       print(op3)
       answer=input("enter the answer")
       if answer=="narendra modi":
           print("correct answer! you win $30,000")
       else: print("wrong answer")    
   else: print("wrong answer")    
else: print("wrong answer")    


# this game is not for begineers