#importing the required modules
import instaloader
#creating object
d = instaloader.Instaloader()
#specifying the profilename
profile_Name = "terifcpython"
#do name profile_pic_only = True.
# to download the profile picture
d.download_profile(profile_Name)
#you will notice a folder of this profile's name
#which will all the post downloaded