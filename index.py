import pytube

link = 'https://www.youtube.com/watch?v=KJ8pMCWxBDo'

pytube.YouTube(url=link).streams.get_highest_resolution().download(
    'Video Youtube Download')
