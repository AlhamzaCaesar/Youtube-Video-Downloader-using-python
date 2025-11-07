import pytube
from pytube import youtube

print("IG : @alhamzacaesar")
link = input("Enter the link of video : ")
yt = Youtube(link)
print("The video will install : " + str(yt.title))
yt=yt.streams.get_highest_resolution()
yt.download()
print("DONE !")
