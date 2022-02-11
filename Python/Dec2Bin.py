givenNumber = input("Decimal: ")
#givenNumber = "88"

givenNumber = int(givenNumber)
result = []

while givenNumber > 0:

    rest = givenNumber % 2
    result.append(str(rest))
    if rest == 1:

        givenNumber = (givenNumber - 1)/2

    else:

        givenNumber = givenNumber / 2

result = ''.join(result)
print(result)