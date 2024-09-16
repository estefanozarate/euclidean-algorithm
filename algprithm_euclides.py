import argparse
from termcolor import colored 
import time


title_euclidean = """
    ______           ___     __                    
   / ____/_  _______/ (_)___/ /__  ____ _____      
  / __/ / / / / ___/ / / __  / _ \/ __ `/ __ \     
 / /___/ /_/ / /__/ / / /_/ /  __/ /_/ / / / /     
/_____/\__,_/\___/_/_/\__,_/\___/\__,_/_/ /_/     
    ___    __                 _ __  __            
   /   |  / /___ _____  _____(_) /_/ /_  ____ ___ 
  / /| | / / __ `/ __ \/ ___/ / __/ __ \/ __ `__\\
 / ___ |/ / /_/ / /_/ / /  / / /_/ / / / / / / / /
/_/  |_/_/\__, /\____/_/  /_/\__/_/ /_/_/ /_/ /_/ 
         /____/                                   
                                                   
"""

def print_title(title_euclidean=title_euclidean,)-> None:
    time.sleep(0.2)
    print(colored(title_euclidean, "green"))
    print("\n")
    time.sleep(0.9)
    print(colored("Github: @estefanozarate"))



def get_arguments():
    parser = argparse.ArgumentParser(description="MCD(A,B) = Ax + By")
    parser.add_argument("-a", dest="a", required=True, help = "[?] Valor A en la funcion MCD(A,B) ")
    parser.add_argument("-b", dest="b", required=True, help="[?] Valor de B en la funcion MCD(A,B)")
    options = parser.parse_args()
    return options.a, options.b

def compare_ab(a,b) -> tuple:
    if a < b:
        temp = a
        a = b 
        b = temp
        return (a,b)
    else:
        return (a,b) 

def mcd_euclides_algorithm(a, b):
    _a, _b = compare_ab(a,b)
    while _b != 0:
        r = _a % _b
        _a = _b 
        _b = r
    return _a

def mcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        mcd, x1, y1 = mcd_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return mcd, x, y
 

if __name__ == "__main__":
    print_title()
    a_str,b_str = get_arguments()
    a = int(a_str)
    b = int(b_str)


    mcd_a_b = mcd_euclides_algorithm(a, b)

    time.sleep(1.3)
    print(colored(f"Valores ingresados:", "blue"))
    time.sleep(1.3)
    print(f"a: {a}")
    time.sleep(0.7)
    print(f"b: {b}")
    time.sleep(1.1)
    print(colored(f"Calculando el MCD({a}, {b})"))
    time.sleep(0.9)
    print(colored("Calculando...", "red"))
    time.sleep(0.9)
    print(colored("Calculando...", "red"))
    time.sleep(0.4)
    print(colored(f"MCD({a},{b}) = {mcd_a_b}", "yellow"))
    print(colored("Representando el MCD como una combinacion lineal de la siguiente forma...", "light_green"))
    time.sleep(0.1)
    mcd, x, y = mcd_extended(a,b)
    print(colored(f"MCD({a}, {b}) = aX + bY", "blue"))
    time.sleep(0.1)
    print(colored(f"MCD({a}, {b}) = {a}({x}) + {b}({y})", "light_blue"))


