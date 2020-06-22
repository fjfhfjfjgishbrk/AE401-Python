Public Class Form1
    Dim color(3) As Integer
    Dim changeColor As Integer
    Dim buttons(4) As Button

    Private Sub SetColors()
        For i = 0 To 2
            color(i) = Int(Rnd() * 230)
        Next
        changeColor = Int(Rnd() * 4)
        For i = 0 To 3
            If i = changeColor Then
                buttons(i).BackColor = System.Drawing.Color.FromArgb(color(0) + 25, color(1), color(2))
            Else
                buttons(i).BackColor = System.Drawing.Color.FromArgb(color(0), color(1), color(2))
            End If
        Next
    End Sub
    Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Randomize()
        buttons(0) = Button1
        buttons(1) = Button2
        buttons(2) = Button3
        buttons(3) = Button4
        SetColors()
    End Sub

    Private Sub Buttons_Click(sender As Object, e As EventArgs) Handles Button1.Click, Button2.Click, Button3.Click, Button4.Click
        Dim clickedButton As Integer
        For i = 0 To 3
            If sender Is buttons(i) Then
                clickedButton = i
            End If
        Next
        If changeColor <> clickedButton Then
            Return
        End If
        SetColors()
    End Sub


End Class
