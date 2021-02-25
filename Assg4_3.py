import functools

WithinRange=lambda no:no>70 and no<90
Increment=lambda no:no+10
Multiplication=lambda no1,no2:no1*no2

def PerformR(arr):
    ans=0
    for i in range(len(arr)):
        ans=ans+arr[i]

    return ans

def main():
    numbers=int(input("Enter total count of numbers to be stored in List:"))

    numArr=[]

    for i in range(numbers):
        element=int(input("Enter Elements:"))
        numArr.append(element)

    print("Entered data is {}".format(numArr))
                          
    withinRange=list(filter(WithinRange,numArr))               
    print("Filtered data is {}".format(withinRange))

    print("Map data i.e. add 10 in all filtered numbers")

    addArr=list(map(Increment,withinRange))
    print("Mapped data is {}".format(addArr))

    ans=functools.reduce(Multiplication,addArr)
    #ans=functools.reduce(lambda no1,no2: (no1+no2),list(map(lambda no:(no+2),list(filter(lambda no:(no%2==0),numArr)))))
    #ans=PerformR(addArr)
    print("Multiplication of all modified filtered numbers is {}".format(ans))
if __name__=="__main__":
    main()


