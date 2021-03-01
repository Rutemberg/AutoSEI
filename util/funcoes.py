def menu(os, *args):
    os.system("cls")
    print(f"\nAUTOSEI\n\n")
    for key, item in enumerate(args):
        print(f"{key+1}. {item}")
    print(f"\n{len(args)+1}. Sair\n\n\n")
