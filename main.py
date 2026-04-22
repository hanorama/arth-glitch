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

# welcome + file input
print("Welcome to the glitch generator.")
print("Please enter the name of the image to glitch, including the file extension (.jpg, .png, etc.).")
print("If you do not want to add an image to this repo, leave the input blank and press enter to use a preset.")
IMG_TO_GLITCH = input("")
if (IMG_TO_GLITCH == ""):
    IMG_TO_GLITCH = "real5.jpg"
    #IMG_TO_GLITCH = "wisdomteeth.png"

# open the binary data of the image
with open(IMG_TO_GLITCH, 'rb') as in_data:
    in_data = in_data.read() # reads in an object of class bytes
    ba = bytearray(in_data) # converts to a bytearray so we can modify the bytes directly. prints as hexadecimal (\x00)

# keep the header of the image safe
# if we don't, then it won't be able to convert back to an image
# jpg and jpeg headers end with \xff\xda
ba_length = len(ba)

#get SOS index
for i in range(ba_length):
    current_hex = ba[i]
    if i < ba_length:
        next_hex = ba[i+1]
        if (current_hex == 0xff and next_hex == 0xda): ## \xff and \xda
            SOS_index = i + 2 # Start Of Scan index (where the image starts, after the header ends)
            print("SOS Index:" + str(SOS_index))
            break #found end of header, now exit the loop

# modify the image, ex) ba[200] = 0x00
print(ba[SOS_index])
for i in range(SOS_index, ba_length): # from SOS to end of file:
    pass

# linear search starting at 0
# linear search starting at length
# replace every number with 1

# save the modified binary data as a copy of the image
with open("glitched_" + IMG_TO_GLITCH, 'wb') as out_data:
    out_data.write(ba)
    print("Glitch complete.")