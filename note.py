import time
import pickle

choice = 0
notes = "notes.dat"

try:
    file = open(notes, 'rb')
except Exception:
    print("Error in file, creating new notes.dat.")
    open(notes, 'wb').close()
    file = open(notes, 'rb')

try:
    texts = pickle.load(file)
except Exception:
    texts = []

file.close()

while choice != 5:
    choice = int(input(
        "(1) Raed notes\n(2) Add a note\n(3) Change a note\n(4) Remove a note\n(5) Save and Quit\n\What you want to do?: "))
    if choice == 1:
        for i in texts:
            print(i)
        pass
    elif choice == 2:
        text = input("Write a new note: ")
        text = text + ":::" + time.strftime("%X %x")
        texts.append(text)
        pass
    elif choice == 3:
        print("List has", len(texts), "notes.")
        item = int(input("Which one you want to change?: "))
        print(texts[item-1])
        text = input("Write a new text: ")
        text = text + ":::" + time.strftime("%X %x")
        texts[item-1] = text
        pass
    elif choice == 4:
        print("List has", len(texts), "notes.")
        item = int(input("Which one you want to remove?: "))
        removed = texts.pop(item-1)
        print("Removed note", removed)
        pass
    elif choice == 5:
        print("Quitting.")
        file = open(notes, 'wb')
        pickle.dump(texts, file)
        file.close()
        pass
    else:
        print("Unknown choice.")
        pass
