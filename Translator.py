import sys

from PIL import Image
import numpy as np

sentence= input("Please enter what you would like translated \n").lower()

alph_array=[]

#get list of all hand movements used in the word
for x in sentence:
    if x == ' ' :
        alph_array.append('Alphabet/space.png')
    else:
        alph_array.append('Alphabet/' + x + '.png')
print (alph_array)

#list of all images in our hand array
images= [Image.open(i) for i in alph_array]

#for t in images:
#    t.show()

sizeAr=[]
for t in images:
    sizeAr.append(t.size)

smallest= min(sizeAr)

print(smallest)

#for t in images:
#    t.resize(smallest)
#    print(t.size)
