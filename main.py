import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title = title, size = (600, 800))

        panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        verticalBox = wx.BoxSizer(wx.VERTICAL)
        horizontalBox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.label = wx.StaticText(self, label = "This is a label", style=wx.ALIGN_CENTER)
        verticalBox.Add(self.label, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 35)

        self.anotherLabel = wx.StaticText(self, label = "This is another label", style=wx.ALIGN_CENTER)
        verticalBox.Add(self.anotherLabel, 0, wx.EXPAND)

        self.hLabel=wx.StaticText(self, label = "This is a h label", style=wx.ALIGN_CENTER)
        horizontalBox.Add(self.hLabel, 0, wx.EXPAND)

        self.anotherHLabel=wx.StaticText(self, label = "This is another h label", style=wx.ALIGN_CENTER)
        horizontalBox.Add(self.anotherHLabel, 0, wx.EXPAND)
        
        verticalBox.Add(horizontalBox, 0, wx.ALIGN_CENTER)
        self.SetSizer(verticalBox)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent = None, title = "Box Sizer")
        self.frame.Show()

        return True

app = MyApp()
app.MainLoop()
