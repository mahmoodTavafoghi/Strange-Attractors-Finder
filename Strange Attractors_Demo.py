#######-This Program was written by M.Tavafoghi in winter 1401
#######-mahmood.tavafoghi@gmail.com

import matplotlib.pyplot as plt
from math import *


# ----------
def lyapunov_exponent(xar, yar, st):
    xe = 0.000001
    ye = 0
    lsum = 0
    cc = [((float("%.1f" % ((ord(q) - 65) * 0.1 - 1.2)))) for q in st]

    for i in range(len(xar) - 1):
        xesp = xar[i] + xe
        yesp = yar[i] + ye

        pe = cc[0] + cc[1] * xesp + cc[2] * (
            xesp**2) + cc[3] * xesp * yesp + cc[4] * yesp + cc[5] * (yesp**2)
        qe = cc[6] + cc[7] * xesp + cc[8] * (
            xesp**2) + cc[9] * xesp * yesp + cc[10] * yesp + cc[11] * (yesp**2)

        df = 10e12 * ((pe - xar[i + 1])**2 + (qe - yar[i + 1])**2)
        rs = 1 / sqrt(df)
        xe = (pe - xar[i + 1]) * rs
        ye = (qe - yar[i + 1]) * rs
        lsum += log(df)
        L = 0.721347 * lsum / (i + 1)

    return (L)


#-------------------
def cal_img(st):
    c = [((float("%.1f" % ((ord(q) - 65) * 0.1 - 1.2)))) for q in st]
    dx = []
    dy = []
    x = 0.05
    y = 0.05
    for i in range(100000):  ##Increase this range give u better image quality
        dx.append(x)
        dy.append(y)
        p = c[0] + c[1] * x + c[2] * (
            x**2) + c[3] * x * y + c[4] * y + c[5] * (y**2)
        q = c[6] + c[7] * x + c[8] * (
            x**2) + c[9] * x * y + c[10] * y + c[11] * (y**2)
        x = p
        y = q
    ll = lyapunov_exponent(dx, dy, st)
    return (dx, dy, st, ll)


#--------------------
def demo():
    DD = [
        'PMLKIGCSUGCQ', 'NBDVKBFLOJES', 'MKUJTDEMTUIU', 'KARVVSGOLMNX',
        'HVMALJJMUJEV', 'HMSUMMGMPATN', 'TUMJBRXRLDVN', 'OFVEQDMWKQFH',
        'SIFBCSGLPLXU', 'HAUGIWOOHAQC', 'UTDWWJLOOMMD', 'RCGKSRELRARX',
        'RCGKSRELRARX', 'UTDWWJLOOMMD', 'ICHSRULFNNDV', 'GVQUEUJKDHEL',
        'CVQKGHQTPHTE', 'FIRCDERRPVLD', 'GIIETPIQRRUL', 'GLXOESFTTPSV',
        'GXQSNSKEECTX', 'HGUHDPHNSGOH', 'ILIBVPKJWGRR', 'LUFBBFISGJYS',
        'MCRBIPOPHTBN', 'MDVAIDOYHYEA', 'ODGQCNXODNYA', 'QFFVSLMJJGCR',
        'UWACXDQIGKHF', 'SRAENVJFRUKP'
    ]

    mmtt = []
    for uu in DD:
        mmtt.append(cal_img(uu))

    plt.ion()
    figure, ax = plt.subplots()
    u = 0
    
    while (True):
        plot_1 = ax.scatter(mmtt[u][0],
                            mmtt[u][1],
                            c=mmtt[u][1],
                            s=0.008, ## This factor is size of Dots on screen u can change it.
                            marker='o',
                            cmap='gnuplot')
        ax.set_xlim(min(mmtt[u][0]) - 0.05, max(mmtt[u][0]) + 0.05)
        ax.set_ylim(min(mmtt[u][1]) - 0.05, max(mmtt[u][1]) + 0.05)
        plt.title("Strange Attractors     " + mmtt[u][2] + '    L= ' +
                  str("%.2f" % mmtt[u][3]))
        
        #plt.savefig(mmtt[u][2]) ## If u wanna to save plots comment out this line.
        plt.show()

        figure.canvas.draw_idle()
        plt.pause(0.1)
        plot_1.remove()
        u += 1
        u = u % len(DD)


# ---------------------

demo()
