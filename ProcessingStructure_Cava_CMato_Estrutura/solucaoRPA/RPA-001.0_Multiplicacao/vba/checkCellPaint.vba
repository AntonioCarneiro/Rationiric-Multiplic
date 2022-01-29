Sub checkCellPaint()

'
' Macro VBA: checkCellPaint
' Object: Retirar informação de erro *# e rescrever a informação
' Data : 28/11/2021
' Autor: RPA4All - Antonio Carneiro
'

On Error GoTo checkCellPaint_Error
    
Dim v_Col As Long
Dim v_Lin As Long
Dim v_totLin As Long
Dim v_totCol As Long
Dim v_caracterNumberFail As String
Dim v_caracterFail As String
Dim v_caracterSucs As String
Dim i_PosFail As Integer
Dim i_PosNumberFail As Integer
Dim i_PosSucs As Integer
Dim v_counteudo As String
Dim v_countSheet As Long
Dim v_indSheet As Long
Dim s_coluna    As String

v_Col = 0
v_Lin = 2
v_caracterFail = "*"
v_caracterSucs = "#"
v_caracterNumberFail = "99"
v_countSheet = Sheets.Count

'Debug.Print "== Inicio da Execução da Macro = " & Format(Now, "dd/MM/yyyy hh:mm:ss") & "=="
' Loop para todas as sheets
For v_indSheet = 1 To v_countSheet

    Sheets(v_indSheet).Activate
    v_totLin = ActiveSheet.Cells.SpecialCells(xlCellTypeLastCell).Row
    v_totCol = ActiveSheet.Cells.SpecialCells(xlCellTypeLastCell).Column

    If Sheets(v_indSheet).Name = "MV" Then
        Sheets(v_indSheet).Range("A1:Z1").Font.Bold = True
        Sheets(v_indSheet).Range("A1:Z1").Font.ColorIndex = 2
        Sheets(v_indSheet).Range("A1:P1").Interior.ColorIndex = 10
        Sheets(v_indSheet).Range("Q1:Z1").Interior.ColorIndex = 25
        s_coluna = "G1:Z" & Trim(Str(v_totLin))
        Sheets(v_indSheet).Range(s_coluna).HorizontalAlignment = xlCenter
    End If

    If Sheets(v_indSheet).Name = "INA" Then
        Sheets(v_indSheet).Range("A1:AF1").Font.Bold = True
        Sheets(v_indSheet).Range("A1:AF1").Font.ColorIndex = 2
        Sheets(v_indSheet).Range("A1:T1").Interior.ColorIndex = 10
        Sheets(v_indSheet).Range("U1:AF1").Interior.ColorIndex = 25
        s_coluna = "G1:AF" & Trim(Str(v_totLin))
        Sheets(v_indSheet).Range(s_coluna).HorizontalAlignment = xlCenter
    End If

    If Sheets(v_indSheet).Name = "RR" Then
        Sheets(v_indSheet).Range("A1:AI1").Font.Bold = True
        Sheets(v_indSheet).Range("A1:AI1").Font.ColorIndex = 2
        Sheets(v_indSheet).Range("A1:U1").Interior.ColorIndex = 10
        Sheets(v_indSheet).Range("V1:AI1").Interior.ColorIndex = 25
        s_coluna = "G1:AI" & Trim(Str(v_totLin))
        Sheets(v_indSheet).Range(s_coluna).HorizontalAlignment = xlCenter
    End If

    If Sheets(v_indSheet).Name = "PZ" Then
        Sheets(v_indSheet).Range("A1:AF1").Font.Bold = True
        Sheets(v_indSheet).Range("A1:AT1").Font.ColorIndex = 2
        Sheets(v_indSheet).Range("A1:T1").Interior.ColorIndex = 10
        Sheets(v_indSheet).Range("U1:AF1").Interior.ColorIndex = 25
        s_coluna = "G1:AF" & Trim(Str(v_totLin))
        Sheets(v_indSheet).Range(s_coluna).HorizontalAlignment = xlCenter
    End If
    DoEvents

' Loop para todas as linhas
For v_Lin = 2 To v_totLin
 
    ' Loop para todas as colunas
    For v_Col = 1 To v_totCol

        If v_Col = 2 Or v_Col = 3 Then
            DoEvents
        Else
            DoEvents
            v_counteudo = Cells(v_Lin, v_Col).Value
            i_PosNumberFail = InStr(1, Mid(v_counteudo, 1, 2), v_caracterNumberFail)
            i_PosFail = InStr(1, v_counteudo, v_caracterFail)
            i_PosSucs = InStr(1, v_counteudo, v_caracterSucs)

            If i_PosNumberFail > 0 Then
               DoEvents
               Cells(v_Lin, v_Col).Interior.ColorIndex = 3
               Cells(v_Lin, v_Col).Value = IIf(Len(v_counteudo) > 2, (Mid(v_counteudo, i_PosNumberFail + 2)), "")
            Else
                If i_PosFail > 0 Then
                   DoEvents
                   Cells(v_Lin, v_Col).Interior.ColorIndex = 3
                   Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosFail + 1)
                Else
                   If i_PosSucs > 0 Then
                    DoEvents
                        If Sheets(v_indSheet).Name = "INA" Or Sheets(v_indSheet).Name = "PZ" Then
                           If v_Col = 24 Then
                            Cells(v_Lin, v_Col).Interior.ColorIndex = 43
                            Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosSucs + 1)
                           ElseIf v_Col = 25 Then
                                 Cells(v_Lin, v_Col).Interior.ColorIndex = 3
                             Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosSucs + 1)
                           End If
                        ElseIf Sheets(v_indSheet).Name = "MV" Then
                           If v_Col = 18 Then
                            Cells(v_Lin, v_Col).Interior.ColorIndex = 43
                            Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosSucs + 1)
                           ElseIf v_Col = 19 Then
                                 Cells(v_Lin, v_Col).Interior.ColorIndex = 3
                             Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosSucs + 1)
                           End If
                        ElseIf Sheets(v_indSheet).Name = "RR" Then
                            If v_Col = 27 Then
                       Cells(v_Lin, v_Col).Interior.ColorIndex = 43
                       Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosSucs + 1)
                    ElseIf v_Col = 28 Then
                           Cells(v_Lin, v_Col).Interior.ColorIndex = 3
                           Cells(v_Lin, v_Col).Value = Mid(v_counteudo, i_PosSucs + 1)
                                End If
                        End If
                   End If
                End If
            End If
        End If

        If (Sheets(v_indSheet).Name = "PZ" or Sheets(v_indSheet).Name = "INA") and (v_Col = 7 or v_Col = 14 or v_Col = 17 or v_Col = 18) Then
           DoEvents
           v_counteudo = Replace(v_counteudo, "*", "")
           Cells(v_Lin, v_Col).Value = v_counteudo
        End If
           
        If (Sheets(v_indSheet).Name = "RR" or Sheets(v_indSheet).Name = "MV") and (v_Col = 7) Then
	   DoEvents
	   v_counteudo = Replace(v_counteudo, "*", "")
	   Cells(v_Lin, v_Col).Value = v_counteudo
        End If

        'Debug.Print v_Lin, v_Col
        DoEvents
    Next v_Col ' Loop Col
    DoEvents
Next v_Lin ' Loop Lin
DoEvents
Next v_indSheet ' Loop Sheet

'Debug.Print "== Final da Execução da Macro = " & Format(Now, "dd/MM/yyyy hh:mm:ss") & "=="
Exit Sub

checkCellPaint_Error:

    Exit Sub

End Sub
