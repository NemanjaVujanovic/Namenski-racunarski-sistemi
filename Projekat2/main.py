from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from pygame import mixer
from PyQt5.QtWidgets import QMessageBox
import sys, random, pickle, os

class SlotMasina(object):
    ulozen_novac = 0
    osvojen_novac_nova_suma = 200
    osvojen_novac_stara_suma = osvojen_novac_nova_suma
    dobitna_kombinacija = [0, 0, 0]
    kliknuto_ulog = 1
    kliknuto_audio = 1

    if os.path.exists("rezultat.dat"):
        fajl = open("rezultat.dat", "rb")
        sadrzaj_fajla = pickle.load(fajl)
        fajl.close()
        
        rezultati = sadrzaj_fajla.split("\n")

        ulozen_novac = int(rezultati[0])
        osvojen_novac_nova_suma = int(rezultati[1])
        osvojen_novac_stara_suma = int(rezultati[2])
        kliknuto_ulog = int(rezultati[3])
        kliknuto_audio = int(rezultati[4])
        
    def setupUi(self, ceo_ekran):
        slotMasina = SlotMasina()
        
        def sacuvaj_rezultat():
            if (uzmiUlozenNovac() > 0 or uzmiOsvojenNovacNovaSuma() > 0):
                fajl = open("rezultat.dat", "wb")
                
                string = str(uzmiUlozenNovac()) + "\n" + str(uzmiOsvojenNovacNovaSuma()) + "\n" + str(uzmiOsvojenNovacStaraSuma()) + "\n" + str(uzmiBrojKliknutihUlog()) + "\n" + str(uzmiBrojKliknutihAudio())

                pickle.dump(string, fajl)
                fajl.close()
            else:
                obrisi_rezultat()

        def obrisi_rezultat():
            if os.path.exists("rezultat.dat"):
                os.remove("rezultat.dat")
        
        def napusti_aplikaciju():
            sys.exit(aplikacija.exec_())
        
        def postavi_audio():            
            if (uzmiBrojKliknutihAudio() == 1):
                self.podesavanje_audio.setIcon(QtGui.QIcon("Slike/audio-ukljucen.jpg"))
            else:
                self.podesavanje_audio.setIcon(QtGui.QIcon("Slike/audio-iskljucen.jpg"))
                postaviBrojKliknutihAudio(0)
                 
            postaviBrojKliknutihAudio(uzmiBrojKliknutihAudio() + 1)
        
        def spin():
            if (uzmiUlozenNovac() > 0):
                self.podesavanje_audio.setEnabled(False)
                self.rucica.setEnabled(False)
                self.resetuj.setEnabled(False)
                self.prikazi_pravila.setEnabled(False)
                self.ulozi_jedan.setEnabled(False)
                self.ulozi_sve.setEnabled(False)
                self.audio.setEnabled(False)
                self.spin.setEnabled(False)
                self.reset.setEnabled(False)
                self.pravila.setEnabled(False)
                self.jedan.setEnabled(False)
                self.sve.setEnabled(False)
                self.sacuvaj.setEnabled(False)

                self.rucica_gore.setPixmap(QtGui.QPixmap(""))
                self.rucica_dole.setPixmap(QtGui.QPixmap("Slike/rucica-dole.png"))
                
                postaviZvuk("spin")
                
                IKONICE = (1, 2, 3, 4, 5, 6, 7, 8, 9)
                POLJA = (self.polje_1, self.polje_2, self.polje_3)

                for i in range(3):
                    element = random.choice(IKONICE)
                    odabir_racunara = "Slike/ikonica" + str(element) + ".jpg"
                    
                    animacija = QtGui.QMovie("Animacije/animacija.gif")
                    POLJA[i].setMovie(animacija)
                    animacija.start()
                    
                    QtTest.QTest.qWait(1250)
                    POLJA[i].setPixmap(QtGui.QPixmap(odabir_racunara))
                    
                    postaviDobitnuKombinaciju(i, element)

                if (uzmiDobitnuKombinaciju()[0] == uzmiDobitnuKombinaciju()[1] and
                    uzmiDobitnuKombinaciju()[1] == uzmiDobitnuKombinaciju()[2]):
                    postaviZvuk("jackpot")
                    
                    if (uzmiDobitnuKombinaciju()[0] == 1):
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 80 * uzmiUlozenNovac())
                    elif (uzmiDobitnuKombinaciju()[0] == 6):
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 40 * uzmiUlozenNovac())
                    elif (uzmiDobitnuKombinaciju()[0] == 8):
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 25 * uzmiUlozenNovac())
                    else:
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 10 * uzmiUlozenNovac())
                    
                elif (uzmiDobitnuKombinaciju()[0] == uzmiDobitnuKombinaciju()[1] or
                      uzmiDobitnuKombinaciju()[0] == uzmiDobitnuKombinaciju()[2] or
                      uzmiDobitnuKombinaciju()[1] == uzmiDobitnuKombinaciju()[2]):
                    postaviZvuk("dobitak")

                    if (uzmiDobitnuKombinaciju()[0] == 1 and uzmiDobitnuKombinaciju()[1] == 1 or
                      uzmiDobitnuKombinaciju()[0] == 1 and uzmiDobitnuKombinaciju()[2] == 1 or
                      uzmiDobitnuKombinaciju()[1] == 1 and uzmiDobitnuKombinaciju()[2] == 1):
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 8 * uzmiUlozenNovac())
                        
                    elif (uzmiDobitnuKombinaciju()[0] == 6 and uzmiDobitnuKombinaciju()[1] == 6 or
                      uzmiDobitnuKombinaciju()[0] == 6 and uzmiDobitnuKombinaciju()[2] == 6 or
                      uzmiDobitnuKombinaciju()[1] == 6 and uzmiDobitnuKombinaciju()[2] == 6):
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 7 * uzmiUlozenNovac())
                        
                    elif (uzmiDobitnuKombinaciju()[0] == 8 and uzmiDobitnuKombinaciju()[1] == 8 or
                      uzmiDobitnuKombinaciju()[0] == 8 and uzmiDobitnuKombinaciju()[2] == 8 or
                      uzmiDobitnuKombinaciju()[1] == 8 and uzmiDobitnuKombinaciju()[2] == 8):
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 6 * uzmiUlozenNovac())
                        
                    else:
                        postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacNovaSuma() + 5 * uzmiUlozenNovac())
                    
                postaviOsvojenNovacStaraSuma(uzmiOsvojenNovacNovaSuma())
                    
                postaviUlozenNovac(0)
                postaviBrojKliknutihUlog(1)
                self.ulozeno.setText("Uloženo: " + str(uzmiUlozenNovac()) + "$")
                self.osvojeno.setText("Osvojeno: " + str(uzmiOsvojenNovacNovaSuma()) + "$")

                if (uzmiOsvojenNovacNovaSuma() == 0):
                    self.rucica.setEnabled(False)
                    self.resetuj.setEnabled(False)
                    self.ulozi_jedan.setEnabled(False)
                    self.ulozi_sve.setEnabled(False)
                    self.spin.setEnabled(False)
                    self.reset.setEnabled(False)
                    self.jedan.setEnabled(False)
                    self.sve.setEnabled(False)
                    self.sacuvaj.setEnabled(False)
                else:
                    self.rucica.setEnabled(True)
                    self.resetuj.setEnabled(True)
                    self.ulozi_jedan.setEnabled(True)
                    self.ulozi_sve.setEnabled(True)
                    self.spin.setEnabled(True)
                    self.reset.setEnabled(True)
                    self.jedan.setEnabled(True)
                    self.sve.setEnabled(True)
                    self.sacuvaj.setEnabled(True)
                    
            self.podesavanje_audio.setEnabled(True)
            self.prikazi_pravila.setEnabled(True)
            self.audio.setEnabled(True)
            self.pravila.setEnabled(True)

            self.rucica_dole.setPixmap(QtGui.QPixmap(""))
            self.rucica_gore.setPixmap(QtGui.QPixmap("Slike/rucica-gore.png"))
            
        def reset():
            postaviUlozenNovac(0)
            postaviOsvojenNovacNovaSuma(uzmiOsvojenNovacStaraSuma())
            postaviBrojKliknutihUlog(1)
            
            string = "Uloženo: 0$"
            
            if (self.ulozeno.text() != string):
                self.ulozeno.setText("Uloženo: " + str(uzmiUlozenNovac()) + "$")
                self.osvojeno.setText("Osvojeno: " + str(uzmiOsvojenNovacNovaSuma()) + "$")

        def prikazi_pravila():
            popup_prozor = QMessageBox()

            popup_prozor.setWindowIcon(QtGui.QIcon("Slike/logo.jpg"))
            popup_prozor.setIconPixmap(QtGui.QPixmap("Slike/pravila.jpg"))
            popup_prozor.setWindowTitle("Pravila igre ©")
            
            popup_prozor.setText("")
            popup_prozor.setStandardButtons(QMessageBox.Ok)
              
            popup_prozor.exec_()

        def ulozi_jedan():
            if (uzmiOsvojenNovacNovaSuma() > 0):
                self.novcic.setPixmap(QtGui.QPixmap("Slike/novcic.png"))
                self.novcic.setScaledContents(True)
                ubaciNovcic()
            
                postaviUlozenNovac(1 * uzmiBrojKliknutihUlog())
                oduzmiNovac(uzmiUlozenNovac(), uzmiOsvojenNovacStaraSuma())
                
                self.ulozeno.setText("Uloženo: " + str(uzmiUlozenNovac()) + "$")
                self.osvojeno.setText("Osvojeno: " + str(uzmiOsvojenNovacNovaSuma()) + "$")

                postaviBrojKliknutihUlog(1 + uzmiBrojKliknutihUlog())

        def ulozi_sve():
            if (uzmiOsvojenNovacNovaSuma() > 0):
                self.novcic.setPixmap(QtGui.QPixmap("Slike/novcic.png"))
                self.novcic.setScaledContents(True)
                ubaciNovcic()

                postaviUlozenNovac(uzmiUlozenNovac() + uzmiOsvojenNovacNovaSuma())

                self.ulozeno.setText("Uloženo: " + str(uzmiUlozenNovac()) + "$")
                postaviOsvojenNovacNovaSuma(0)
                self.osvojeno.setText("Osvojeno: " + str(uzmiOsvojenNovacNovaSuma()) + "$")
            
        def ubaciNovcic():
            postaviZvuk("novcic")
            QtTest.QTest.qWait(500)
            self.novcic.setPixmap(QtGui.QPixmap(""))

        def postaviUlozenNovac(ulozen_novac):
            slotMasina.ulozen_novac = ulozen_novac

        def postaviOsvojenNovacNovaSuma(osvojen_novac_nova_suma):
            slotMasina.osvojen_novac_nova_suma = osvojen_novac_nova_suma
            
        def postaviOsvojenNovacStaraSuma(osvojen_novac_stara_suma):
            slotMasina.osvojen_novac_stara_suma = osvojen_novac_stara_suma

        def postaviDobitnuKombinaciju(indeks, element):
            slotMasina.dobitna_kombinacija[indeks] = element

        def postaviBrojKliknutihUlog(brojac):
            slotMasina.kliknuto_ulog = brojac

        def postaviBrojKliknutihAudio(brojac):
            slotMasina.kliknuto_audio = brojac

        def uzmiUlozenNovac():
            return slotMasina.ulozen_novac

        def uzmiOsvojenNovacNovaSuma():
            return slotMasina.osvojen_novac_nova_suma

        def uzmiOsvojenNovacStaraSuma():
            return slotMasina.osvojen_novac_stara_suma

        def uzmiDobitnuKombinaciju():
            return slotMasina.dobitna_kombinacija

        def uzmiBrojKliknutihUlog():
            return slotMasina.kliknuto_ulog

        def uzmiBrojKliknutihAudio():
            return slotMasina.kliknuto_audio 

        def oduzmiNovac(ulozen_novac, osvojen_novac_nova_suma):
            postaviOsvojenNovacNovaSuma(osvojen_novac_nova_suma - ulozen_novac)

        def postaviZvuk(zvuk):
            if (uzmiBrojKliknutihAudio() != 1):
                mixer.init()
                mixer.music.load("Animacije/" + zvuk + ".mp3")
                mixer.music.play()

        def proveriAudio():
            if (uzmiBrojKliknutihAudio() == 1):
                self.podesavanje_audio.setIcon(QtGui.QIcon("Slike/audio-iskljucen.jpg"))
            else:
                self.podesavanje_audio.setIcon(QtGui.QIcon("Slike/audio-ukljucen.jpg"))
                postaviBrojKliknutihAudio(0)
            
        ceo_ekran.setObjectName("ceo_ekran")
        ceo_ekran.setFixedSize(1024, 790)
        
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Slike/logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ceo_ekran.setWindowIcon(icon1)
        
        self.centralni_vidzet = QtWidgets.QWidget(ceo_ekran)
        self.centralni_vidzet.setObjectName("centralni_vidzet")
        
        self.slika_slot_masine = QtWidgets.QLabel(self.centralni_vidzet)
        self.slika_slot_masine.setGeometry(QtCore.QRect(0, 0, 1024, 768))
        self.slika_slot_masine.setText("")
        self.slika_slot_masine.setPixmap(QtGui.QPixmap("Slike/slot-masina.jpg"))
        self.slika_slot_masine.setScaledContents(True)
        self.slika_slot_masine.setObjectName("slika_slot_masine")
        
        self.podesavanje_audio = QtWidgets.QPushButton(self.centralni_vidzet)
        self.podesavanje_audio.setGeometry(QtCore.QRect(970, 5, 50, 50))
        self.podesavanje_audio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.podesavanje_audio.setText("")
        
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Slike/audio-iskljucen.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.podesavanje_audio.setIcon(icon2)
        self.podesavanje_audio.setIconSize(QtCore.QSize(50, 50))
        self.podesavanje_audio.setFlat(True)
        self.podesavanje_audio.setObjectName("podesavanje_audio")
        self.podesavanje_audio.clicked.connect(postavi_audio) 
        
        self.polje_1 = QtWidgets.QLabel(self.centralni_vidzet)
        self.polje_1.setGeometry(QtCore.QRect(274, 290, 137, 105))
        self.polje_1.setText("")
        self.polje_1.setPixmap(QtGui.QPixmap("Slike/ikonica1.jpg"))
        self.polje_1.setScaledContents(True)
        self.polje_1.setObjectName("polje_1")
        
        self.polje_2 = QtWidgets.QLabel(self.centralni_vidzet)
        self.polje_2.setGeometry(QtCore.QRect(445, 290, 137, 105))
        self.polje_2.setText("")
        self.polje_2.setPixmap(QtGui.QPixmap("Slike/ikonica1.jpg"))
        self.polje_2.setScaledContents(True)
        self.polje_2.setObjectName("polje_2")
        
        self.polje_3 = QtWidgets.QLabel(self.centralni_vidzet)
        self.polje_3.setGeometry(QtCore.QRect(615, 290, 137, 105))
        self.polje_3.setText("")
        self.polje_3.setPixmap(QtGui.QPixmap("Slike/ikonica1.jpg"))
        self.polje_3.setScaledContents(True)
        self.polje_3.setObjectName("polje_3")
        
        self.rucica = QtWidgets.QPushButton(self.centralni_vidzet)
        self.rucica.setGeometry(QtCore.QRect(895, 265, 50, 175))
        self.rucica.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.rucica.setText("")
        self.rucica.setStyleSheet("background: transparent;")
        self.rucica.setObjectName("rucica")
        self.rucica.clicked.connect(spin)
        
        self.resetuj = QtWidgets.QPushButton(self.centralni_vidzet)
        self.resetuj.setGeometry(QtCore.QRect(200, 470, 120, 80))
        self.resetuj.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetuj.setText("")
        self.resetuj.setStyleSheet("background: transparent;")
        self.resetuj.setObjectName("resetuj")
        self.resetuj.clicked.connect(reset) 
        
        self.prikazi_pravila = QtWidgets.QPushButton(self.centralni_vidzet)
        self.prikazi_pravila.setGeometry(QtCore.QRect(340, 470, 120, 80))
        self.prikazi_pravila.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.prikazi_pravila.setText("")
        self.prikazi_pravila.setStyleSheet("background: transparent;")
        self.prikazi_pravila.setObjectName("prikazi_pravila")
        self.prikazi_pravila.clicked.connect(prikazi_pravila) 
        
        self.ulozi_jedan = QtWidgets.QPushButton(self.centralni_vidzet)
        self.ulozi_jedan.setGeometry(QtCore.QRect(490, 470, 120, 80))
        self.ulozi_jedan.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ulozi_jedan.setText("")
        self.ulozi_jedan.setStyleSheet("background: transparent;")
        self.ulozi_jedan.setObjectName("ulozi_jedan")
        self.ulozi_jedan.clicked.connect(ulozi_jedan) 
        
        self.ulozi_sve = QtWidgets.QPushButton(self.centralni_vidzet)
        self.ulozi_sve.setGeometry(QtCore.QRect(640, 470, 120, 80))
        self.ulozi_sve.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ulozi_sve.setText("")
        self.ulozi_sve.setStyleSheet("background: transparent;")
        self.ulozi_sve.setObjectName("ulozi_sve")
        self.ulozi_sve.clicked.connect(ulozi_sve) 

        self.novcic = QtWidgets.QLabel(self.centralni_vidzet)
        self.novcic.setGeometry(QtCore.QRect(762, 480, 70, 70))
        self.novcic.setText("")
        self.novcic.setObjectName("novcic")

        self.ulozeno = QtWidgets.QLabel(self.centralni_vidzet)
        self.ulozeno.setGeometry(QtCore.QRect(10, 710, 495, 50))
        
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.ulozeno.setFont(font)
        self.ulozeno.setObjectName("ulozeno")

        self.osvojeno = QtWidgets.QLabel(self.centralni_vidzet)
        self.osvojeno.setGeometry(QtCore.QRect(522, 710, 495, 50))
        
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        
        self.osvojeno.setFont(font)
        self.osvojeno.setObjectName("osvojeno")

        self.rucica_gore = QtWidgets.QLabel(self.centralni_vidzet)
        self.rucica_gore.setGeometry(QtCore.QRect(880, 255, 75, 200))
        self.rucica_gore.setText("")
        self.rucica_gore.setPixmap(QtGui.QPixmap("Slike/rucica-gore.png"))
        self.rucica_gore.setScaledContents(True)
        self.rucica_gore.setObjectName("rucica_gore")
        
        self.rucica_dole = QtWidgets.QLabel(self.centralni_vidzet)
        self.rucica_dole.setGeometry(QtCore.QRect(880, 422, 75, 200))
        self.rucica_dole.setText("")
        self.rucica_dole.setPixmap(QtGui.QPixmap(""))
        self.rucica_dole.setScaledContents(True)
        self.rucica_dole.setObjectName("rucica_dole")
        
        self.meniBar = QtWidgets.QMenuBar(ceo_ekran)
        self.meniBar.setGeometry(QtCore.QRect(0, 0, 1024, 26))
        self.meniBar.setObjectName("meniBar")
        
        self.meniOpcije = QtWidgets.QMenu(self.meniBar)
        self.meniOpcije.setObjectName("meniOpcije")        
        ceo_ekran.setMenuBar(self.meniBar)
        
        self.audio = QtWidgets.QAction(ceo_ekran)
        self.audio.setObjectName("audio")
        self.audio.triggered.connect(postavi_audio)
        
        self.spin = QtWidgets.QAction(ceo_ekran)
        self.spin.setObjectName("spin")
        self.spin.triggered.connect(spin)
        
        self.reset = QtWidgets.QAction(ceo_ekran)
        self.reset.setObjectName("reset")
        self.reset.triggered.connect(reset)
        
        self.pravila = QtWidgets.QAction(ceo_ekran)
        self.pravila.setObjectName("pravila")
        self.pravila.triggered.connect(prikazi_pravila)
        
        self.jedan = QtWidgets.QAction(ceo_ekran)
        self.jedan.setObjectName("jedan")
        self.jedan.triggered.connect(ulozi_jedan)
        
        self.sve = QtWidgets.QAction(ceo_ekran)
        self.sve.setObjectName("sve")
        self.sve.triggered.connect(ulozi_sve)
        
        self.sacuvaj = QtWidgets.QAction(ceo_ekran)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Slike/sacuvaj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sacuvaj.setIcon(icon3)
        self.sacuvaj.setObjectName("sacuvaj")
        self.sacuvaj.triggered.connect(sacuvaj_rezultat)
        
        self.obrisi = QtWidgets.QAction(ceo_ekran)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Slike/obrisi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.obrisi.setIcon(icon4)
        self.obrisi.setObjectName("obrisi")
        self.obrisi.triggered.connect(obrisi_rezultat)
        
        self.izlaz = QtWidgets.QAction(ceo_ekran)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("Slike/izlaz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.izlaz.setIcon(icon5)
        self.izlaz.setObjectName("izlaz")
        self.izlaz.triggered.connect(napusti_aplikaciju)

        self.rucica.raise_()
        self.meniOpcije.addAction(self.audio)
        self.meniOpcije.addAction(self.spin)
        self.meniOpcije.addAction(self.reset)
        self.meniOpcije.addAction(self.pravila)
        self.meniOpcije.addAction(self.jedan)
        self.meniOpcije.addAction(self.sve)
        self.meniOpcije.addSeparator()
        self.meniOpcije.addAction(self.sacuvaj)
        self.meniOpcije.addAction(self.obrisi)
        self.meniOpcije.addAction(self.izlaz)
        self.meniBar.addAction(self.meniOpcije.menuAction())

        proveriAudio()
        
        ceo_ekran.setCentralWidget(self.centralni_vidzet)
        self.retranslateUi(ceo_ekran)
        QtCore.QMetaObject.connectSlotsByName(ceo_ekran)

    def retranslateUi(self, ceo_ekran):
        _translate = QtCore.QCoreApplication.translate
        ceo_ekran.setWindowTitle(_translate("ceo_ekran", "Slot Mašina © ¯\_(ツ)_/¯"))
        
        self.meniOpcije.setTitle(_translate("ceo_ekran", "Opcije"))
        self.audio.setText(_translate("ceo_ekran", "Audio"))
        self.audio.setShortcut(_translate("ceo_ekran", "A"))
        self.spin.setText(_translate("ceo_ekran", "Spin"))
        self.spin.setShortcut(_translate("ceo_ekran", "Z"))
        self.reset.setText(_translate("ceo_ekran", "Reset"))
        self.reset.setShortcut(_translate("ceo_ekran", "R"))
        self.pravila.setText(_translate("ceo_ekran", "Pravila"))
        self.pravila.setShortcut(_translate("ceo_ekran", "P"))
        self.jedan.setText(_translate("ceo_ekran", "Uloži jedan $"))
        self.jedan.setShortcut(_translate("ceo_ekran", "J"))
        self.sve.setText(_translate("ceo_ekran", "Uloži sve $"))
        self.sve.setShortcut(_translate("ceo_ekran", "S"))
        self.sacuvaj.setText(_translate("ceo_ekran", "Sačuvaj"))
        self.sacuvaj.setShortcut(_translate("ceo_ekran", "Ctrl+S"))
        self.obrisi.setText(_translate("ceo_ekran", "Obriši"))
        self.obrisi.setShortcut(_translate("ceo_ekran", "Ctrl+O"))
        self.izlaz.setText(_translate("ceo_ekran", "Izlaz"))
        self.izlaz.setShortcut(_translate("ceo_ekran", "Ctrl+I"))
        self.ulozeno.setText(_translate("ceo_ekran", "Uloženo: " + str(self.ulozen_novac) + "$"))
        self.osvojeno.setText(_translate("ceo_ekran", "Osvojeno: " + str(self.osvojen_novac_nova_suma) + "$"))

if __name__ == "__main__":
    aplikacija = QtWidgets.QApplication(sys.argv)
    ceo_ekran = QtWidgets.QMainWindow()
    
    ui = SlotMasina()
    ui.setupUi(ceo_ekran)
    
    ceo_ekran.show()
    sys.exit(aplikacija.exec_())
