import os
import shutil

def move_folder_contents(from_path, to_path):
    shutil.copytree(from_path, to_path)
from_path = r'C:\Users\John Becker\Dropbox\Documents\School Stuff\UC Denver New Degree'
to_path = r'C:\Users\John Becker\Dropbox\Documents\School Stuff\UC Denver New Degree\Fall 2018\Operating Systems\Phoronix-Test-Suite\test'
move_folder_contents(from_path, to_path)
