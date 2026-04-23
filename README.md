# ARTH 251 Final Project
Hannah Kostuk

sak675 

11318046

## Files in this Repo
| File Name | Description |
| -------- | -------- |
| README.md | Statement on technology used, references, feedback type. Recommended to view with a markdown previewer  |
| notes.md  | Notes from references, completed before I wrote main.py. Recommended to view with a markdown previewer |
| main.py  | The file to run the code from |
| real5.jpg | A preset image for glitching. Photo is by Hannah Kostuk |
| wisdomteeth.jpg | A preset image for glitching. Photo is by Hannah Kostuk |
| preset-1| A directory containing pre-glitched images using glitch 1, in case you can't run the program yourself |
| preset-2| A directory containing pre-glitched images using glitch 2, in case you can't run the program yourself |
| preset-3| A directory containing pre-glitched images using glitch 3, in case you can't run the program yourself |
| glitch1 | Where the photo series from glitch 1 is stored. Overwrites itself on each run.|
| glitch2 | Where the photo series from glitch 2 is stored. Overwrites itself on each run.|
| glitch3 | Where the photo series from glitch 3 is stored. Overwrites itself on each run.|
| glitchvid1.mp4 | Video version of the glitch1 photo series. Cannot open in VSCode - must run from file explorer.|
| glitchvid2.mp4 | Video version of the glitch2 photo series. Cannot open in VSCode - must run from file explorer.|
| glitchvid3.mp4 | Video version of the glitch3 photo series. Cannot open in VSCode - must run from file explorer.|

## How to Use
1. Clone this repo if you don't already have a copy (in terminal: git clone https://git.cs.usask.ca/sak675/arth-glitch.git).
2. Open arth-glitch in VSCode (or some other code editor - this is just what I use and what I know works).
3. Open main.py.
4. If "import cv2" has a warning squiggle under it:
    1. On Windows, hit CTRL + ` to open the integrated terminal
    2. In terminal, type: pip install opencv-python
    3. Hit enter. It should download the package
5. Hit CTRL + F5 to run main.py.
6. Instructions on how to use the main program will write out to the terminal (which should open automatically). Comments within the code explain how each glitch effect works, and what I did to create them.
7. You may see messages in the terminal like "Corrupt JPEG data: premature end of data segment", "[ WARN:0@0.508] global cap_ffmpeg_impl.hpp:2774 writeFrame write frame skipped - expected 3 channels but got 1", "[ WARN:0@0.508] global cap_ffmpeg.cpp:218 write FFmpeg: Failed to write frame", or something else similar. This is just the video library complaining about working with corrupted image files - this is normal and will not disrupt how the program runs.
8. To watch the resultant videos from each glitch method, right-click on the file name in the VSCode file explorer, and click "Reveal in File Explorer". This will open your computer files. Click on the video there to view them.

## Feedback Type: B

## Statement on Technology Used
| Name of Technology | Use Case |
| -------- | -------- |
| Firefox  | Web browser  |
| VSCode   | Code editor  |
| Google   | Search engine |
| File Explorer   | For sifting through my files quickly |
| Media Player   | For watching the videos (can't open them in VSCode, must find them via file explorer and then open in media player) |

## References

Dab. (2024, August 1). 10 Digital Artists: The Best of Glitch art. DIGITAL ARTS BLOG. https://www.digitalartsblog.com/artist-spotlights/glitch-art 

Ďurišinová, M. (2026, February 6). 6 Types of Search Algorithms You Need to Know. Luigi’s Box. https://www.luigisbox.com/blog/types-of-search-algorithms/ 

Getting Started with Videos. OpenCV. (n.d.). https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html 

Moukthika. (2025, March 28). Reading and writing videos using opencv. OpenCV. https://opencv.org/reading-and-writing-videos-using-opencv/ 

Phil. (2016a, June 16). How to glitch images using Processing scripts. Datamoshing. http://datamoshing.com/2016/06/16/how-to-glitch-images-using-processing-scripts/ 

Phil. (2016b, June 26). How to glitch images with WordPad. Datamoshing. http://datamoshing.com/2016/06/26/how-to-glitch-images-with-wordpad/ 

Schnutzel. (2021). The program processing this data does. If you open a text file in an image viewer, it will try to [Comment on the blog post “I’ve always understood that computers work in binary. But programming languages use letters, numbers, symbols, and punctuation. How does the program get translated in binary that the computer understands?”] Reddit. https://www.reddit.com/r/explainlikeimfive/comments/o3jml9/comment/h2cchpj/ 