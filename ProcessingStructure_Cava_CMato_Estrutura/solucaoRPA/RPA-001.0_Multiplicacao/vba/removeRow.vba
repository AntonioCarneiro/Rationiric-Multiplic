Option Explicit
Sub removeRow()

'
' Macro VBA: checkCellPaint
' Object: Excluir linhas da Planilha, para não gerar exception na execução do UiPath - pre configuração
' Data : 20/12/2021
' Autor: RPA4All - Antonio Carneiro
'
On Error GoTo removeRow_ERROR

Dim vl_row       As long
Dim v_countSheet As Integer
Dim v_indSheet   AS integer

vl_row = 1
v_countSheet = Sheets.Count

For v_indSheet = 1 To v_countSheet
    Doevents 	
    Sheets(v_indSheet).Activate
    
    For vl_row = 1 To 2
    	Doevents
        If Mid(Cells(vl_row, 1), 1, 11) = "Instrumento" Then
            Rows(vl_row).Delete
        Else
            If vl_row = 2 Then
                Rows(vl_row - 1).Delete
            End If
        End If
    Next vl_row
Next v_indSheet

	Exit Sub

removeRow_ERROR:

	Exit Sub

End Sub

