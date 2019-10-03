Option Compare Database


Public Function foto2_bestimmen(Anrede As Variant, Ref As Boolean, f1, f2, f3, foto2 As Variant)
  endung = ""
  If Anrede = "Frau" Then endung = "in"
  faecher = ""
  zeile = ""
  If Not (IsNull(f1)) Then faecher = f1
  If Not (IsNull(f2)) Then faecher = faecher & ", " & f2
  'If Not (IsNull(f3)) Then faecher = faecher & ", " & f3
  faecher = "(" & faecher & ")"
  zeile = faecher
  If Ref Then zeile = "Referendar" & endung & " " & faecher
  If Not (IsNull(foto2)) Then zeile = foto2
  foto2_bestimmen = zeile
End Function



Public Sub fotowand_formatieren(bericht As Report, pfad As String)
  'On Error GoTo fotowand_formatieren_Error
    Dim strBildpfad As String
    strBildpfad = Nz(Application.CurrentProject.Path & "\" & pfad & "\" & bericht![Kürzel_bereinigt] & ".jpg", "")
    strBildpfad = LCase(strBildpfad)
    'MsgBox strBildpfad
    If Len(Dir(strBildpfad)) = 0 Then
      strBildpfad = Nz(Application.CurrentProject.Path & "\" & pfad & "\" & "_fehlt.jpg", "")
      strBildpfad = LCase(strBildpfad)
    End If
    If Len(Dir(strBildpfad)) > 0 Then
      bericht!picBildVerknuepft.Picture = strBildpfad
    End If

''fotowand_formatieren_Exit:
    ''MsgBox "Fehler " & bericht![Kürzel_bereinigt]
    ''Exit Sub

''fotowand_formatieren_Error:
    ''Resume fotowand_formatieren_Exit
End Sub

Public Sub Fotowand_Reihenfolge()
  Dim i As Integer
  Dim db_lehrer As Database
  Set db_fotowand = CurrentDb
  Dim rs_fotowand As Recordset
  Dim db_fotowand_reihenfolge As Database
  Set db_fotowand_reihenfolge = CurrentDb
  Dim rs_fotowand_reihenfolge As Recordset
  Quelle = "fotos"
  Quelle_fotowand_reihenfolge = "fotowand_reihenfolge"
  SQL_fotowand = "SELECT * FROM [" & Quelle & "]"
  SQL_fotowand_reihenfolge = "SELECT * FROM [" & Quelle_fotowand_reihenfolge & "]"
  Set rs_fotowand = db_fotowand.OpenRecordset(SQL_fotowand)
  Set rs_fotowand_reihenfolge = db_fotowand.OpenRecordset(SQL_fotowand_reihenfolge)
  'Tabelle Reihenfolge löschen
  While rs_fotowand_reihenfolge.RecordCount > 0
   rs_fotowand_reihenfolge.Delete
   rs_fotowand_reihenfolge.MoveNext
  Wend

  
  i = 1
  While rs_fotowand.EOF = False
    'Datensatz erzeugen
    rs_fotowand_reihenfolge.AddNew
    rs_fotowand_reihenfolge![Kürzel_bereinigt] = rs_fotowand![Kürzel_bereinigt]
    rs_fotowand_reihenfolge![Zeile1] = rs_fotowand![Eintrag] & " (" & rs_fotowand![Kürzel_bereinigt] & ")"
    rs_fotowand_reihenfolge![Zeile2] = rs_fotowand![foto2]
    rs_fotowand_reihenfolge![Reihenfolge] = fotowand_index(i)
    rs_fotowand_reihenfolge![Eintrittsdatum] = rs_fotowand![Eintrittsdatum]
    rs_fotowand_reihenfolge.Update
    rs_fotowand.MoveNext
    i = i + 1
  Wend
  MsgBox "Fotowand fertig ..."
End Sub

Public Function fotowand_index(i As Integer)
  'Konstanten festlegen
  zeilen_anordnung2 = 3 '#######################
  blatt_pro_zeile = 4 'Anzahl Seiten pro Zeile Bilderrahmen
  zeilen_pro_blatt = 4 'Anzahl Zeilen Bilder pro Blatt
  spalten_pro_blatt = 5 'Anzahl Spalten Bilder pro Blatt
  zeile_a = Int((i - 1) / (blatt_pro_zeile * zeilen_pro_blatt * spalten_pro_blatt) + 1)
  blatt = Int((i - 1) / spalten_pro_blatt) Mod blatt_pro_zeile + 1
  zeile = Int((i - 1) / (blatt_pro_zeile * spalten_pro_blatt)) Mod zeilen_pro_blatt + 1
  spalte = (i - 1) Mod spalten_pro_blatt + 1
  fotowand_index = (zeile_a - 1) * blatt_pro_zeile * zeilen_pro_blatt * spalten_pro_blatt + (blatt - 1) * zeilen_pro_blatt * spalten_pro_blatt + (zeile - 1) * spalten_pro_blatt + spalte
End Function
Public Sub Fotowand_Reihenfolge192()
   Dim i As Integer
  Dim db_lehrer As Database
  Set db_fotowand = CurrentDb
  Dim rs_fotowand As Recordset
  Dim db_fotowand_reihenfolge As Database
  Set db_fotowand_reihenfolge = CurrentDb
  Dim rs_fotowand_reihenfolge As Recordset
  Quelle = "fotos"
  Quelle_fotowand_reihenfolge = "fotowand_reihenfolge"
  SQL_fotowand = "SELECT * FROM [" & Quelle & "]"
  SQL_fotowand_reihenfolge = "SELECT * FROM [" & Quelle_fotowand_reihenfolge & "]"
  Set rs_fotowand = db_fotowand.OpenRecordset(SQL_fotowand)
  Set rs_fotowand_reihenfolge = db_fotowand.OpenRecordset(SQL_fotowand_reihenfolge)
  'Tabelle Reihenfolge löschen
  While rs_fotowand_reihenfolge.RecordCount > 0
   rs_fotowand_reihenfolge.Delete
   rs_fotowand_reihenfolge.MoveNext
  Wend

  
  i = 1
  While rs_fotowand.EOF = False
    'Datensatz erzeugen
    rs_fotowand_reihenfolge.AddNew
    rs_fotowand_reihenfolge![Kürzel_bereinigt] = rs_fotowand![Kürzel_bereinigt]
    rs_fotowand_reihenfolge![NACHNAME] = rs_fotowand![NACHNAME]
    rs_fotowand_reihenfolge![VORNAME] = rs_fotowand![VORNAME]
    rs_fotowand_reihenfolge![Zeile1] = rs_fotowand![Eintrag] & " (" & rs_fotowand![Kürzel_bereinigt] & ")"
    rs_fotowand_reihenfolge![Zeile2] = rs_fotowand![foto2]
    rs_fotowand_reihenfolge![Reihenfolge] = fotowand_index192(i)
    ' rs_fotowand_reihenfolge![Reihenfolge] = i
    rs_fotowand_reihenfolge![Eintrittsdatum] = rs_fotowand![Eintrittsdatum]
    rs_fotowand_reihenfolge.Update
    rs_fotowand.MoveNext
    i = i + 1
  Wend
    j = i - 1
  While i <= 192
    rs_fotowand_reihenfolge.AddNew
    rs_fotowand_reihenfolge![Reihenfolge] = fotowand_index192(i)
    rs_fotowand_reihenfolge.Update
    i = i + 1
  Wend
  MsgBox "Fotowand fertig ... mit " & j & " Fotos und " & 192 - j & " Leerfeldern"
End Sub

Public Function fotowand_index192(i As Integer)
  'bei max 192 Positionen Feld festlegen
  Position = Array("1", "2", "3", "4", "5", "6", "25", "26", "27", "28", "29", "30", "49", "50", "51", "52", "53", "54", "73", "74", "75", "76", "77", "78", "7", "8", "9", "10", "11", "12", "31", "32", "33", "34", "35", "36", "55", "56", "57", "58", "59", "60", "79", "80", "81", "82", "83", "84", "13", "14", "15", "16", "17", "18", "37", "38", "39", "40", "41", "42", "61", "62", "63", "64", "65", "66", "85", "86", "87", "88", "89", "90", "19", "20", "21", "22", "23", "24", "43", "44", "45", "46", "47", "48", "67", "68", "69", "70", "71", "72", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "121", "122", "123", "124", "125", "126", "145", _
  "146", "147", "148", "149", "150", "169", "170", "171", "172", "173", "174", "103", "104", "105", "106", "107", "108", "127", "128", "129", "130", "131", "132", "151", "152", "153", "154", "155", "156", "175", "176", "177", "178", "179", "180", "109", "110", "111", "112", "113", "114", "133", "134", "135", "136", "137", "138", "157", "158", "159", "160", "161", "162", "181", "182", "183", "184", "185", "186", "115", "116", "117", "118", "119", "120", "139", "140", "141", "142", "143", "144", "163", "164", "165", "166", "167", "168", "187", "188", "189", "190", "191", "192")


  fotowand_index192 = Position(i - 1)
End Function