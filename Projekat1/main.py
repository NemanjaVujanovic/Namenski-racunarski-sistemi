from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pytube import YouTube, Playlist
from tkinter import messagebox
import sys

class YouTube_Mp3_Mp4_Downloader(object):
    def main(self, MainWindow):
        def text_changed():
            try:
                self.lineEdit.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
        "selection-background-color: rgb(50, 50, 50);\n")
                
                user_input = self.lineEdit.text()    
                urls = []
                mp3_quality = []
                mp4_quality = []
                              
                for url in user_input.split("\n"):
                    urls.append(url)

                self.comboBox.clear()    

                for i in range(len(urls)):
                    youtube = YouTube(urls[i])

                    audios = youtube.streams.filter(only_audio=True).order_by('abr').desc()
                    videos = youtube.streams.filter(progressive=True).order_by('resolution').desc()            

                    for audio in audios:
                        self.comboBox.addItem(".mp3 (Audio) " + audio.abr)
                        mp3_quality.append(audio.abr)

                    for video in videos:
                        self.comboBox.addItem(".mp4 (Video) " + video.resolution)
                        mp4_quality.append(video.resolution)

                self.mp3_quality = mp3_quality
                self.mp4_quality = mp4_quality
            
            except:
                self.comboBox.addItem(".mp3 (Audio)")
                self.comboBox.addItem(".mp4 (Video)")
        
        def button_clicked():
            def input_exception():
                self.lineEdit.setText("")
                self.lineEdit.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
    "selection-background-color: rgb(50, 50, 50);\n" "color: rgb(255, 0, 0);\n" "border: 2px solid red;")
                self.progressBar.setProperty("value", 0)

            def download_exception():
                self.lineEdit.setText("") 
                self.progressBar.setProperty("value", 0)
                
            def download_started():
                self.progressBar.setProperty("value", 10) 
                self.progressBar.setProperty("value", 20)   
                
            def download_progress():
                self.progressBar.setProperty("value", 40)
                self.progressBar.setProperty("value", 50)
                self.progressBar.setProperty("value", 60)            

            def download_finishing():
                self.progressBar.setProperty("value", 70)
                self.progressBar.setProperty("value", 80)
                self.progressBar.setProperty("value", 90)
                self.progressBar.setProperty("value", 100)
            
            def audio_download_completed():
                messagebox.showinfo("YouTube Mp3/Mp4 Downloader", "Mp3 download completed!")

            def video_download_completed():
                messagebox.showinfo("YouTube Mp3/Mp4 Downloader", "Mp4 download completed!")

            def audio_playlist_download_completed():
                messagebox.showinfo("YouTube Mp3/Mp4 Downloader", "Mp3 playlist download completed!")

            def video_playlist_download_completed():
                messagebox.showinfo("YouTube Mp3/Mp4 Downloader", "Mp4 playlist download completed!")                
            
            def download_mp3():
                try:                 
                    urls = []
                      
                    for url in user_input.split("\n"):
                        urls.append(url)

                    destination = ""    

                    for i in range(len(urls)):                    
                        youtube = YouTube(urls[i])
                        
                        download_started()

                        if (self.comboBox.currentText().endswith(self.mp3_quality[0])):
                            audio = youtube.streams.filter(only_audio=True, abr=self.mp3_quality[0]).first()
                            
                        elif (self.comboBox.currentText().endswith(self.mp3_quality[1])):                        
                            audio = youtube.streams.filter(only_audio=True, abr=self.mp3_quality[1]).first()

                        elif (self.comboBox.currentText().endswith(self.mp3_quality[2])):                        
                            audio = youtube.streams.filter(only_audio=True, abr=self.mp3_quality[2]).first()

                        elif (self.comboBox.currentText().endswith(self.mp3_quality[3])):                        
                            audio = youtube.streams.filter(only_audio=True, abr=self.mp3_quality[3]).first()    
                            
                        else:                        
                            audio = youtube.streams.filter(only_audio=True, abr=self.mp3_quality[4]).first()
                        
                        self.progressBar.setProperty("value", 30)                                                
                            
                        if (i == 0):
                            youtube_title = youtube.title
                            specialChars = """\/:*?"<>|"""

                            for char in specialChars:
                                if (char in youtube_title):
                                    youtube_title = youtube_title.replace(char, "")
                                    
                            file_save = QFileDialog.getSaveFileName(None, "Save As", youtube_title, "Audio (*.mp3)")   

                            if (len(file_save[0]) > 0):
                                download_progress()
                                        
                                destination_help1 = file_save[0][::-1]
                                destination_help2 = file_save[0][::-1]
                                        
                                for j in range(len(destination_help1)):
                                    if (destination_help1[j] == "/"):
                                        destination_help1 = destination_help1[j:]
                                        break
                                            
                                for k in range(len(destination_help2)):
                                    if (destination_help2[k] == "/"):
                                        destination_help2 = destination_help2[:k]
                                        break
                                            
                                destination = destination_help1[::-1]
                                file_name = destination_help2[::-1]                         
                                
                                audio.download(output_path=destination, filename=file_name)
                                
                                download_finishing()                          
                                
                            else:
                                download_exception()
                                
                        else:                            
                            if (len(destination) > 0):  
                                download_progress()

                                youtube_title = youtube.title
                                specialChars = """\/:*?"<>|"""

                                for char in specialChars:
                                    if (char in youtube_title):
                                        youtube_title = youtube_title.replace(char, "")                                        
                                  
                                audio.download(output_path=destination, filename=youtube_title+".mp3")                                
                                download_finishing()
                                
                            else:
                                download_exception()
                                break
                            
                    if (len(destination) > 0):
                        audio_download_completed()
                    
                except:
                    input_exception()

            def download_mp4():
                try:
                    urls = []
                      
                    for url in user_input.split("\n"):
                        urls.append(url)

                    destination = ""     

                    for i in range(len(urls)):                    
                        youtube = YouTube(urls[i])
                        
                        download_started()

                        if (self.comboBox.currentText().endswith(self.mp4_quality[0])):
                            video = youtube.streams.filter(progressive=True, resolution=self.mp4_quality[0]).first()
                            
                        elif (self.comboBox.currentText().endswith(self.mp4_quality[1])):                        
                            video = youtube.streams.filter(progressive=True, resolution=self.mp4_quality[1]).first()
                            
                        else:                        
                            video = youtube.streams.filter(progressive=True, resolution=self.mp4_quality[2]).first()
                        
                        self.progressBar.setProperty("value", 30)                                               
                            
                        if (i == 0):
                            youtube_title = youtube.title
                            specialChars = """\/:*?"<>|"""

                            for char in specialChars:
                                if (char in youtube_title):
                                    youtube_title = youtube_title.replace(char, "")
                            
                            file_save = QFileDialog.getSaveFileName(None, "Save As", youtube_title, "Video (*.mp4)")  

                            if (len(file_save[0]) > 0):
                                download_progress()
                                        
                                destination_help1 = file_save[0][::-1]
                                destination_help2 = file_save[0][::-1]
                                        
                                for j in range(len(destination_help1)):
                                    if (destination_help1[j] == "/"):
                                        destination_help1 = destination_help1[j:]
                                        break
                                            
                                for k in range(len(destination_help2)):
                                    if (destination_help2[k] == "/"):
                                        destination_help2 = destination_help2[:k]
                                        break
                                            
                                destination = destination_help1[::-1]                                
                                file_name = destination_help2[::-1]                         
                                
                                video.download(output_path=destination, filename=file_name)                                
                                
                                download_finishing()                          
                                
                            else:
                                download_exception()
                                
                        else:
                            if (len(destination) > 0):
                                download_progress()

                                youtube_title = youtube.title
                                specialChars = """\/:*?"<>|"""

                                for char in specialChars:
                                    if (char in youtube_title):
                                        youtube_title = youtube_title.replace(char, "")
                                    
                                video.download(output_path=destination, filename=youtube_title+".mp4")                            
                                    
                                download_finishing()

                            else:
                                download_exception()
                                break  
                            
                    if (len(destination) > 0):
                        video_download_completed()
                    
                except:
                    input_exception()                        

            def download_mp3_playlist():
                try:
                    url = user_input                                       
                    youtube = Playlist(url)                
                        
                    download_started()

                    youtube_title = youtube.title
                    specialChars = """\/:*?"<>|"""

                    for char in specialChars:
                        if (char in youtube_title):
                            youtube_title = youtube_title.replace(char, "")

                    file_save = QFileDialog.getSaveFileName(None, "Save As", youtube_title, "Audio (*.mp3)")              
                    
                    self.progressBar.setProperty("value", 30)             

                    if (len(file_save[0]) > 0):
                        download_progress()
                                
                        destination_help1 = file_save[0][::-1]
                        destination_help2 = file_save[0][::-1]
                                
                        for j in range(len(destination_help1)):
                            if (destination_help1[j] == "/"):
                                destination_help1 = destination_help1[j:]
                                break
                                    
                        for k in range(len(destination_help2)):
                            if (destination_help2[k] == "/"):
                                destination_help2 = destination_help2[:k]
                                break
                                    
                        destination = destination_help1[::-1]
                        file_name = destination_help2[::-1]

                        for audio in youtube.videos:
                            youtube_title = audio.title
                            specialChars = """\/:*?"<>|"""

                            for char in specialChars:
                                if (char in youtube_title):
                                    youtube_title = youtube_title.replace(char, "")
                            
                            audio.streams.filter(only_audio=True).order_by('abr').desc().first().download(
                                output_path=destination, filename=youtube_title+".mp3") 
                        
                        download_finishing()
                        
                        audio_playlist_download_completed()
                        
                    else:
                        download_exception()               
                    
                except:
                    download_mp3()        

            def download_mp4_playlist():
                try:
                    url = user_input                                       
                    youtube = Playlist(url)                
                        
                    download_started()

                    youtube_title = youtube.title
                    specialChars = """\/:*?"<>|"""

                    for char in specialChars:
                        if (char in youtube_title):
                            youtube_title = youtube_title.replace(char, "")
                    
                    file_save = QFileDialog.getSaveFileName(None, "Save As", youtube_title, "Video (*.mp4)")

                    self.progressBar.setProperty("value", 30)
                    
                    if (len(file_save[0]) > 0):
                        download_progress()
                                
                        destination_help1 = file_save[0][::-1]
                        destination_help2 = file_save[0][::-1]
                                
                        for j in range(len(destination_help1)):
                            if (destination_help1[j] == "/"):
                                destination_help1 = destination_help1[j:]
                                break
                                    
                        for k in range(len(destination_help2)):
                            if (destination_help2[k] == "/"):
                                destination_help2 = destination_help2[:k]
                                break
                                    
                        destination = destination_help1[::-1]
                        file_name = destination_help2[::-1]

                        for video in youtube.videos:
                            youtube_title = video.title
                            specialChars = """\/:*?"<>|"""

                            for char in specialChars:
                                if (char in youtube_title):
                                    youtube_title = youtube_title.replace(char, "")
                            
                            video.streams.filter(progressive=True).order_by('resolution').desc().first().download(
                                output_path=destination, filename=youtube_title+".mp4") 

                        download_finishing()
                        
                        video_playlist_download_completed()
                        
                    else:
                        download_exception()
                        
                except:                    
                    download_mp4()        
               
            if (self.pushButton.isChecked() == True):
                user_input = self.lineEdit.text()
                
                if (len(user_input) < 1):                    
                    input_exception()                   
                    self.pushButton.toggle()
                    
                else:
                    if (self.comboBox.currentText().startswith(".mp3 (Audio)")):
                        download_mp3_playlist()
                        self.pushButton.toggle()
                        
                    else:
                        download_mp4_playlist()
                        self.pushButton.toggle()                     
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pictures/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout_1 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_1.setContentsMargins(25, 0, 25, 10)
        self.gridLayout_1.setHorizontalSpacing(0)
        self.gridLayout_1.setVerticalSpacing(10)
        self.gridLayout_1.setObjectName("gridLayout_1")
        
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 50))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(50, 50, 50);\n" "color: rgb(255, 255, 255);\n" "border-radius: 10;\n")
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(button_clicked) 
        
        self.gridLayout_7.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_1.addLayout(self.gridLayout_7, 3, 0, 1, 3)
        
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 30))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
"    background-color: rgb(50, 50, 50);\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        
        self.gridLayout_8.addWidget(self.progressBar, 0, 0, 1, 1)
        self.gridLayout_1.addLayout(self.gridLayout_8, 4, 0, 1, 3)
        
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 50))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 50))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.comboBox.setFont(font)
        self.comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(50, 50, 50);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        self.gridLayout_6.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout_1.addLayout(self.gridLayout_6, 2, 0, 1, 3)
        
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(400, 200))
        self.label.setMaximumSize(QtCore.QSize(400, 200))        
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pictures/youtube.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_1.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 100))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("selection-color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(50, 50, 50);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(text_changed)
        self.lineEdit.editingFinished.connect(button_clicked)
        
        self.gridLayout_5.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout_1.addLayout(self.gridLayout_5, 1, 0, 1, 3)

        mp3_quality = []
        mp4_quality = []
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Mp3/Mp4 Downloader"))        
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Paste YouTube URL/s here:"))
        self.comboBox.setItemText(0, _translate("MainWindow", ".mp3 (Audio)"))
        self.comboBox.setItemText(1, _translate("MainWindow", ".mp4 (Video)"))
        self.pushButton.setText(_translate("MainWindow", "Download"))
        
if __name__ == "__main__":    
    application = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    ui = YouTube_Mp3_Mp4_Downloader()
    ui.main(MainWindow)
    
    MainWindow.show()
    sys.exit(application.exec_())