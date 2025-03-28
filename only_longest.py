import matplotlib.pyplot as plt
import numpy as np

f = 2.39

_lambda = 300/f

c = 500

s = 4/3

dec = 11

a_best = 0
P_best = 0

def Calc(a, mi):
    global P_best, a_best, dec
    b = s*a
    d = (a**2+b**2)**0.5

    r = _lambda/4

    mi_a = a/d*mi
    mi_b = b/d*mi

    n1 = np.ceil((2*r)/(d+mi))
    n2 = np.ceil((2*r)/(a+mi_a))
    n3 = np.ceil((2*r)/(b+mi_b))

    n = max(n1, n2, n3)

    A = 20*np.log10(_lambda/(2*d))-10*np.log10(n)

    cols = np.floor(c/(b+mi_b))
    rows = np.floor(c/(a+mi_a))

    rem_a = c - rows*(a+mi_a) + mi_a
    rem_b = c - cols*(b+mi_b) + mi_b

    P1 = cols*rows*a*b 

    if(P1 > P_best and A >= dec):
        P_best = P1
        a_best = a

    P2 = c**2

    P3 = P1/P2*100

    #print(P1, P2, P3)

    return np.array([A, P3, n, a, b, mi_a, mi_b, cols, rows, rem_a, rem_b])


def draw(a, b, mi_a, mi_b, cols, rows, rem_a, rem_b):

    ax = plt.subplot(1, 2, 2)

    # Tworzenie rysunku
    #fig, ax = plt.subplots(figsize=(5, 5))

    # Rysowanie siatki prostokątów
    for i in range(cols):
        for j in range(rows):
            x = i * (mi_b+b) + rem_b/2
            y = j * (mi_a+a) + rem_a/2
            rect = plt.Rectangle((x, y), b, a, edgecolor='black', facecolor='none', linewidth=1)
            ax.add_patch(rect)

    # Ustawienie granic osi
    ax.set_xlim(0, c)
    ax.set_ylim(0, c)

    circle = plt.Circle((_lambda/2, _lambda/2), _lambda/4, color='red', fill=False, linewidth=1)
    ax.add_patch(circle)

    ax.set_aspect('equal')  # Zachowanie proporcji
    plt.show()


def longest():
    print(f'Projekt przesłony o zadanych parametrach')
    print("Figura: Prostokąt 3:4")
    print(f'Częstotliwość: {f} GHz')
    print(f'Lambda: {_lambda} mm')
    print(f'Minimalne tłumienie: {dec} dB')

    mi = _lambda/10
    print(f'Odstęp po skosie: {mi}')
    print(f'Rozmiar płyty: {c} mm x {c} mm')

    

    x = np.linspace(_lambda/50, _lambda/2, 1000)

    res = np.array([Calc(e, mi) for e in x])
    A = res[:,0]
    P3 = res[:,1]
    n = res[:,2]

    print(f'Najlepsza długość boku A: {a_best}')
    print(f'Najlepsza przekątna: {a_best*5/3}')
    print(f'Najlepsze pole: {P_best}')
    
    plt.subplot(3, 2, 1)
    plt.title("A")
    plt.plot(x, A)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axhline(y=11, color='y', linestyle='-', linewidth=2)
    

    plt.subplot(3, 2, 3)
    plt.title("P3")
    plt.plot(x, P3)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)

    plt.subplot(3, 2, 5)
    plt.title("n")
    plt.plot(x, n)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)

    best_res = Calc(a_best, mi)
    print(best_res)

    #plt.show()

    draw(best_res[3], best_res[4], best_res[5], best_res[6], int(best_res[7]), int(best_res[8]), best_res[9], best_res[10])



