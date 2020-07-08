import sys
from fractions import Fraction


class frac:
    bruch_1__priv: int
    bruch_2__priv: int
    zähler__priv: int
    nenner__priv: int

    def __init__(self, zähler, nenner):
        self.zähler: int = zähler
        self.nenner: int = nenner
        #Übergabe Instanzvraible an Klassenvariable
        frac.zähler = zähler
        frac.nenner = nenner

    def print_wert(self):
        bruch = Fraction(self.zähler, self.nenner)
        print("Der Wert des ersten Bruches beträgt", bruch)
        frac.bruch_1 = bruch

    def print_wert2(self):
        bruch_2 = Fraction(self.zähler, self.nenner)
        print("Der Wert des ersten Bruches beträgt", bruch_2)
        frac.bruch_2 = bruch_2
        frac.Operation_Entscheidung(self)


    def Operation_Entscheidung(self):
        additions_fragen = str(input("Wollen Sie die beiden Brüche addieren? "))
        if additions_fragen in ["true", "ja", "Ja", "yes", "Yes"]:
            frac.addation(self)
        else:
            multiply_frage = str(input("Wollen Sie die beiden Brüche Multiplizieren? "))
            if multiply_frage in ["true", "ja", "Ja", "yes", "Yes"]:
                frac.multiply(self)


    def addation(self):
        AdditionZweierBrüche = frac.bruch_1 + frac.bruch_2
        print()
        print("Die Adittion der zwei Brüche ist", Fraction(AdditionZweierBrüche))


    def multiply(self):
        MultiZweierBrüche = frac.bruch_1 * frac.bruch_2
        print()
        print("Die Multiplikation von zweier Brüche ist:", Fraction(MultiZweierBrüche))


# main
if __name__ == '__main__':
    try:
        input_zähler1 = int(input("Geben Sie ihren Zähler für den ersten Bruch ein: "))
        input_nenner1 = int(input("Geben Sie ihren Nenner für den ersten Bruch ein: "))
        input_zähler2 = int(input("Geben Sie ihren Zähler für den zweiten Bruch ein: "))
        input_nenner2 = int(input("Geben Sie ihren Nenner für den zweiten Bruch ein: "))
    except ValueError:
        print("Nur ganze Zahlen sind erlaubt! Bitte überprüfen sie Ihre Eingabe!")
    if input_nenner1 | input_nenner2 == 0:
        print("Der Nenner eines Bruches darf nicht null werden, dies ist nicht definiert!")
        sys.exit(0)

    Bruch_Obj = frac(input_zähler1, input_nenner1)
    Bruch_Obj2 = frac(input_zähler2, input_nenner2)
    Bruch_Obj.print_wert()
    Bruch_Obj2.print_wert2()


