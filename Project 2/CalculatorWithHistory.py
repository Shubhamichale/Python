def calculation(n,num1,num2):
    option_operator={
"+":1,
"-":2,
"*":3,
"/":4,
"%":5
}
    if(n=="1" or option_operator.get(n)==1):
        result=(f"{num1} + {num2} = {num1+num2}")
        return result
    elif(n=="2" or option_operator.get(n)==2):
        result=(f"{num1} - {num2} = {num1-num2}")
        return result
    elif(n=="3" or option_operator.get(n)==3):
        result=(f"{num1} * {num2} = {num1*num2}")
        return result
    elif(n=="4" or option_operator.get(n)==4):
        if(num2==0):
             return "Error: Division by zero!"
        else:
            result=(f"{num1} / {num2} = {num1/num2}")
            return result
    elif(n=="5" or option_operator.get(n)==5):
         if(num2==0):
              return "Error: Cannot take modulus with 0"
         else:
          result=(f"{num1} % {num2} = {num1%num2}")
          return result
while True:
        menu='''WHAT YOU WANT TO DO:
1.DO CALCULATION
2.VIEW PAST HISTORY
3.CLEAR HISTORY
'''
        print(f"\n{menu}")
        sel=int(input("ENTER YOUR CHOICE :"))
        if sel==1 :
            option='''CHOOSE AN OPERATION:
1.+
2.-
3.*
4./
5.%
'''
            print(option)
            chose=(input("ENTER THE CHOSEN OPERATION :"))
            num1=float(input("ENTER THE FIRST NUMBER :"))
            num2=float(input("ENTER THE SECOND NUMBER :"))
            sol=calculation(chose,num1,num2)
            print(sol)
            with open("CalculatorHistory.txt","a+") as k:
                 k.seek(0)
                 old_history=k.read()
            with open("CalculatorHistory.txt","w") as f:
                 f.write(f"{sol}\n{old_history}")
        
        elif(sel==2):
              with open("CalculatorHistory.txt") as file:
                 history=file.read()
                 if(history==""):
                      print("YOUR HISTORY IS EMPTY!")
                 else: 
                      print(f"YOU RECENT HISTORY :\n{history}")
        elif(sel==3):
              sur=input("ARE YOU SURE? (Y/N) :")
              if (sur.lower()=="y"):
                    open("CalculatorHistory.txt","w").close()
                    print("YOUR HISTORY IS SUCCESSFULLY DELETED!")
              
                   
        else:
              print("INVALID CHOICE! PLEASE SELECT A VALID OPTION.")
        
        dec=input("DO YOU WANT TO QUIT (Y/N) : ")
        if(dec.lower()=="y"):
            break
