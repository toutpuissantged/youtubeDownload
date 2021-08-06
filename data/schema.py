from autoloader import time,random

class Schema():

    @staticmethod
    def Video(title='',size='--',save_dir='F:\code\Projets\python\youtubeSlack\vm',youtube_link='',objet=''):
        if (len(title)<1): title='Loading ...'
        return {
            'title':title ,
            'size':str(size)+' Mb',
            'save_dir':save_dir,
            'video_url':'',
            'youtube_link':youtube_link,
            'completed':False,
            'progress':0,
            'stream':0,
            'objet':'',
            'index':0,
            'progress_pointer':0,
            'youtube_dl_pointer':0,
            'id':int(time.time()+random.randint(9999,999999))
        }