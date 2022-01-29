Sub checkCellPaintCadastro()

'
' Macro VBA: checkCellPaintCadastro
' Object: Retirar informação de erro * e rescrever a informação do Cadastro
' Data : 04/12/2021
' Autor: RPA4All - Antonio Carneiro
'

On Error GoTo checkCellPaint_Error
Dim v_Col As Long
Dim v_Lin As Long
Dim v_Conteudo As String
Dim v_totLin As Long
Dim v_totCol As Long
Dim v_caracterFail As String
Dim i_PosFail As Integer
Dim v_countSheet As Long
Dim v_indSheet As Long
Dim s_coluna    As String

v_Col = 0
v_Lin = 2
v_caracterFail = "*"

v_contSheet = Sheets.Count
'Debug.Print "== Inicio da Execução da Macro = " & Format(Now, "dd/MM/yyyy hh:mm:ss") & "=="
' Loop para todas as sheets
For v_indSheet = 1 To v_contSheet

Sheets(v_indSheet).Activate
v_totLin = ActiveSheet.Cells.SpecialCells(xlCellTypeLastCell).Row
v_totCol = ActiveSheet.Cells.SpecialCells(xlCellTypeLastCell).Column
Doevents

If Sheets(v_indSheet).Name = "Instrumentos Ativos" Then
    Sheets(v_indSheet).Range("A1:AB1").Font.Bold = True
    Sheets(v_indSheet).Range("A1:U1").Interior.ColorIndex = 10
    Sheets(v_indSheet).Range("V1:AB1").Interior.ColorIndex = 45
    s_coluna = "F1:AB" & Trim(Str(v_totLin))
    Sheets(v_indSheet).Range(s_coluna).HorizontalAlignment = xlCenter
End If

If Sheets(v_indSheet).Name = "Instrumentos Inativos" Then
    Sheets(v_indSheet).Range("A1:M1").Font.Bold = True
    Sheets(v_indSheet).Range("A1:J1").Interior.ColorIndex = 10
    Sheets(v_indSheet).Range("K1:M1").Interior.ColorIndex = 45
    s_coluna = "E1:M" & Trim(Str(v_totLin))
    Sheets(v_indSheet).Range(s_coluna).HorizontalAlignment = xlCenter
End If
DoEvents

' Loop para todas as linhas
For v_Lin = 2 To v_totLin
 
    ' Loop para todas as colunas
    For v_Col = 1 To v_totCol
    
    If v_Col = 2 Or v_Col = 3 Or v_Col = 4 Then
       DoEvents
    Else
        If v_indSheet = 1 Then
            If v_Col = 5 Or v_Col > 20 Then
                DoEvents
            Else
                v_Conteudo = Cells(v_Lin, 1).Value
                i_PosFail = InStr(1, v_Conteudo, v_caracterFail)

                If i_PosFail > 0 Then
                    Cells(v_Lin, v_Col).Interior.ColorIndex = 3
                    Cells(v_Lin, v_Col).Value = Mid(v_Conteudo, i_PosFail + 1)
                End If
            
                v_Conteudo = Cells(v_Lin, v_Col).Value
                If (v_Col > 5 And v_Col < 12) Or (v_Col > 13 And v_Col < 21) Then
                    Cells(v_Lin, v_Col).Value = v_Conteudo
                End If
            End If
        Else
            If v_Col > 10 Then
                DoEvents
            Else
                v_Conteudo = Cells(v_Lin, 1).Value
                i_PosFail = InStr(1, v_Conteudo, v_caracterFail)

                If i_PosFail > 0 Then
                    Doevents
                    Cells(v_Lin, v_Col).Interior.ColorIndex = 3
                    Cells(v_Lin, v_Col).Value = Mid(v_Conteudo, i_PosFail + 1)
                End If
            
                v_Conteudo = Cells(v_Lin, v_Col).Value
                If (v_Col > 4 And v_Col < 11) or (v_col = 13) Then
                    Doevents
                    Cells(v_Lin, v_Col).Value = v_Conteudo
                End If
            End If
        End If
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
