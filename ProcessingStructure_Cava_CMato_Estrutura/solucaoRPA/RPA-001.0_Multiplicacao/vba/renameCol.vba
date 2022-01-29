Sub renameCol()

'
' Macro VBA: renameCol
' Object: Update nome da coluna da Planilha, para evitar erro de carga no Uipath com colunas com o mesmo nome - pre configuração
' Data : 20/12/2021
' Autor: RPA4All - Antonio Carneiro
'

    On Error GoTo renameCol_ERROR
   
    Dim v_totCol As Integer
    Dim v_nameCol As String
    Dim v_indcol As Integer
    Dim v_findCol As Integer
    Dim v_altColumn As Integer
    Dim v_countSheet As integer
    Dim v_indSheet as integer
    Dim a_nameCol()
   
    ' Get qtde de sheets da planilha	   
    v_countSheet = Sheets.Count
      
    ' Loop para todas as sheets
    For v_indSheet = 1 To v_countSheet
        doEvents
    	Sheets(1).Activate
    	
    	' Total de colunas preenchidas
    	v_totCol = ActiveSheet.Cells.SpecialCells(xlCellTypeLastCell).Column
    	ReDim Preserve a_nameCol(1 To v_totCol)
   
    	For v_indcol = 1 To v_totCol
    	    DoEvents
    	    v_altColumn = 0
    	    If v_indcol > 1 Then
       
    	        For v_findCol = 1 To UBound(a_nameCol)
       			DoEvents()
    	            If v_findCol > v_indcol Then Exit For
               
    	            If a_nameCol(v_findCol) = Cells(1, v_indcol).Value Then
    	            
    	                colname = Split(Worksheets(1).Cells(1, v_indcol).Address, "$")(1)
    	                
       			' Altera o nome da coluna existente para nome da coluna mais posicao da coluna        
    	                a_nameCol(v_indcol) = Cells(1, v_indcol).Value & "_" & colname
    	                v_altColumn = 1
           
    	            End If
       
            	Next v_findCol
            End If
       
            if v_altColumn = 0 Then a_nameCol(v_indcol) = Cells(1, v_indcol).Value
       
    	Next v_indcol
    Next v_indSheet
	   
    For v_indcol = 1 to Ubound(a_nameCol)
    	Doevents
        Cells(1, v_indcol).Value = a_nameCol(v_indcol)
    next v_indcol
    
    Exit Sub
   
renameCol_ERROR:

    Exit Sub

End Sub