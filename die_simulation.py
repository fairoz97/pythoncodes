from random import randint

def roll_die(n):
    sum_of_rolls = []
    for i in range(n):
        die1 = randint(1,6)
        die2 = randint(1,6)
        sum = die1 + die2
        #print(sum)
        sum_of_rolls.append(sum)
    #print(sum_of_rolls)
    return sum_of_rolls


def main():
    count ={
        2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0
    }
    n = int(input("Enter number of rolls: "))
    list = roll_die(n)
    for num in list:
        if num in count:
            count[num]+=1
    print("  Sum  " + "  Simulated Percentage  ")
    for key in count:
        percentage = float (count[key] / n *100)
        print("  ", key, "     " ,round(percentage,2))
    #print(count)


    #print(roll_die(n))


main()