# face_recog
face recognition from the photos in the folder
First need to run the code encode.py and then face_recog.py for th ouput.

Basically of 2 programs 1st program takes the folder of images and encodes all the images in the folder and stores it in a file. 
The other program access the file and gives you the result. Every time you add a new photo you need to run the first program for initialization. 


encode.py gets all the encodings of all the photos in the folder 'faces' and saves in a file named encodings.npy
and face_recog.py reads the readings from the file encodings.npy so it'll be faster.
