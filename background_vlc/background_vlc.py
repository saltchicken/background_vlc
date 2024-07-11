import sys, argparse
import vlc
from PyQt5 import QtWidgets, QtCore, QtGui

class FramelessPlayer(QtWidgets.QWidget):
    def __init__(self, media_path, x=0, y=0, width=2560, height=1440, mute=True):
        super().__init__()

        # Set the window to be frameless
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Set the desired window size
        self.setGeometry(x, y, width, height)

        # Create an instance of VLC
        self.instance = vlc.Instance()

        # Create a media player
        self.player = self.instance.media_player_new()
        self.player.audio_set_mute(True)

        # Create a media object
        media = self.instance.media_new(media_path)
        self.player.set_media(media)

        # Create a video frame widget
        self.videoframe = QtWidgets.QFrame()
        self.videoframe.setStyleSheet("background-color: black;")

        # Create a layout and add the video frame
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.videoframe)
        self.setLayout(layout)

        # Set the media player to render to the video frame
        if sys.platform == "linux":
            self.player.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32":
            self.player.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin":
            self.player.set_nsobject(int(self.videoframe.winId()))

        # Bind the escape key to close the window
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self)
        self.shortcut.activated.connect(self.close)

        # Play the media
        self.player.play()

def main():
    parser = argparse.ArgumentParser(description="Automatically setup EBSynth.")
    
    parser.add_argument('-b', '--backend', default="pyqt5", help='Backend to use')
    parser.add_argument('-f', '--folder', help='Folder for playlist')
    parser.add_argument('-v', '--video', help='Path of video to play')
    parser.add_argument('-x', '--horizontal_position', type=int, default=0, help='Horizontal position of video window')
    parser.add_argument('-y', '--vertical_position', type=int, default=0, help='Vertical position of video window')
    parser.add_argument('--width', default=2560, type=int, help='Width of video window')
    parser.add_argument('--height', default=1440, type=int, help='Height of video window')
    
    # parser.add_argument('--flag', action='store_true', help='Optional flag')
    
    args = parser.parse_args()
    
    if args.backend == "pyqt5":
        app = QtWidgets.QApplication(sys.argv)
        player = FramelessPlayer(args.video, args.horizontal_position, args.vertical_position, args.width, args.height)
        player.show()
        sys.exit(app.exec_())
        player = FramelessPlayer(args.video)
            
if __name__ == "__main__":
    main()