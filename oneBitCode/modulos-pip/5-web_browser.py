import webbrowser

DONE = False

while DONE is False:
    print("Oque você deseja fazer?")
    print("1. Aprender Python")
    print("2. Aprender sobre módulos")
    print("3. Aprender Python, Fullstack JS, Inglês e No Code")
    print("4. Sair")
    
    choice = input("> ")
    
    if choice == "1":
        webbrowser.open("http://www.python.org")
    elif choice == "2":
        webbrowser.open("https://docs.python.org/3/py-modindex.html")
    elif choice == "3":
        webbrowser.open("https://pages.onebitcode.com/")
    elif choice == "4":
        DONE = True
    else:
        print("Opção inválida Escolha uma opção entre 1 e 4")