from autoloader import *

class PageMenu(FileMenu):

    def __init__(self,props):
        self.props=props
        self.windows=self.props['Views']['windows']    
        self.MyMenu=self.props['Views']['Menu'] 

        self.shortcut()

    def shortcut(self):
        self.Next="" 
        self.Previous=""

    def monted(self):
        root=self.windows
        Tab=self.props['Tabs']
        NavBarFrame=Frame(root)
        menu = Menu(NavBarFrame)
        PageBox = Menu(menu)
        
        Tabnum=0
        PageBox.add_command(label='Next',command=lambda:self.props['vidInfo'].Next(),accelerator=self.Next)
        PageBox.add_command(label='Previous',command=lambda:self.props['vidInfo'].Previous(),accelerator=self.Previous)

        return PageBox