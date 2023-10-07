Sub RunRScript()
    Dim R As Object
    Dim output As String
    
    ' path to R script
    Dim scriptPath As String
    scriptPath = "C:\PATH\insurance_calculations.R"
    
    ' R executable
    Dim rPath As String
    rPath = "C:\PATH\R\bin\Rscript.exe"
    
    output = CreateObject("WScript.Shell").Exec(rPath & " " & scriptPath).StdOut.ReadAll
    qsFilePath = ThisWorkbook.Path & "\qs_output.csv"
    
    ' import the data from CSV to Excel
    With ThisWorkbook.Sheets("Sheet1") 
        .Range("A1").CurrentRegion.ClearContents
        .QueryTables.Add Connection:="TEXT;" & qsFilePath, Destination:=.Range("F1")
        .QueryTables(1).TextFileParseType = xlDelimited
        .QueryTables(1).TextFileCommaDelimiter = True 
        .QueryTables(1).Refresh
        .QueryTables(1).Delete
    End With
End Sub
