
# (1)
import math


def arithmetic(arv1:float, arv2:float, tehe:str)->any:
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: Sisend kasutajalt, mingi ujukomaarv
    :param float arv2: Sisend kasutajalt, mingi ujukomaarv
    :param str tehe: Sisend aritmeetiline tehe, mis valib kasutaja
    :rtype: Määrata tüüp(float või str)
    """
    if tehe in ["+", "-", "*", "/"]:
        if arv2 == 0 and tehe == "/":
            vastus = "DIV/0"
        else:
            vastus = eval(str(arv1) + tehe + str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

# (2)
def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasta ja False kui on tavaline aasta.
    :param int aasta: aasta number,
    :rtype: bool tagastab tõeväärtuses formaadis tulemus
    """
    return aasta % 4 == 0

# (3)
def square(kulg:float)->any:
    """Ruudu pindala, perimeeter ja diagonaal leidmine
    Tagastab 3 numberid
    :param kulg float: Ruudu külje suurus
    :rtype: Kolm float numberid
    """
    S = kulg ** 2
    P = kulg * 4
    d = math.sqrt(2) * kulg
    return S, P, d

# (3)
def square_list(kulg:float)->list:
    """Ruudu pindala, perimeeter ja diagonaal leidmine
    Tagastab 3 numberid
    :param kulg float: Ruudu külje suurus
    :rtype: List milles on kolm elemendid mille tüüp on float
    """
    S = kulg ** 2
    P = kulg * 4
    d = math.sqrt(2) * kulg
    s_list = [S, P, d]
    return s_list

# (4)
def season(month:int)->str:
    """Aastaaja leidmine
    Tagastab aastaaja nime
    :param int month: Kuu number
    :rtype: str tagastab aastaaja nime
    """
    if month in [12, 1, 2]:
        return "Talv"
    elif month in [3, 4, 5]:
        return "Kevad"
    elif month in [6, 7, 8]:
        return "Suvi"
    elif month in [9, 10, 11]:
        return "Sügis"
    else:
        return "Tundmatu kuu"

# (4) 2
def seasonInput()->str:
    """Aastaaja leidmine
    Tagastab aastaaja nime
    :rtype: str tagastab aastaaja nime
    """
    k = int(input("Sisesta kuu number: "))
    while True:
        if k in range(1, 13):
            break
        else:
            k = int(input("Sisesta kuu number: "))
    return season(k)

# (5)
def bank(a:float, years:int)->float:
    """Pangas raha kasvamine
    Tagastab raha summa pärast aastate möödumist
    :param float a: Sisend kasutajalt, mingi täisarv
    :param int years: Sisend kasutajalt, mingi täisarv
    :rtype: float tagastab raha summa pärast aastate möödumist
    """
    a *= math.pow(1.1, years)
    return a

# (6)
def is_prime(a:int)->bool:
    """Kontrollib kas arv on algarv või mitte
    Tagastab True, kui arv on algarv ja False kui ei ole algarv.
    Ainult töötab arvetega 1-1000!
    :param int a: Sisend kasutajalt, mingi täisarv
    :rtype: bool tagastab tõeväärtuses formaadis tulemus
    """
    if (a < 1 or a > 1000):
        return False

    if (a == 1):
        return True

    for i in range(2, a):
        if (a % i == 0):
            return False

    return True

# (8)
def xorCipher(word:str, key:str)->str:
    """XOR krüpteerimine
    Tagastab krüpteeritud sõna
    :param str word: Sisend kasutajalt, mingi sõna
    :param str key: Sisend kasutajalt, mingi võti
    :rtype: str tagastab krüpteeritud sõna
    """
    crypt = ""
    for i in range(len(word)):
        crypt += chr(ord(word[i]) ^ ord(key[i % len(key)]))
    return crypt

def xorUncipher(word:str, key:str)->str:
    """XOR de-krüpteerimine
    Tagastab de-krüpteeritud sõna
    :param str word: Sõna mis only XOR krüpteeritud
    :param str key: Võti mis kasutati XOR krüpteerimiseks
    :rtype: str tagastab krüpteeritud sõna
    """
    return xorCipher(word, key)

    