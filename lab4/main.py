import numpy as np
import matplotlib.pyplot as plt


def euler_method(rh, c, h0, tmax, t0, dt, rc):

    print("Euler method calculating...")
    time_array = [t0]
    #vazos aukstis
    height_array = [h0]
    #cilindro aukstis
    height_array2 = [h0]
    #nustatomas pradinis aukstis
    h=h0
    h2=h0
    prec = 1e-3

    #naudojama surasti per kiek laiko isbega vanduo
    found_solution = False
    found_solution2 = False


    for t in np.arange(t0, tmax, dt):

        #formule pagal duota varianta
        Awh = get_Awh(h)
        dhdt = -(((c*rh**2*np.pi)*((2*9.8*h)**0.5).real)/(Awh))
        dhdt2 = -((c*rh**2)*((2*9.8*h2)**0.5).real/(rc**2))
        h = h + dt * dhdt
        h2 = h2 + dt * dhdt2

        if h <= prec and not found_solution:
            print(f"Visas vanduo (vazos) išbėgo per {t}s")
            found_solution = True

        if h2 <= prec and not found_solution2:
            print(f"Visas vanduo (cilindro) išbėgo per {t}s")
            found_solution2 = True

        height_array.append(h)
        height_array2.append(h2)
        time_array.append(t)
        if(found_solution and found_solution2):
            break

    #graph
    plt.plot(time_array,height_array, label="Vaza oileris")
    plt.plot(time_array, height_array2, label="Cilindras oileris")
    plt.legend()
    plt.xlabel("Laikas, s")
    plt.ylabel("Aukštis h, m")
    plt.show()




def get_Awh(H):

    return (43/400+np.cos(4*np.pi*H)/40)**2*np.pi

def runge_kutta_method(rh, c, h0, tmax, t0, dt, rc):

    print("Runge-Kutta method calculating...")

    time_array = [t0]
    # vazos aukstis
    height_array = [h0]
    # cilindro aukstis
    height_array2 = [h0]
    # nustatomas pradinis aukstis
    h = h0
    hh = h0
    prec = 1e-3

    # naudojama surasti per kiek laiko isbega vanduo
    found_solution = False
    found_solution2 = False

    for t in np.arange(t0, tmax, dt):

        Awh = get_Awh(h)
        dhdt = -(((c * rh ** 2 * np.pi) * ((2 * 9.8 * h) ** 0.5).real) / (Awh))
        dhdt2 = -((c * rh ** 2) * ((2 * 9.8 * hh) ** 0.5).real / (rc ** 2))
        f1 = dhdt
        ff1 = dhdt2

        h1 = h + dt / 2 * f1
        hh1 = hh + dt/2 * ff1
        Awh = get_Awh(h1)
        dhdt = -(((c * rh ** 2 * np.pi) * ((2 * 9.8 * h1) ** 0.5).real) / (Awh))
        dhdt2 = -((c * rh ** 2) * ((2 * 9.8 * hh1) ** 0.5).real / (rc ** 2))
        f2 = dhdt
        ff2= dhdt2

        h2 = h + dt / 2 * f2
        hh2 = hh + dt / 2 * ff2
        Awh = get_Awh(h2)
        dhdt = -(((c * rh ** 2 * np.pi) * ((2 * 9.8 * h2) ** 0.5).real) / (Awh))
        dhdt2 = -((c * rh ** 2) * ((2 * 9.8 * hh2) ** 0.5).real / (rc ** 2))
        f3 = dhdt
        ff3= dhdt2

        h3 = h + dt * f3
        hh3 =hh + dt * ff3
        Awh = get_Awh(h3)
        dhdt = -(((c * rh ** 2 * np.pi) * ((2 * 9.8 * h3) ** 0.5).real) / (Awh))
        dhdt2 = -((c * rh ** 2) * ((2 * 9.8 * hh3) ** 0.5).real / (rc ** 2))
        f4 = dhdt
        ff4 = dhdt2

        h = h + dt / 6 * (f1 + 2 * f2 + 2 * f3 + f4)
        hh = hh + dt / 6 * (ff1 + 2 * ff2 + 2 * ff3 + ff4)

        if h <= prec and not found_solution:
            print(f"Visas vanduo (vazos) išbėgo per {t}s")
            found_solution = True

        if hh <= prec and not found_solution2:
            print(f"Visas vanduo (cilindro) išbėgo per {t}s")
            found_solution2 = True

        time_array.append(t)
        height_array.append(h)
        height_array2.append(hh)

    plt.plot(time_array, height_array, label="Vaza Rungė ir Kuta")
    plt.plot(time_array, height_array2, label="Cilindras Rungė ir Kuta")
    plt.xlabel("Laikas, s")
    plt.ylabel("Aukštis h, m")
    plt.legend()
    plt.show()





if __name__ == '__main__':

    #skyles apacioje spindulys
    rh = 0.0075
    #proporcingumo daugiklis
    c = 0.6
    #laikas
    tmax = 120
    #pradinis skyscio aukstis talpoje
    h0 = 0.5
    #laiko pokycio zingsnis
    dt = 0.01
    #pradinis laiko momentas
    t0=0
    #cilindro spindulys
    rc = 0.1

    euler_method(rh, c, h0, tmax, t0, dt, rc)

    runge_kutta_method(rh, c, h0, tmax, t0, dt, rc)

