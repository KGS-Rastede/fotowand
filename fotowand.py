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
"""
 
import os
from fpdf import FPDF




 
# L = Landscape, P = Portrait
pdf = FPDF(orientation='L', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Test der Fotowand", ln=1, align="C") # C: Center
pdf.output("fotowand.pdf")

kuerzel = [] #hier sind alle (bis zu 192) Kuerzel drin.

#Praktischerweise sortiert das Dateisystem die Dateinamen
#automatisch, so dass wir hier an der Reihenfolge
#nichts mehr aendern muessen.
with os.scandir("fotos") as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_file():
            #print(entry.name.split(".")[0])
            kuerzel.append(entry.name.split(".")[0])


print(kuerzel) # zum Sicherstellen kurz ausgeben, ob alle Dateien ausgelesen wurden

# for k in kuerzel:
#     print(type(k))

reihen, spalten = (4, 24) 
  
# method 2a 
# arr = [[0]*spalten]*reihen 


# Zum Testen eine 6x4 Matrize, muessen am Ende aber 24x4 sein
matritze = [

[[],[],[],[],[],[]],
[[],[],[],[],[],[]],
[[],[],[],[],[],[]],
[[],[],[],[],[],[]]

]

# sollen am Ende 4 und 24 sein
anzahl_reihen = 4
anzahl_spalten = 6

aktuelle_reihe = 0
aktuelle_spalte = 0
for k in kuerzel:
    print("Setze Reihe und Spalte:", aktuelle_reihe, aktuelle_spalte, k)
    matritze[aktuelle_reihe][aktuelle_spalte] = k


    if aktuelle_spalte < anzahl_spalten-1:
        aktuelle_spalte = aktuelle_spalte+1 # naechste Spalte, gleiche Zeile
    else:
        aktuelle_spalte = 0
        aktuelle_reihe = aktuelle_reihe +1 #gehe in die naechste Reihe

print(matritze)