import sys


def savetofile(lista):
    out_file = open(sys.argv[1], "w")
    for cosa in lista:
        out_file.write(cosa + "\n")
    out_file.close()


def loadfromfile():
    in_file = open(sys.argv[1], "r")
    list = in_file.readlines()
    for i in range(0, len(list)):
        list[i] = list[i].replace("\n", "")
    in_file.close()
    return list


todo_list = loadfromfile()
while 1:
    choice = int(input("Cosa vuoi fare?\n"
                   "1)Aggiungi una cosa da fare\n"
                   "2)Rimuovi una cosa da fare\n"
                   "3)Vedi le cose da fare\n"
                   "4)Chiudi il programma\n"))

    if choice < 0 or choice > 4:
        print("Errore.")
        pass

    if choice == 1:
        new = input("Cosa vuoi aggiungere: ")
        todo_list.append(new)
    elif choice == 2:
        to_delete = input("Inserisci la cosa da cancellare: ")
        for cosa in todo_list:
            if to_delete in cosa:
                todo_list.remove(cosa)
    elif choice == 3:
        print(sorted(todo_list))
    elif choice == 4:
        savetofile(todo_list)
        exit(1)