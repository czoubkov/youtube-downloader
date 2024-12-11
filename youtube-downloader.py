import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import subprocess as sp

# import dependencies



class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("YouTube to MP3 (yt-dlp GUI)")

        # Set Vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # Create a label
        my_label = qtw.QLabel("Enter the YouTube URL")
        # Change the font size of the label
        my_label.setFont(qtg.QFont('Helvetica', 16))
        self.layout().addWidget(my_label)

        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("youtube_url_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # Create a button
        my_button = qtw.QPushButton("Download", 
                                    clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        # Show the app
        self.show()

        def press_it():
            youtube_url = my_entry.text()
            sp.run(["yt-dlp", "--extract-audio", "--audio-format", "mp3", "-i", youtube_url])

app = qtw.QApplication([])
mw = MainWindow()

# Run the app
app.exec_()