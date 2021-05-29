import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title = title, size = (600, 500))

        panel = MyPanel(self)

class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        verticalBox = wx.BoxSizer(wx.VERTICAL)
        horizontalBox0 = wx.BoxSizer(wx.HORIZONTAL)
        horizontalBox1 = wx.BoxSizer(wx.HORIZONTAL)
        
        self.title = wx.StaticText(self, label = "Program Title", style=wx.ALIGN_CENTER)
        verticalBox.Add(self.title, 0, wx.EXPAND | wx.TOP, 35)

        self.instructions = wx.StaticText(self, label = "Instructions", style=wx.ALIGN_CENTER)
        verticalBox.Add(self.instructions, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 25)

        # first input set
        self.firstLabel=wx.StaticText(self, label = "Enter input 1: ", style=wx.ALIGN_CENTER)
        horizontalBox0.Add(self.firstLabel, 0, wx.EXPAND)
        self.firstInput = wx.TextCtrl(self)
        horizontalBox0.Add(self.firstInput, 0, wx.EXPAND)

        # second input set
        self.firstLabel=wx.StaticText(self, label = "Enter input 2: ", style=wx.ALIGN_CENTER)
        horizontalBox1.Add(self.firstLabel, 0, wx.EXPAND)
        self.firstInput = wx.TextCtrl(self)
        horizontalBox1.Add(self.firstInput, 0, wx.EXPAND)

        # action button
        actionButton = wx.Button(self, label = "Action", style=wx.ALIGN_CENTER)
        actionButton.Bind(wx.EVT_BUTTON, print("Action!"))

        # result message
        
        # adding elements to verticalBox
        verticalBox.Add(horizontalBox0, 0, wx.ALIGN_CENTER)
        verticalBox.Add(horizontalBox1, 0, wx.ALIGN_CENTER | wx.TOP, 25)
        verticalBox.Add(actionButton, 0, wx.ALIGN_CENTER | wx.TOP, 25)

        self.SetSizer(verticalBox)
    
        # fonts
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
