givenNumber = input("Binary: ")
#givenNumber = "11111111"

length = len(givenNumber)

cLength = length
counter = 0
result = 0

while counter < length:

    number = givenNumber[counter]
    #print(number)
    #print(cLength)
    powNumber = int(number) * (2**int(cLength))
    #print(powNumber)
    result += int(powNumber)

    counter += 1
    cLength -= 1

result /= 2
print(int(result))