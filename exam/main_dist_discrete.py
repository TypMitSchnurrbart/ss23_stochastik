"""

    Quick easy and OWN stat functions to compute the basics
    and therefore know what is happening in the exam

    author:     Alexander Mueller
    date:       29.03.2023
    version:    0.0.1

    Every function that is "[VERIFIED]" is checked
    to give the same results as b.staehle considers
    correct in her script!

    CDF when value is given; looking for probability
    PPF when probability is given; looking for value

"""

#===== IMPORTS =======================================
from scipy.stats import poisson, binom, geom, hypergeom, norm

#===== FUNCTIONS =====================================
if __name__ == "__main__":

    data = [1, 1, 1, 1, 2, 3, 3, 3]
    #data = [1, 1, 1, 2, 2, 2, 3, 3]

    ########################################
    # Wenn Rate gegeben und unabhängig zufällig
    # POISSON - Verteilung Po(X=versuche)
    rate = 1
    versuche = 0
    print(f"Po(X={versuche}) mit Rate {rate}  =\t{poisson.pmf(k=versuche, mu=rate)}")
    print(f"Po(X<={versuche}) mit Rate {rate} =\t{poisson.cdf(k=versuche, mu=rate)}")
    print(f"Po E(X) = {rate}")
    print(f"Po Var(X) = {rate}\n")

    ########################################
    # Wenn feste Anzahl versuche mit Erfolg oder nicht! p = const. 
    # Binominal - Bino(X=versuche)
    gesamt = 3
    p = 0.3
    k = 0
    target = 0.99
    print(f"Binom(X={k})  =\t{binom.pmf(k, gesamt, p)}")
    print(f"Binom(X<={k}) =\t{binom.cdf(k, gesamt, p)}")
    print(f"Binom(X_{target}) =\t{binom.ppf(target, gesamt, p)}")
    print(f"Binom E(X) = {gesamt*p}")
    print(f"Binom Var(X) = {gesamt*p*(1-p)}\n")


    ########################################
    # Wie lange bis etwas eintritt, unabhängig; zwei Möglichkeiten; Wie lange bis das erste...?
    # Geometrisch
    p = 0.7
    k = 1
    target = 0.9
    print(f"geom(X={k})  =\t{geom.pmf(k, p)}")
    print(f"geom(X<={k}) =\t{geom.cdf(k, p)}")
    print(f"geom(X_{target}) =\t{geom.ppf(target, p)}")
    print(f"geom E(X) = {1/p}")
    print(f"geom Var(X) = {(1-p) / (p**2)}\n")

    ########################################
    # Wenn zwei Gruppen gegeben; begrenzte Gesamheit ohne zurücklegen; Qualitätkontrollen
    # HYPERGeometrisch
    gesamt = 60    # Anzahl Tiere
    N = 10          # Davon 40 Hunde
    n = 3          # Anzahl ausgewählter Tiere
    k = 0           # Wahrscheinlichkeit 4 Hunde zu finden, wenn ich 12 ziehe aus 100 Tieren mit 40 Hunden
    print(f"hyper(X={k})  =\t{hypergeom.pmf(k, gesamt, N, n)}")
    print(f"hyper(X<={k}) =\t{hypergeom.cdf(k, gesamt, N, n)}")
    print(f"hyper E(X) = {n * N/gesamt}")
    print(f"hyper Var(X) = {n * N/gesamt * (1-N/gesamt) * (gesamt-n)/(gesamt-1)}\n")

    ########################################
    # Wenn normal verteilt. Also nur Erwartungswert und std angegeben!
    # NORM
    erwartung = 1200
    std = 111.8
    untere = 1000
    obere = 1000
    target = 0.05
    print(f"norm -> F({untere}) =\t{norm.cdf(untere, erwartung, std)}")
    print(f"norm -> F({obere}) =\t{norm.cdf(obere, erwartung, std)}")
    print(f"norm -> F(x_{target}) =\t{norm.ppf(target, erwartung, std)}")


