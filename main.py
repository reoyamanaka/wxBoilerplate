import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title = title, size = (800, 800))

        panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        verticalBox = wx.BoxSizer(wx.VERTICAL)
        horizontalBox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.title = wx.StaticText(self, label = "Program Title", style=wx.ALIGN_CENTER)
        verticalBox.Add(self.title, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 35)

        self.instructions = wx.StaticText(self, label = "Instructions", style=wx.ALIGN_CENTER)
        verticalBox.Add(self.instructions, 0, wx.EXPAND)

        self.hLabel=wx.StaticText(self, label = "This is a h label", style=wx.ALIGN_CENTER)
        horizontalBox.Add(self.hLabel, 0, wx.EXPAND)

        self.anotherHLabel=wx.StaticText(self, label = "This is another h label", style=wx.ALIGN_CENTER)
        horizontalBox.Add(self.anotherHLabel, 0, wx.EXPAND)
        
        verticalBox.Add(horizontalBox, 0, wx.ALIGN_CENTER)
        self.SetSizer(verticalBox)
    
        #fonts
        headerFont = wx.Font(24, wx.DEFAULT, wx.DEFAULT, wx.BOLD)
        self.title.SetFont(headerFont)

        subheaderFont = wx.Font(18, wx.DEFAULT, wx.DEFAULT, wx.DEFAULT)
        self.instructions.SetFont(subheaderFont)

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent = None, title = "Program")
        self.frame.Show()

        return True

app = MyApp()
app.MainLoop()
