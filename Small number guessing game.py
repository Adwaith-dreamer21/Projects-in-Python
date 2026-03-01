import random       #imporating random module
n=int(input(("Enter a number: ")))
jk=random.randint(1,100)      #take a number between 1 and 100
count=1       #Intaliazed the count which user have guessed
while n!=jk:     #The loop runs till the given condition is wrong eg when n==jk the loop will stop
    if n<jk:     #If the number is smaller than the random number it will excute this number
        print("Give a Bigger number")
    else:       #else this statement excutes  where  n is bigger than the random number 
        print("Give a smaller number")
    n=int(input("Enter a  number: "))       #if the number is wrong the program ask to entert lesser number or bigger number
    count+=1       #the count of the guess add by 1 one after every loop excution
print('Your guess is correct')      #if n==jk then the print statemnt excutes printing the statement your guess is correct 
print(f'You have taken {count} guess')   #gives tghe total guess takn by the user  
