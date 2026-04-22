# TO - DO :

# -- PRE-PROGRAMMING --
# visit source sites again - DONE
# choose 2-3 selection algorithms
# find + choose a good image processing library for python

# -- PROGRAMMING -- 
# choose photo(s) to upload - DONE
# read photo as text
# parse through photo, making selections/replacements/removals based on selection method
# execute through photo text in an iterative fashion, saving a copy of the photo text every so often
# then, save the series of images to disk
# if possible, turn series of images into a video and save THAT to disk instead/as well

# end of to - do.
print("Welcome to the glitch generator.")
print("Please enter the name of the image to glitch, including the file extension (.jpg, .png, etc.).")
print("If you do not want to add an image to this repo, leave the input blank and press enter to use a preset.")
IMG_TO_GLITCH = input("")
if (IMG_TO_GLITCH == ""):
    IMG_TO_GLITCH = "real5.jpg"

# open the binary data of the image
with open(IMG_TO_GLITCH, 'rb') as in_data:
    in_data = in_data.read() # reads in an object of class bytes
    ba = bytearray(in_data) # converts to a bytearray so we can modify the bytes directly

# save the modified binary data as a copy of the image
with open("glitched_" + IMG_TO_GLITCH, 'wb') as out_data:
    out_data.write(ba)
    print("Glitch complete.")
