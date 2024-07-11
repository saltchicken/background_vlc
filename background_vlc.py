import sys, argparse
import vlc
from PyQt5 import QtWidgets, QtCore, QtGui

def main():
    parser = argparse.ArgumentParser(description="Automatically setup EBSynth.")
    
    parser.add_argument('-f', '--folder', help='Folder for playlist')
    parser.add_argument('-v', '--video', help='Path of video to play')
    parser.add_argument('-x', '--horizontal_postition', default='0', help='Horizontal position of video window')
    parser.add_argument('-y', '--vertical_postition', default='0', help='Vertical position of video window')
    # parser.add_argument('--flag', action='store_true', help='Optional flag')
    
    args = parser.parse_args()
    
    print(args.folder)
    print(args.video)
    print(args.horizontal_position)
    print(args.vertical_position)
    
    
if __name__ == "__main__":
    main()