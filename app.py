import random

#Finding minimum of random numbers

randNum = []
for x in range(10):
    randNum.append(random.randint(0,100))
print(min(randNum))
test = "Sample string"
num = int(input("Enter a number:  "))
print("You entered {} test {} ".format(num,test))

list = [random.randint(0,10) for x in range(3)]
print(list)
test_var = ["hello" for x in range(2)]
print(test_var)
for x in range(5):
    print(test_var)

chances = int(input("Enter no. of chances: "))  

#function to provide x no. of chances
def run_func_x_time(chances):
    for x in range(chances):
        rand_num = random.randint(0,10)
        print("This is attempt {} ".format(x+1))
        num_entered = int(input("Guess a number between 0 and 10: "))
        if(rand_num == num_entered):
            print("Correct guess")
            break
        else:
            print("Incorrect guess")
            continue

run_func_x_time(chances)    

def get_player_number():
    number_csv = input("Enter 6 numbers seperated by commas:\n")
    number_list = number_csv.split(',')
    number_set = {int(number) for number in number_list}
    return number_set

print(get_player_number())
