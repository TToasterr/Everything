import os
import glob

pngs = glob.glob('*.png')
jpgs = glob.glob('*.jpg')
jpegs = glob.glob('*.jpeg')
mdps = glob.glob('*.mdp')
gifs = glob.glob('*.gif')

i = 0

for png in pngs:
    i += 1
    os.rename(png, '%s.png' % ('a' * i))

for jpg in jpgs:
    i += 1
    os.rename(jpg, '%s.jpg' % ('a' * i))

for jpeg in jpegs:
    i += 1
    os.rename(jpeg, '%s.jpeg' % ('a' * i))

for mdp in mdps:
    i += 1
    os.rename(mdp, '%s.mdp' % ('a' * i))

for gif in gifs:
    i += 1
    os.rename(gif, '%s.gif' % ('a' * i))
