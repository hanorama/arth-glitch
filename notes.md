# Notes from Some References
References which do not have notes below were used primarily for programming purposes, such as learning how to use a new library.

## Dab. (2024, August 1). 10 Digital Artists: The Best of Glitch art. DIGITAL ARTS BLOG. https://www.digitalartsblog.com/artist-spotlights/glitch-art 
King Xerox's most popular works include glitch art in GIF formats with a focus on religious imagery. The glitch effects in his art appear to be added in post-production, rather than using a method of corrupting the data of the work itself. The effects he uses are prominent and singular, tending to be the focal point of the piece.

Clayton Campbell's glitch art is presented with more subtlety. He uses glitch effects that are visually similar to double exposures in analog photography, making the glitches appear more as a ghostly collage. His work appears to be done using standard photo manipulation, rather than directly modifying the data of an image itself.

Empress Trash most recent glitch works use Artificial Intelligence in their creation. Her works tend to focus on a pastel pink-blue-purple palette, leaning towards a vapourwave aesthetic. Rather than employing actual glitch techniques in her art, she seems to lean towards abstracting the idea of a glitch, and presenting that as her subject matter.

Matt Kane uses code to create his works. Much of his recent work appears to draw from printmaking and abstract techniques. Many of his works involve repetitions of patterns or line that look as though they were created with a patterned block or fabric.

Adrian Cain uses the programs Audacity, Blender, and the programming language Processing to create his works. These works look more aligned with traditional glitch art - they appear as images that look similar to the kinds of accidental glitches a person would encounter in the world. Datamoshing appears to be one of the main techniques he uses for these works.

Dawnia Darkstone creates glitch art that is often heavily abstracted. The glitches in many of her works are the art itself, as whatever the image was before is almost always completely obscured by the glitch. She has also created glitch art by circuitbending different devices, such as cameras. Much of her art is also described by her as digital collages.

Max Osiris has many works that draw on themes of psychedelic drugs. His works do not all necessarily use glitch techniques, but they do seem to have glitch-adjacent elements, such as collage techniques.

Jennifer Juniper Stratford was listed as a glitch artist in this article, but her work is almsot all retro-themed video art. While cool, I don't consider her to be a glitch artist, rather a video artist that is well-versed in the techniques video artists used throughout the 60's-90's.

Neurocolor makes works that seem to combine the different types of glitch art made by the artists previously mentioned in this list. His approach mixes the collage style with repetition and more traditional glitch aesthetics.

Kate the Cursed creates work that I would define as computer graphics or computer art, with glitch art sprinkled in. Her focus is primarily on 80s-90s themed graphics, with glitch art interrupting the rigid computer graphics she creates.

## Ďurišinová, M. (2026, February 6). 6 Types of Search Algorithms You Need to Know. Luigi’s Box. https://www.luigisbox.com/blog/types-of-search-algorithms/ 

Linear search
- iterates sequentially
- O(n) complexity
- good for unordered data, like image text
- Useful for sorting through image text: YES

Binary search
- splits lists in half until it finds the target
- O(log n) complexity
- good for ordered data
- Useful for sorting through image text: NO

Interpolation search
- a "smarter" version of binary search, where the search adjusts its position based on the value it was given to search for
- O(n log n)
- good for ordered data
- Useful for sorting through image text: NO

Jump search
- Checks every Kth number in the list. If it finds a value that is within K distance from the target, it uses linear search to try and find the target
- O($\sqrt{n}$)
- good for ordered data
- Useful for sorting through image text: NO

Exponential search
- similar to jump search, but the number to search by increases exponentially
- O(log n)
- good for ordered data
- Useful for sorting through image text: NO

Ternary search
- similar to binary search, but it splits the list into three rather than half
- requires more searches than binary search
- O($log_3$ n)
- Useful for sorting through image text: NO

Given the unordered nature of photo data loaded as text, linear search would be best for finding all instances of a specific value.

## Phil. (2016a, June 16). How to glitch images using Processing scripts. Datamoshing. http://datamoshing.com/2016/06/16/how-to-glitch-images-using-processing-scripts/ 
Instructions on how to loop through all the pixels in an image and interpolate a new colour for that pixel using its' old colour, plus a randomly generated colour. Interesting, but I want to play directly with the image in a text editor.

## Phil. (2016b, June 26). How to glitch images with WordPad. Datamoshing. http://datamoshing.com/2016/06/26/how-to-glitch-images-with-wordpad/ 
Apparently, even simply opening the image in WordPad and saving it without making any modifications will cause the image to glitch. First, they converted the image to a .bmp extension file, and then opened that in WordPad. I will try converting my images into a .txt and opening them in VSCode, then converting them back to images, so I can see if there is an 'inherent' glitch to opening an image as text. 

## Schnutzel. (2021). The program processing this data does. If you open a text file in an image viewer, it will try to [Comment on the blog post “I’ve always understood that computers work in binary. But programming languages use letters, numbers, symbols, and punctuation. How does the program get translated in binary that the computer understands?”] Reddit. https://www.reddit.com/r/explainlikeimfive/comments/o3jml9/comment/h2cchpj/ 
The way that images convert into text is not random, although it appears that way. It seems that the "random" output is determined by the binary data of the image - meaning, there must be a logical system that creates the random-seeming output text that the image gives us, in a means similar to homomorphism. This would imply that there is a way to identify the rules that are used to convert image binary into text, which is what makes me think that there may be a way to glitch images in a predictable manner. Hopefully, this project will help shed light on what these conversion patterns may be.