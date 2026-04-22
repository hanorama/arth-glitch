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

real_in_data = []

# open the binary data of the image
with open('real5.jpg', 'rb') as real_in:
    real_in_data = real_in.read() # reads in an object of class bytes
    real_in_data = real_in_data.decode() # casts from byte to string type
    print(type(real_in_data))


# save the modified binary data as a copy of the image
with open('real5MODDED.jpg', 'wb') as real_out:
    real_in_data = real_in_data.encode() # cast back from string to byte type
    real_out.write(real_in_data)
