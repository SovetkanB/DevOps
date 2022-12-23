import random

def compChoise():
    computer_choise = random.choice(["1", "2", "3"])
    return computer_choise

def winner(your_choise, computer_choise):
    if your_choise == "1" and computer_choise == "2":
        result = "Ты выйграл!"
        return result
    elif your_choise == "1" and computer_choise == "3":
        result = "Ты Проиграл(!"
        return result
    elif your_choise == "2" and computer_choise == "1":
        result = "Ты Проиграл(!"
        return result
    elif your_choise == "2" and computer_choise == "3":
        result = "Ты выйграл!"
        return result
    elif your_choise == "3" and computer_choise == "1":
        result = "Ты выйграл!"
        return result
    elif your_choise == "3" and computer_choise == "2":
        result = "Ты Проиграл("
        return result
    else:
        result = "Ничья"
        return result

print("1-Камень, 2-ножницы, 3-бумага")
choise = {"1":"Камень", "2":"Ножницы", "3":"Бумага"}

your_choise = input("Выберите номер: ")
print("Ваш выбор:", choise[your_choise])

computer_choise = compChoise()
print("Соперник выбрал:", choise[computer_choise])

print(winner(your_choise, computer_choise))
