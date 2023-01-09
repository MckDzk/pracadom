class Uczen():
    imie = ''
    drugie_imie_po_zmarlej_prababce = ''
    nazwisko = ''
    klasa = ''
    wiek = None
    ocena_zachowanie = None
    ocena_fiz = None
    ocena_mat = None
    ocena_inf = None
    ocena_pol = None
    ocena_ang = None
    profil_klasy = ''
    l_uczniowklasy = None
    hobby = ''


    def __init__(self, i, dipzp, n, k, w, oz, of, om, oi, op, oa, pk, luk, h):
        self.imie = i
        self.drugie_imie_po_zmarlej_prababce = dipzp
        self.naziwsko = n
        self.klasa = k
        self.wiek = w
        self.ocena_zachowanie = oz
        self.ocena_fiz = of
        self.ocena_mat = om 
        self.ocena_inf = oi 
        self.ocena_pol = op 
        self.ocena_ang = oa
        self.profil_klasy = pk
        self.l_uczniowklasy = luk
        self.hobby = h

    
    def imiee(self):
        print(self.imie) 

    def drugieimiepozmarlejprababce(self):
        print(self.drugie_imie_po_zmarlej_prababce)

    def nazwiskoo(self):
        print(self.naziwsko)

    def klasaa(self):
        print(self.klasa)

    def wiekk(self):
        print(self.wiek)


    def  zdawalnosc(self):
        if self.ocena_zachowanie == 1:
            print("zachowanie - ocena niedostateczna")
        elif self.ocena_zachowanie == 2:
            print("zachowanie - ocena dopusczajaca")
        elif self.ocena_zachowanie == 3:
            print("zachowanie - ocena poprawna")
        elif self.ocena_zachowanie == 4:
            print("zachowanie - ocena dobra")
        elif self.ocena_zachowanie == 5:
            print("zachowanie - ocena b.dobra")
        elif self.ocena_zachowanie == 6:
            print("zachowanie - ocena wzorowa")
        else:
            print("blad - wpisano zla ocene")

    def  ocenyfiz(self):
        if self.ocena_fiz == 1:
            print("fizyka - ocena niedostateczna")
        elif self.ocena_fiz == 2:
            print("fizyka - ocena dopusczajaca")
        elif self.ocena_fiz == 3:
            print("fizyka - ocena poprawna")
        elif self.ocena_fiz == 4:
            print("fizyka - ocena dobra")
        elif self.ocena_fiz == 5:
            print("fizyka - ocena b.dobra")
        elif self.ocena_fiz == 6:
            print("fizyka - ocena wzorowa")
        else:
            print("blad - wpisano zla ocene")


    def  ocenymat(self):
        if self.ocena_mat == 1:
            print("matematyka - ocena niedostateczna")
        elif self.ocena_mat == 2:
            print("matematyka - ocena dopusczajaca")
        elif self.ocena_mat == 3:
            print("matematyka - ocena poprawna")
        elif self.ocena_mat == 4:
            print("matematyka - ocena dobra")
        elif self.ocena_mat == 5:
            print("matematyka - ocena b.dobra")
        elif self.ocena_mat == 6:
            print("matematyka - ocena wzorowa")
        else:
            print("blad - wpisano zla ocene")

    def  ocenyinf(self):
        if self.ocena_inf == 1:
            print("informatyka - ocena niedostateczna")
        elif self.ocena_inf == 2:
            print("informatyka  - ocena dopusczajaca")
        elif self.ocena_inf == 3:
            print("informatyka  - ocena poprawna")
        elif self.ocena_inf == 4:
            print("informatyka  - ocena dobra")
        elif self.ocena_inf == 5:
            print("informatyka  - ocena b.dobra")
        elif self.ocena_inf == 6:
            print("informatyka  - ocena wzorowa")
        else:
            print("blad - wpisano zla ocene")


    def  ocenypol(self):
        if self.ocena_pol == 1:
            print("polski - ocena niedostateczna")
        elif self.ocena_pol == 2:
            print("polski  - ocena dopusczajaca")
        elif self.ocena_pol == 3:
            print("polski  - ocena poprawna")
        elif self.ocena_pol == 4:
            print("polski  - ocena dobra")
        elif self.ocena_pol == 5:
            print("polski  - ocena b.dobra")
        elif self.ocena_pol == 6:
            print("polski  - ocena wzorowa")
        else:
            print("blad - wpisano zla ocene")

    def  ocenyang(self):
        if self.ocena_ang == 1:
            print("angielski - ocena niedostateczna")
        elif self.ocena_ang == 2:
            print("angielski  - ocena dopusczajaca")
        elif self.ocena_ang == 3:
            print("angielski  - ocena poprawna")
        elif self.ocena_ang == 4:
            print("angielski  - ocena dobra")
        elif self.ocena_ang == 5:
            print("angielski  - ocena b.dobra")
        elif self.ocena_ang == 6:
            print("angielski  - ocena wzorowa")
        else:
            print("blad - wpisano zla ocene")


    def rozszerzenia(self):
        print( self.profil_klasy)

    
    def liczbauczniowklasy(self):
        print(self.l_uczniowklasy)
    
    def hobbyt(self):
        print(self.hobby)

