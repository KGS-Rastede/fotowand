"""
Die Idee dieser Datei ist es, eine Fotowand aus 192 Fotos zu erstellen. Dabei sind immer
6 x 4 Bilder auf einer Seite:

1	2	3	4	5	6	| 7	    8	9	10	11	12	|13	    14	15	16	17	18	|19	    20	21	22	23	24
25	26	27	28	29	30	| 31	32	33	34	35	36	|37	    38	39	40	41	42	|43	    44	45	46	47	48
49	50	51	52	53	54	| 55	56	57	58	59	60	|61	    62	63	64	65	66	|67	    68	69	70	71	72
73	74	75	76	77	78	| 79	80	81	82	83	84	|85	    86	87	88	89	90	|91	    92	93	94	95	96
---------------------------------------------------------------------------------------------------
97	98	99	100	101	102	| 103	104	105	106	107	108	|109	110	111	112	113	114	|115	116	117	118	119	120
121	122	123	124	125	126	| 127	128	129	130	131	132	|133	134	135	136	137	138	|139	140	141	142	143	144
145	146	147	148	149	150	| 151	152	153	154	155	156	|157	158	159	160	161	162	|163	164	165	166	167	168
169	170	171	172	173	174	| 175	176	177	178	179	180	|181	182	183	184	185	186	|187	188	189	190	191	192

Das erste Bild mit ist also oben links auf der ersten Seite und das letzte Bild
ist ganz unten rechts auf der letzen Seite.


Ein gute Anleitung fuer das Erstellen von PDF-Dateien mit Formen und so weiter
ist hier zu finden
https://technicalmasterblog.wordpress.com/2019/08/08/creating-pdfs-with-pyfpdf-and-python/

So kann man zum Beispiel ein Rechteck mit

  pdf.rect(20, 20, 100, 50)

erstellen. 
Und Bilder kann man mit self.image('Dateiname.jpg, 8, 33) einfuegen
"""

import os
import csv

from fpdf import FPDF



kuerzel = [] #hier sind alle (bis zu 192) Kuerzel drin.


"""
Diese Methode liest die Kuerzel nach den Bilddateinamen ein. 
Das funktioniert und hat den Vorteil, dass das Dateisystem die Sortierung 
macht. Wir wollen aber Kontrolle ueber die Reihenfolge haben, 
zum Beispiel sollen die Referendare moeglicherweise hinten sein
oder die Hausmeister vorne. 
Daher ist diese Methode in dieser Form nicht notwendig. Der Code
funktioniert aber.
"""
def lese_kuerzel_ein_alt():
    #Praktischerweise sortiert das Dateisystem die Dateinamen
    #automatisch, so dass wir hier an der Reihenfolge
    #nichts mehr aendern muessen.
    with os.scandir("fotos") as it:
        for entry in it:
            # if not entry.name.startswith('.') and entry.is_file():
            if entry.name.endswith('.jpg') and entry.is_file():
                #print(entry.name.split(".")[0])
                dateiname = entry.name.split(".")[0]
                if not dateiname == "texte":
                    kuerzel.append( dateiname )     

"""
Diese Methode oeffnet die CSV-Datei und liest sie ein. Dabei wir
Kuerzel fuer Kuerzel in der Reihenfolge der Datei eingelesen.
So hat man Kontrolle ueber die Reihenfolge der Bilder.
"""
def lese_kuerzel_ein():
    with open('fotos/texte_neu.csv', encoding='utf-8') as csvfile:
        fototexte = csv.reader(csvfile, delimiter=';')
        for zeile in fototexte:
            # Lies die zweite Spalte, also das Kuerzel, ein
            kuerzel.append( zeile[1] )     

"""
In dieser Methode werden die Texte aus der .csv-Datei eingelesen.
Der erste Teil der Zeile muss einem Dateinamen entsprechen, dass dahinter
kann ein beliebiger Text sein.
"""
def lese_texte_ein():
    beschreibungen = {} # Ein Dictionary 
                        # siehe auch hier:
                        # https://docs.python.org/3/tutorial/datastructures.html#dictionaries

    with open('fotos/texte_neu.csv', encoding='utf-8') as csvfile:
        fototexte = csv.reader(csvfile, delimiter=';')
        for zeile in fototexte:
            beschreibungen[zeile[1]] = zeile[2] + " (" + zeile[1].upper() + ")" + "\n" + zeile[3] 
            #[0]=Index, [1]=Kuerzel [2]=Geschlecht [3]=Name+Funktion+Faecher

    return beschreibungen

"""
Diese Methode erzeugt im speziellen Fall 8 Matritzen, die für 8 DIN-A3-Seiten
stehen. In einer spaeteren Version kann man das vielleicht verallgemeinern,
aber erstmal ist es fuer die konkrete Anforderung mit 192 Fotos programmiert.
"""
def erzeuge_matrize():  
    anzahl_spalten = 24 # idealerweise muss das nicht definiert werden
                        # aber zunaechst codiere ich das alles fest, so dass
                        # es auf jeden Fall erstmal passt

    # Eine manuell angelegte Matrix mit 24x8 Feldern. Das kann man
    # natürlich auch mit einer For-Schleife machen, aber so ist
    # es visueller
    matritze = [

    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]],
    [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    ]

    aktuelle_reihe = 0
    aktuelle_spalte = 0
    for k in kuerzel:
        # print("Setze Reihe und Spalte:", aktuelle_reihe, aktuelle_spalte, k)
        matritze[aktuelle_reihe][aktuelle_spalte] = k


        if aktuelle_spalte < anzahl_spalten-1:
            aktuelle_spalte += 1 # naechste Spalte, gleiche Zeile
        else:
            aktuelle_spalte = 0
            aktuelle_reihe += 1 #gehe in die naechste Reihe

    # debug_matritze(matritze)

    return matritze

"""
Diese Methode gibt einfach nur zeilenweise eine Matritze aus
"""
def debug_matritze(matritze):
    for x in matritze:
        print(x)
        print("\n")

"""
Diese Methode erzeugt 8 Matritzen: m1 bis m8. 
Diese 8 haben jeweils 8x4 Zellen und entsprechen einer DIN-A3-
Seite. Aus diesen einzelnen Seiten werden dann die PDF-Dateien generiert.
"""
def generiere_einzelseiten(matritze, bildtexte):
    # zuenachst programmiert fuer die Testmatrize
    # muss anschliessend verallgemeinert werden
    m1 = [] # erste Seite, also Spalten 1-6
    m2 = [] # zweite Seite, also Spalten 7-12
    m3 = [] # dritte Seite, also Spalten 13-18
    m4 = [] # vierte Seite, also Spalten 19-24

    # ab hier die untere Haelfte der Matrix
    m5 = [] # fünfte Seite, also Spalten 1-6
    m6 = [] # sechste Seite, also Spalten 7-12
    m7 = [] # siebte Seite, also Spalten 13-18
    m8 = [] # achte Seite, also Spalten 19-24
    

    for zeile in range(0,4):
        m1.append(matritze[zeile][0:6])

    for zeile in range(0,4):
        m2.append(matritze[zeile][6:12])        
    
    for zeile in range(0,4):
        m3.append(matritze[zeile][12:18])

    for zeile in range(0,4):
        m4.append(matritze[zeile][18:24])      
        
    for zeile in range(4,8):
        m5.append(matritze[zeile][0:6])

    for zeile in range(4,8):
        m6.append(matritze[zeile][6:12])        
    
    for zeile in range(4,8):
        m7.append(matritze[zeile][12:18])

    for zeile in range(4,8):
        m8.append(matritze[zeile][18:24])   
    
    # Fuer diesen Code gibt es keinen Preis, aber in der ersten
    # Version funktioniert er erstmal...
    generiere_einzelseiten_als_pdf( m1, "seite1.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m2, "seite2.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m3, "seite3.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m4, "seite4.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m5, "seite5.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m6, "seite6.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m7, "seite7.pdf", bildtexte )
    generiere_einzelseiten_als_pdf( m8, "seite8.pdf", bildtexte )


"""
Gibt als Rueckgabewert die komplette Bildunterschrift zurueck
Im Falle einer Leerstelle (das sind z.B. die letzten Bilder, die
es gar nicht gibt), wird als Text "-FEHLER-" eingesetzt.
"""
def erzeuge_bildunterschrift( zellinhalt, beschreibungen ):
    unterschrift = ""

    # Wenn da nichts drin steht ist das Objekt an dieser
    # Stelle vom Typ List und kein String. Fuer diesen
    # Fall muss ich hier einen String setzen, sonst
    # stuerzt die Software ab. So kann man ausserdem
    # auch super Fehler finden :-)
    if not isinstance( zellinhalt, str):
        unterschrift = "-FEHLER-"
    else:
        try:
            unterschrift = beschreibungen[ zellinhalt ]
        except:
            print(zellinhalt + " gibts nicht") #wenn es zum Bild keinen passenden Eintrag gibt 
            pass

    return unterschrift


"""
Generiert aus der gegebeben 8x4 Matritze eine PDF-Datei
"""
def generiere_einzelseiten_als_pdf( matritze, dateiname, beschreibungen ):
    # print("Generiere Einzelseite fuer:")
    # print("######################################")
    # debug_matritze( matritze )
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # print(beschreibungen)

    # L = Landscape, P = Portrait
    pdf = FPDF(orientation='L', unit='mm', format='A3')

    #sonst wird, wenn in der letzten Zeile zu viel steht ein Seitenumbruch gemacht. 
    pdf.set_auto_page_break(auto=True, margin=0) 
    
    pdf.add_page()
    #Fuer Kollegen mit ganz speziellen Zeichen im Namen muss man eine 
    #Schriftart nehmen, die das auch untersützt. DejaVu geht auf 
    #jeden Fall. Aus Copyrightgruenden lade ich die aber nicht hoch,
    #man findet die Datei aber überall. Diese muss einfach nur im 
    #selben Verzeichnis liegen
    #https://stackoverflow.com/questions/54679597/why-is-the-font-not-loading-in-pfpd-add-font

    pdf.add_font('DejaVu', '', r'DejaVuSans.ttf', uni=True) 
    pdf.set_font('DejaVu', '', size=12)
    #pdf.set_line_width(1)
    pdf.set_draw_color(255,255,255)
    pdf.set_fill_color(255,255,255)

    # Zeichne den Seitenhintergrund in einer Farbe
    pdf.rect(0,0 , 300, 300, 'F')

    
    x = 0
    y = 0

    # jetzt geht der Code Zeile fuer Zeile durch die Matritze und 
    # innerhalb der Zeilen die einzelnen Zellen
    for zeile in matritze:
        # Jetzt die konkrete Zeile mit jeweils 6 Bildern
        for zelle in zeile:
            zellinhalt = erzeuge_bildunterschrift( zelle, beschreibungen )
                  
            # wenn kein Text vorliegt sollte auch kein Bild gedruckt werden
            if zellinhalt != "-FEHLER-" and zellinhalt != "TEXT FEHLT" and zelle != "":
                pdf.set_xy(x * 70+5, y * 65+40)
                
                # # Drucke Umrandung
                #pdf.set_line_width(1)
                pdf.set_draw_color(0,0,0)
                # pdf.set_fill_color(188,188,188)
                # pdf.rect(x * 50 +5, y*45 +10 , 40, 42, style="F")
                pdf.rect(x * 70 +5, y*65 +10 , 60, 62)
                

                # Drucke das Bild
                bild_pfad = "./fotos/" + zelle + ".jpg"
                pdf.image(bild_pfad, x=x*70+20, y=y * 65 +12, w=32)

                # Hintergrund fuer den Text
                # pdf.rect(x * 70 +10, y*65 +40 , 60, 15, 'F')


                # Drucke Bildunterschrift
                # pdf.set_draw_color(240,240,240)
                # pdf.set_fill_color(240,240,240)
                pdf.set_xy(x * 70+5, y * 65+56)
                pdf.multi_cell(60,5, txt=zellinhalt, align="C")#, fill=1) # C: Center

                # Hier die Doku zum Drucken von Mehrzeilen-Text:
                # https://pyfpdf.readthedocs.io/en/latest/reference/multi_cell/index.html
                # fpdf.multi_cell(w: float, h: float, txt: str, border = 0, align: str = 'J', fill: bool = False)
                

            # Nach jedem Bild muss die Position um 1 nach rechts korrigiert werden
            x += 1

            # print( "Werte von x und y sind: ", zellinhalt, x, y)
        
        # Nach jeder Zeile muss die x-Position wieder auf Anfang gesetzt werden
        # y steht fuer die Zeile, dieser Wert muss um 1 erhoeht werden
        y += 1
        x = 0  

    pdf.output( dateiname )


# Speichere alle Bildbeschreibungen in einem Dictionary
bildbeschreibungen = lese_texte_ein()
lese_kuerzel_ein()

m = erzeuge_matrize()
generiere_einzelseiten(m, bildbeschreibungen)