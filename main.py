from lutadores import *

if __name__ == "__main__":
    popo = Boxeador('Popo')
    bambam = Boxeador('Bambam')
    popo.soco(bambam)
    print(popo)
    print(bambam)
    popo.gancho(bambam)
    print(popo)
    print(bambam)
    gracie = MMA('Royce Gracie')
    popo.cruzado(gracie)
    gracie.superman_punch(popo)
    gracie.chave_braco(popo)
    print(popo)
    print(gracie)