from tkinter import * 
from tkinter import ttk
import time,os,asyncio

class VideoInfo():

    def __init__(self,props):
        self.moduleid=1
        self.props=props
        self.New()
        self.props['VideoWigdet']=''


    def Main(self,info=''):
        root=self.root
        if (len(info)<1):
            info=self.info

        
        MainLabel=Label(root,text='Titre : '+info['title'],padx=10,pady=10,font='fantasy',fg="darkslategray")
        MainLabel2=Label(root,text='Destination : '+self.TextReduc(text=info['save_dir'],num=6),padx=10,pady=10,font='fantasy',fg="darkslategray")
        MainLabel3=Label(root,text='File Size : '+info['size'],padx=10,pady=10,font='fantasy',fg="darkslategray")
        MainLabel4=Label(root,text='Progress : '+str(info['progress'])+' %',padx=10,pady=10,font='fantasy',fg="darkslategray")

        MainButton2=Button(root,text='Change',width='10',border=0,bg="royalblue",activebackground='blue',fg='white',padx=10,pady=5,activeforeground='white',font="arial")
        MainButton=Button(root,text='Download',width='10',border=0,bg="royalblue",activebackground='blue',fg='white',padx=10,pady=5,activeforeground='white',font="arial",command=lambda:self.props['Temp']['Search'].Download())
        
        MainProgress=ttk.Progressbar(master=root,orient=HORIZONTAL,length=200,mode='determinate')
        
        MainLabel.grid(row=3)
        MainLabel2.grid(row=4)
        MainButton2.grid(row=5)
        MainLabel3.grid(row=6)
        MainButton.grid(row=7)
        MainLabel4.grid(row=8,pady=1)
        MainProgress.grid(row=9,pady=1)

        self.MainProgress=MainProgress
        self.props['CurVideoInfo']['progress_pointer']= self.Progressbar()
        #self.Progressbar()
        

        self.props['VideoWigdet']=[MainLabel,MainLabel2,MainLabel3]

    def Destroy(self):
        self.root.destroy()

    def New(self,videoInfo=''):
        props=self.props
        self.root=props['videoInfoFrame']
        self.root.grid()
        self.info=videoInfo
        props['CurVideoInfo']=videoInfo
        props['AllVideoInfo'].append(videoInfo)
        props['CurVideoIndex']+=1

    def Loading(self):
        LoadingLabel=Label(self.root,text='Loading ... ',padx=20,pady=10,font='fantasy',fg="darkblue")
        LoadingLabel.grid(row=3,padx=10,pady=10)

    def Error(self,Log):

        LoadingLabel=Label(self.root,text='! '+Log,padx=10,pady=10,font='fantasy',fg="White",bg="crimson")
        LoadingLabel.grid(row=3,padx=10,pady=10)

    def Next(self):
        props=self.props
        if (props['CurVideoIndex']>=len(props['AllVideoInfo'])-1): return 0
        props['CurVideoIndex']+=1
        self.Updated()

    def Previous(self):
        props=self.props
        if (props['CurVideoIndex']<=0): return 0
        props['CurVideoIndex']-=1
        self.Updated()
       

    def Updated(self):
        props=self.props
        props['CurVideoInfo']=props['AllVideoInfo'][props['CurVideoIndex']]
        self.Loading()
        #time.sleep(1)
        self.Main(info=props['CurVideoInfo'])
        #self.props['VideoWigdet'][0].configure(text='updated')
        self.Debug()

    def Debug(self):
        props=self.props
        print(props['CurVideoIndex'])
        print(props['AllVideoInfo'])

    def TextReduc(self,text,num):
        reducLen=6
        textLen=len(text)
        textsliced=text.split('/')
        if (len(textsliced)<2) : textsliced=text.split('\\')
        if  (textLen<num) : return text
        return '... /'+textsliced[-1]

    async def Progressbar(self):
        for i in range(100):
            self.MainProgress['value']+=1
            time.sleep(0.1)
            await 2
             
