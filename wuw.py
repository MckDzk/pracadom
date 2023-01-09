from otw import Uczen

Uczen1 = Uczen("Adam", "Igor", "Czapla", "2B", 17,2,3,5,4,2,1, "biol/chem/fiz", 24, "jazda na deskorolce")
Uczen2 = Uczen("Jacek", "Wlodzimierz", "Jarząbek", "1D",15,4,2,5,1,3,4 , "Mat/Geo/Fiz", 19, "Zabawa w chowanego")
Uczen3 = Uczen("Dawid", "Sebastian", "Świerk", "4C",18,3,2,1,1,5,3, "Hist/Wos/J.Pol", 25, "Gra w szachy")
Uczen4 = Uczen("Kacper", "Edmund", "Biedronka",'1E',14, 1,1,2,2,3,5, "J.ang/Wos/J.niem", 15, "Gotowanie")
Uczen5 = Uczen("Basia", "Angelika", "Skowronek","3C",17, 5,4,5,3,5,4, "Hist/Wos/J.Pol", 18, "Balet")
Uczen6 = Uczen("Pawel", "Angelika", "Strzelecki","4A",19,4,4,5,5,5,2, "mat/fiz/inf", 4, "strzelanie do rzutek")
Uczen7 = Uczen("Damian", "Angelika", "Kruk","2G",16,3,1,2,2,2,3, "ang/pol/mat", 7, "lucznictwo")

Uczen1.imie = "Adam"
Uczen1.drugie_imie_po_zmarlej_prababce = "Igor"
Uczen1.nazwisko = "Czapla"
Uczen1.klasa = '2B'
Uczen1.wiek = 17
Uczen1.ocena_zachowanie = 2
Uczen1.ocena_fiz = 3
Uczen1.ocena_mat = 5
Uczen1.ocena_inf = 4
Uczen1.ocena_pol = 2
Uczen1.ocena_ang = 1
Uczen1.profil_klasy = "biol/chem/fiz"
Uczen1.l_uczniowklasy = 24
Uczen1.hobby = "jazda na deskorolce"



Uczen2.imie = "Jacek"
Uczen2.drugie_imie_po_zmarlej_prababce = "Wlodzimierz"
Uczen2.nazwisko = "Jarząbek"
Uczen2.klasa = '1D'
Uczen2.wiek = 15
Uczen2.ocena_zachowanie = 4
Uczen2.ocena_fiz = 2
Uczen2.ocena_mat = 5
Uczen2.ocena_inf = 1
Uczen2.ocena_pol = 3
Uczen2.ocena_ang = 4
Uczen2.profil_klasy = "Mat/Geo/Fiz"
Uczen2.l_uczniowklasy = 19
Uczen2.hobby = "Zabawa w chowanego"



Uczen3.imie = "Dawid"
Uczen3.drugie_imie_po_zmarlej_prababce = "Sebastian"
Uczen3.nazwisko = "Świerk"
Uczen3.klasa = '4C'
Uczen3.wiek = 18
Uczen3.ocena_zachowanie = 3
Uczen3.ocena_fiz = 2
Uczen3.ocena_mat = 1
Uczen3.ocena_inf = 1
Uczen3.ocena_pol = 5
Uczen3.ocena_ang = 3
Uczen3.profil_klasy = "Hist/Wos/J.Pol"
Uczen3.l_uczniowklasy = 25
Uczen3.hobby = "Gra w szachy"


Uczen4.imie = "Kacper"
Uczen4.drugie_imie_po_zmarlej_prababce = "Edmund"
Uczen4.nazwisko = "Biedronka"
Uczen4.klasa = '1E'
Uczen4.wiek = 14
Uczen4.ocena_zachowanie = 1
Uczen4.ocena_fiz = 1
Uczen4.ocena_mat = 2
Uczen4.ocena_inf = 2
Uczen4.ocena_pol = 3
Uczen4.ocena_ang = 5
Uczen4.profil_klasy = "J.ang/Wos/J.niem"
Uczen4.l_uczniowklasy = 15
Uczen4.hobby = "Gotowanie"


Uczen5.imie = "Basia"
Uczen5.nazwisko = "Skowronek"
Uczen5.klasa = '3C'
Uczen5.wiek = 17
Uczen5.ocena_zachowanie = 5
Uczen5.ocena_fiz = 4
Uczen5.ocena_mat = 5
Uczen5.ocena_inf = 3
Uczen5.ocena_pol = 5
Uczen5.ocena_ang = 4
Uczen5.profil_klasy = "Hist/Wos/J.Pol"
Uczen5.l_uczniowklasy = 18
Uczen5.hobby = "Balet"


Uczen6.imie = "Pawel"
Uczen6.nazwisko = "Strzelecki"
Uczen6.klasa = '4A'
Uczen6.wiek = 19
Uczen6.ocena_zachowanie = 4
Uczen6.ocena_fiz = 4
Uczen6.ocena_mat = 5
Uczen6.ocena_inf = 5
Uczen6.ocena_pol = 5
Uczen6.ocena_ang = 2
Uczen6.profil_klasy = "mat/fiz/inf"
Uczen6.l_uczniowklasy = 3
Uczen6.hobby = "strzelanie do rzutek"



Uczen7.imie = "Damian"
Uczen7.nazwisko = "Kruk"
Uczen7.klasa = '2G'
Uczen7.wiek = 16
Uczen7.ocena_zachowanie = 3
Uczen7.ocena_fiz = 1
Uczen7.ocena_mat = 2
Uczen7.ocena_inf = 2
Uczen7.ocena_pol = 2
Uczen7.ocena_ang = 3
Uczen7.profil_klasy = "ang/pol/mat"
Uczen7.l_uczniowklasy = 7
Uczen7.hobby = "lucznictwo"


lista_u = [Uczen1, Uczen2, Uczen3, Uczen4, Uczen5, Uczen6, Uczen7]

for u in lista_u:
    u.imiee()
    u.drugieimiepozmarlejprababce()
    u.nazwiskoo()
    u.wiekk()
    u.zdawalnosc()
    u.ocenyfiz()
    u.ocenymat()
    u.ocenyinf()
    u.ocenypol()
    u.ocenyang()
    u.liczbauczniowklasy()
    u.rozszerzenia()
    u.hobbyt()