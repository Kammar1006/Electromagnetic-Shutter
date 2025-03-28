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

    n = np.ceil((2*r+mi)/(d+mi))

    A = 20*np.log10(_lambda/(2*d)) #-10*np.log10(n)

    #print(a, b, d, n, A)

    ami = a/d*mi
    bmi = b/d*mi

    k = np.floor(c/(b+bmi))
    m = np.floor(c/(a+ami))
    P1 = k*m*a*b 

    if(P1 > P_best and A >= dec):
        P_best = P1
        a_best = a

    P2 = c**2

    P3 = P1/P2*100

    #print(P1, P2, P3)

    return [A, P3, n]


if __name__ == "__main__":
    print(f'Projekt przesłony o zadanych parametrach')
    print("Figura: Prostokąt 3:4")
    print(f'Częstotliwość: {f} GHz')
    print(f'Lambda: {_lambda} mm')
    print(f'Minimalne tłumienie: {dec} dB')

    mi = _lambda/10
    print(f'Odstęp po skosie: {mi}')
    print(f'Rozmiar płyty: {c} mm x {c} mm')

    

    x = np.linspace(_lambda/20, _lambda/2, 1000)

    res = np.array([Calc(e, mi) for e in x])
    A = res[:,0]
    P3 = res[:,1]
    n = res[:,2]

    print(f'Najlepsza długość boku: {a_best}')
    print(f'Najlepsze pole: {P_best}')

    
    plt.subplot(3, 1, 1)
    plt.title("A")
    plt.plot(x, A)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axhline(y=11, color='y', linestyle='-', linewidth=2)
    

    plt.subplot(3, 1, 2)
    plt.title("P3")
    plt.plot(x, P3)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)

    plt.subplot(3, 1, 3)
    plt.title("n")
    plt.plot(x, n)
    plt.axvline(x=a_best, color='g', linestyle='-', linewidth=1)
    plt.axvline(x=mi, color='r', linestyle='-', linewidth=1)
    plt.show()



