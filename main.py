#P1
#print('Input a temperature in Fahrenheit')
#a=int(input())
#b=(a-32)*5/9
#print(b,"°C")
#I've printed a sentence that would ask the user to input a number in Fahrenheit. Then the number that they input would be (a-32)*5/9 which is the formula used to convert it into Celsius. Finally, the printed output would be the answer with °C symbol at the end to indicate the unit of the temperature.

#P2
#print("Print F to convert input into Fahrenheit or C to convert input into Celcius")
#a=input()
#if a=='C':
  #print("Input temperature in Fahrenheit")
  #a=int(input())
  #print(round((a-32)*5/9,"°C"))
#else:
  #print("Input temperature in Celcius")
  #a=int(input())
  #print(round((a* 9/5) + 32,"°F"))
#I've made an "IF" statement that asks the user to press C or F depending if they want their number to be converted into Celcius or Fahrenheit.Then the "IF" statement converts the input into Celcius if C is inputted or Fahrenheit in F is inputted. 

#P3
#result=1
#a=input("Input words. Once done, press x to count the amount of words listed.")
#while True:
  #a=input()
  #if a=="x":
    #b="You've typed "+ str(result) +" words"
    #print(b)
    #break
  #elif a!="x":
    #result+=1
  #else:
    #print()
#Since this question includes counting and adding things together, I used result=1 to initiate a starting point. A while loop was used inorder to create a loop when x is pressed the loop stops due to the break and if x isn't pressed, the user can keep on adding words.

#P4
#print("A numeric password is set, guess the password.")
#i= False
#while i==False:
  #a=input()
  #if a=="3458":
    #i= True
    #print('Correct')
  #else:
    #print('Try again')
#I used a "While loop" inorder for the loop to keep on going for the statement to be false until the loop ends and the answer is true. So, while the answer is false, the user can keep on trying until the statment is true, where the loop ends.

#P5
#print("Enter 10 numbers")
#a=int(input())
#b=int(input())
#c=int(input())
#d=int(input())
#e=int(input())
#f=int(input())
#g=int(input())
#h=int(input())
#i=int(input())
#j=int(input())
#l= a,b,c,d,e,f,g,h,i,j
#print(l, sep=',', end=' ')
#Once the user inputs 10 numbers from a-l, the numbers will then be put next to eachother by the veriable l that is assigned to keep everything next to each other and printed with a sep and an end.
    