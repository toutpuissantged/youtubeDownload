from autoloader import Playlist,YouTube,Schema,threading ,time , random

class Search():
    def __init__(self,InputVal,props):
        super().__init__()
        self.input=InputVal
        self.previousprogress = 0
        self.props=props
        self.VideoInfo=Schema.Video()
        self.loop=0
        #self.Init()
        self.videoFormat={
            'file_extension':'mp4',
            'res':'360p'
        }

    @staticmethod
    def Test(InputVal):
        print(InputVal.get())

    def Init(self):
        url=self.input.get()
        yt = YouTube(url)
        self.yt=yt
        return yt

    def GetInfo(self,loop=0):
        print('started')
        title=''
        size='--'
        #self.Init()
        if (loop>0):
            self.Init()
            title=self.yt.title
            size=self.yt.streams.filter(file_extension=self.videoFormat['file_extension'],res=self.videoFormat['res']).first().filesize
            size=int(size//(1024**2))
        self.ui(title=title,size=size ,youtube_link='')
        self.loop+=1
        
        
    
    def Download(self):
        self.Init()
        self.GetInfo()
        self.Progressbar()
        # self.ui(title=self.yt.title,size=22 ,youtube_link='')
        yt=self.yt
        yt.register_on_progress_callback(self.on_progress)
        yt.streams.filter(file_extension=self.videoFormat['file_extension'],res=self.videoFormat['res']).first().download()

    def on_progress(self,stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 

        liveprogress = (int)(bytes_downloaded / total_size * 100)
        if liveprogress > self.previousprogress:
            self.previousprogress = liveprogress
            print(liveprogress)

    def ui(self,title='No Title',size='--' ,youtube_link=''):
        self.props['vidInfo'].Loading()
        #time.sleep(2)
        self.props['vidInfo'].Error(Log='check network')
        self.props['vidInfo'].New(videoInfo=Schema.Video(title=title,size=size ,youtube_link=youtube_link,objet=''))
        self.props['vidInfo'].Main()

    def Progressbar(self):
        self.props['CurVideoInfo']['progress_pointer']
