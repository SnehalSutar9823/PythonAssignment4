import functools

Even=lambda no:no%2==0
Square=lambda no:no*2
Addition=lambda no1,no2:no1+no2

def FilterPrime(arr):
    ans=0
    primeArr=[]
    counter=0
    for j in range(len(arr)):
        counter=0
        if arr[j] > 1:
            for i in range(2,arr[j]):
                if (arr[j] % i) == 0:
                    counter=counter+i
                #print("Counter {}",format(counter))   
            if counter==0:
                primeArr.append(arr[j])    
    return primeArr
def Maximum(arr):
    max=0
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
            
    return max

def main():
    numbers=int(input("Enter total count of numbers to be stored in List:"))

    numArr=[]
    prime=[]
    for i in range(numbers):
        element=int(input("Enter Elements:"))
        numArr.append(element)

    print("Entered data is {}".format(numArr))
                          
    prime=FilterPrime(numArr)               
    print("Filtered data is {}".format(prime))

    print("Map data i.e. multiply by 2 all filtered numbers")

    squareArr=list(map(Square,prime))
    print("Mapped data is {}".format(squareArr))

    ans=Maximum(squareArr)
    print("Maximum of all modified filtered numbers is {}".format(ans))
if __name__=="__main__":
    main()


