from pytube import YouTube

link = input("Enter the link: ")
yu = YouTube(link)

print("Title: ", yu.title)
print("Number of views: ", yu.views)
print("Length of video: ", yu.length)
print("Description: ", yu.description)
print("Ratings: ", yu.rating)

ys = yu.streams.get_highest_resolution()
ys.download("/home/mialskywalker/Downloads")
