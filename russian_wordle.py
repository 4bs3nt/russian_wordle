import random
from tkinter import *

attempts = 5

def check_word(user_word):
    global attempts

    if len(user_word) != 5:
        secrt.config(text="Ошибка! Слово не из 5 букв")
        return

    elif attempts > 0:
        attempts -= 1
        attempts_show.config(text = f"Кол-во попыток: {attempts}")

        user_letters = []

        for user_letter in user_word:
            user_letters.append(user_letter)

        for i in range(len(user_letters)):

            if user_letters[i] == letters[i]:
                secret_word[i] = user_letters[i]

            secrt.config(text = " ".join(secret_word))

        if "".join(secret_word) == target_word:
            win_label = Label(game, text="ТЫ ПОБЕДИЛ!", font="Arial, 20")
            win_label.pack()
            check_button.config(state=DISABLED)

    else:
        check_button.config(state=DISABLED)
        lose_label = Label(game, text="ТЫ ПРОИГРАЛ!", font="Arial, 20")
        lose_label.pack()



word_list = [
    "столб", "парус", "земля", "сахар", "носки", "книга", "ручка", "мосты", "пламя",
    "песок", "сфера", "почка", "трава", "лукав", "дымка", "брево", "камин", "други",
    "город", "лампа", "крыло", "зебра", "рыбак", "яблок", "врата", "света", "линия",
    "мосты", "птица", "почка", "грибок", "рыжик", "дверь", "ледок", "пенья", "скала",
    "квант", "крепь", "ложка", "молва", "сумка", "школа", "ткань", "дымка", "бродя",
    "копье", "пулял", "рысью", "груша", "знойя", "сенья", "вешка", "листя", "толпа",
    "песец", "кожаь", "ручей", "сарай", "шарик", "бочка", "зимаа", "птица", "кустик"
]

target_word = random.choice(word_list)

print(target_word)

letters = []

for letter in target_word:
    letters.append(letter)

secret_word_layout = "__ __ __ __ __"
secret_word = secret_word_layout.split(" ")


game = Tk()
game.title("Угадай слово!")
game.geometry("1000x600")

secrt = Label(game, text=" ".join(secret_word), font="Arial, 20")
secrt.pack(anchor=N)

input_word = Entry(game)
input_word.pack(anchor=CENTER)

check_button = Button(game,text="Проверить слово",width=15,height=1, command=lambda: check_word(input_word.get()))
check_button.pack()

attempts_show = Label(game,text=f"Кол-во попыток: {5}", font="Arial, 20")
attempts_show.pack()

game.mainloop()






