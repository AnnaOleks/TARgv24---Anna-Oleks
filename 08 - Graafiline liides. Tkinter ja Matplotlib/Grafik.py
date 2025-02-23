import numpy as np
import matplotlib.pyplot as plt

def grafik(a,b,c):
    plt.figure(facecolor="slategray")
    D=b**2-4*a*c
    x=np.linspace(-10, 10, 400)
    y=a*x**2+b*x+c
    plt.plot(x,y,label=f"{a}x² + {b}x + {c}", color="slategray", linestyle="-", marker="*", linewidth=0.5)
    if D>0:
        x1=(-b+np.sqrt(D))/(2 * a)
        x2=(-b-np.sqrt(D))/(2*a)
        plt.scatter([x1, x2], [0, 0], color='black', zorder=5)
    elif D==0:
        x=-b/(2*a)
        plt.scatter(x, 0, color='black', zorder=5)
    else:
        plt.text(0, 0, "Нет корней", fontsize=12, color='black', ha='center')
    
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.title(f"График функции {a}x² + {b}x + {c}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    
    plt.show()