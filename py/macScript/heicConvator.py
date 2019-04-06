import os
import subprocess
heic_dir = 'heic/'
jpg_dir = 'jpg/'

files = os.listdir(heic_dir)

for image in files:
    command = 'sips --setProperty format jpeg ' + heic_dir + image + ' --out ' + jpg_dir + image.replace('.heic', '.jpg')
    subprocess.call(command, shell=True)

