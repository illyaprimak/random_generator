import random

minimum = int
maximum = int
amount = int


def firstStep():
    print("Мінімальне число у списку")
    number = input("Введіть значення : ")
    validateNumber(number, 1)


def secondStep():
    print("Максимальне число у списку")
    number = input("Введіть значення : ")
    validateNumber(number, 2)


def thirdStep():
    print("Кількість єлементів у списку")
    number = input("Введіть значення : ")
    validateNumber(number, 3)


def finishStep():
    print("Готово!")
    global minimum, maximum, amount
    list = generateRandomList(minimum, maximum, amount)
    print("Список випадкових цілих чисел : ", list)
    list.sort()
    dictionary = formDictionary(list)
    print("Словник з випадковими цілими числами та їх кількістю у списку : ", dictionary)
    print("У списку випадкових чисел , числа зустрічаються у такій кількості: ")
    for number in dictionary:
        print("Число \"" + str(number) + "\" зустрічається " + str(dictionary[number]) + " разів")


def generateRandomList(minimum, maximum, amount):
    random_list = [random.randint(minimum, maximum) for i in range(amount)]
    return random_list


def formDictionary(list):
    dictionary = dict.fromkeys(list, 0)
    for word in list:
        dictionary[word] += 1
    return dictionary


def validateNumber(number, step):
    if number.isdigit():

        if step == 1:
            global minimum
            minimum = int(number)
            secondStep()
        if step == 2:
            global maximum
            maximum = int(number)
            thirdStep()
        if step == 3:
            global amount
            amount = int(number)
            finishStep()

    else:
        print("Введіть будь ласка ціле число!")
        if step == 1:
            firstStep()
        if step == 2:
            secondStep()
        if step == 3:
            thirdStep()


firstStep()
