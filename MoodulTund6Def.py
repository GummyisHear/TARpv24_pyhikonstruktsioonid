
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



    