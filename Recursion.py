#Question 1

#Iterative
def iterative_sum():
    number = int(input("Enter a Number: "))
    number_list = list(map(int, str(number)))
    print(sum(number_list))


#Recursive
def recursive_sum():
    number = int(input("Input Number: "))
    # Base Case
    if number == 0:
        print(0)
    else:
        sum = 0
        while(number > 0):
            remainder = number % 10
            sum = sum + remainder
            number = number // 10

    print("sum of digits = {}".format(sum))


#Question 2

#Recursive Pallindrome

def recursive_Pallindrome():

    #Process and case correct word
    keyWord = input("Input Word: ")
    keyWord_lower_case = keyWord.lower()

    #Find reversed word
    resultant = ""
    for i in range(len(keyWord_lower_case),0 ,-1):
        resultant += keyWord_lower_case[i - 1]

    #Check if both reversed word and initial keyWord is the same
    if(keyWord_lower_case == resultant):
        print("Is A Pallindrome")
    else:
        print("Is NOT a Pallindrome")

#Iterative Pallindrome
def iterative_Pallindrome():
    keyWord = input("Input Word: ")
    reversed_keyWord = "".join(reversed(keyWord))
    if(reversed_keyWord == keyWord):
        print("Is A Pallindrome")
    else:
        print("Is NOT a Pallindrome")

recursive_sum(12)
