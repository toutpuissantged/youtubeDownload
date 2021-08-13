from autoloader import *

class Index():
    ''' entry class for organize user interface '''

    def __init__(self,props):
        self.props=props
        self.props['Views']['windows']=Frame(self.props['root'])

    def main(self):

        root=self.props['root']
        menubar = Menu(root)
        props=self.props
        self.props['Views']['Menu']=menubar
        root.config(menu=menubar)
        videoInfoFrame=Frame(root)
        props['videoInfoFrame']=videoInfoFrame
        
        File=FileMenu(props=props).monted()
        Edit=EditMenu(props=props).monted()
        Help=HelpMenu(props).monted()
        Page=PageMenu(props).monted()

        menubar.add_cascade(label='File', menu=File)
        menubar.add_cascade(label='Edit', menu=Edit)
        menubar.add_cascade(label='Help', menu=Help)
        menubar.add_cascade(label='Page', menu=Page)

        BaseTheme(props=props).Main()
        vidInfo=VideoInfo(props)
        props['vidInfo']=vidInfo
        #vidInfo.Error()

        return 0