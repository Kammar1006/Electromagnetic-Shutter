import matplotlib.pyplot as plt
import numpy as np

f = 2.39

_lambda = 300/f

c = 500

s = 4/3

dec = 11

mi = _lambda/10

a_best = 0
P_best = 0

def Calc(a):
    global P_best, a_best, dec
    b = s*a
    d = (a**2+b**2)**0.5

    r = _lambda/4

    mi_a = a/d*mi
    mi_b = b/d*mi

    n1 = np.ceil((2*r)/(d+mi*2**0.5))
    n2 = np.ceil((2*r)/(a+mi))
    n3 = np.ceil((2*r)/(b+mi))

    n = max(n1, n2, n3)

    A = 20*np.log10(_lambda/(2*d))-10*np.log10(n)

    cols = np.floor(c/(b+mi))
    rows = np.floor(c/(a+mi))

    rem_a = c - rows*(a+mi) + mi
    rem_b = c - cols*(b+mi) + mi

    P1 = cols*rows*a*b 

    if(P1 > P_best and A >= dec):
        P_best = P1
        a_best = a

    P2 = c**2

    P3 = P1/P2*100

    #print(P1, P2, P3)

    return np.array([A, P3, n, a, b, cols, rows, rem_a, rem_b])


def draw(a, b, cols, rows, rem_a, rem_b):

    ax = plt.subplot(1, 2, 2)
    plt.title("Przesłona")

    # Tworzenie rysunku
    #fig, ax = plt.subplots(figsize=(5, 5))

    # Rysowanie siatki prostokątów
    for i in range(cols):
        for j in range(rows):
            x = i * (mi+b) + rem_b/2
            y = j * (mi+a) + rem_a/2
            rect = plt.Rectangle((x, y), b, a, edgecolor='black', facecolor='none', linewidth=1)
            ax.add_patch(rect)

    # Ustawienie granic osi
    ax.set_xlim(0, c)
    ax.set_ylim(0, c)

    circle = plt.Circle((_lambda/2+10, _lambda/2), _lambda/4, color='red', fill=False, linewidth=1)
    ax.add_patch(circle)
    circle = plt.Circle((_lambda/2+100, _lambda/2), _lambda/4, color='red', fill=False, linewidth=1)
    ax.add_patch(circle)

    ax.set_aspect('equal')  # Zachowanie proporcji
    plt.show()


def same():
    print(f'Projekt przesłony o zadanych parametrach')
    print("Figura: Prostokąt 3:4")
    print(f'Częstotliwość: {f} GHz')
    print(f'Lambda: {_lambda} mm')
    print(f'Minimalne tłumienie: {dec} dB')

    
    print(f'Odstęp po skosie: {mi}')
    print(f'Rozmiar płyty: {c} mm x {c} mm')

    

    x = np.linspace(_lambda/50, _lambda/2, 1000)

    res = np.array([Calc(e) for e in x])
    A = res[:,0]
    P3 = res[:,1]
    n = res[:,2]

    print(f'Najlepsza długość boku A: {a_best}')
    print(f'Najlepsza przekątna: {a_best*5/3}')
    print(f'Najlepsze pole: {P_best}')
    
    plt.subplot(3, 2, 1)
    plt.title("Tłumienie w funkcji długości boku")
    plt.plot(x, A)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axhline(y=11, color='y', linestyle='-', linewidth=2)
    plt.xlabel("Długość krótszego boku [mm]")
    plt.ylabel("Tłumienie [dB]")
    

    plt.subplot(3, 2, 3)
    plt.title("Stosunek Pól: Otworów do całości przesłony")
    plt.plot(x, P3)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)
    plt.ylabel("Stosunek Pól [%]")
    plt.xlabel("Długość krótszego boku [mm]")

    plt.subplot(3, 2, 5)
    plt.title("Liczba otworów w lambda/2")
    plt.plot(x, n)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)
    plt.ylabel("Liczba otworów")
    plt.xlabel("Długość krótszego boku [mm]")

    plt.tight_layout()

    best_res = Calc(a_best)
    print(best_res)

    #plt.show()

    draw(best_res[3], best_res[4], int(best_res[5]), int(best_res[6]), best_res[7], best_res[8])



