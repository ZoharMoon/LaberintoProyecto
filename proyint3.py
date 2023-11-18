import os
import sys
import time

def clear_and_print(num):
  
    os.system('cls' if os.name=='nt' else 'clear')

   
    print(num)

def main():
    num = 0

    while num <= 50:
       
        key = input("Presiona 'n' para continuar: ")
        if key.lower() == 'n':
            clear_and_print(num)
            num += 1
        else:
            print("Tecla no válida. Presiona 'n' para continuar.")

       
        time.sleep(0.5)

if __name__ == "__main__":
    main()
