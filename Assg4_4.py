import functools

Even=lambda no:no%2==0
Square=lambda no:no*no
Addition=lambda no1,no2:no1+no2

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
                          
    even=list(filter(Even,numArr))               
    print("Filtered data is {}".format(even))

    print("Map data i.e. square of all filtered numbers")

    squareArr=list(map(Square,even))
    print("Mapped data is {}".format(squareArr))

    ans=functools.reduce(Addition,squareArr)
    #ans=functools.reduce(lambda no1,no2: (no1+no2),list(map(lambda no:(no+2),list(filter(lambda no:(no%2==0),numArr)))))
    #ans=PerformR(addArr)
    print("Addition of all modified filtered numbers is {}".format(ans))
if __name__=="__main__":
    main()


