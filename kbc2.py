i=0
print("wow")
questions=[
    ["what is the capital of india","A. New Delhi","B. Pune","C. Mumbai","D. Lucknow",1],
["who is harry potter","A. wizard","B. mudblood","C. slave","D. idiot",1],
["who is the cm of uttar pradesh","A. amit shah","B. arun jaitley","C. narendra modi","D. yogi adityanath",4],
["which among the following is an imposter game","A. BGMI","B. Kitchen story","C.Among us","D. subway surfers",3],
["what is the capital of china","A. shanghai","B. beijing","C. tokyo","D. delhi",2],
["what is the currency of india","A. rand","B. euro","C. dollar","D. rupee",4],
["what is the capital of india","A. New Delhi","B. Pune","C. Mumbai","D. Lucknow",1]
]
j=0
levels=[2000,5000,10000,20000,40000,80000,160000]
while(i<8):
    if i==2:
       MONEY=10000
    if i==4:
       MONEY=40000
    if i==6:
       MONEY=160000
    print(questions[i])
    answer=int(input("enter the answer"))
    if int(answer)==questions[i][5]:
      print("you win ",levels[j])
    else: 
       print("wrong")
       print("your take home money is",MONEY)
       break
    i=i+1
    j=j+1
