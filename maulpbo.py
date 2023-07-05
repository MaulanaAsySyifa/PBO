from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QMessageBox, QFileDialog, QComboBox, QPushButton
from PyQt5.QtGui import QIcon, QFont
import sys


class AplikasiBukuHarian(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.editorTeks = QTextEdit()
        self.setCentralWidget(self.editorTeks)

        self.ukuranFontComboBox = QComboBox(self)
        self.ukuranFontComboBox.addItem('12')
        self.ukuranFontComboBox.addItem('14')
        self.ukuranFontComboBox.addItem('16')
        self.ukuranFontComboBox.addItem('18')
        self.ukuranFontComboBox.currentTextChanged.connect(self.ubahUkuranFont)
        self.toolbar = self.addToolBar('Font Size')
        self.toolbar.addWidget(self.ukuranFontComboBox)

        tombolBuka = QPushButton('Buka', self)
        tombolBuka.clicked.connect(self.bukaBukuHarian)
        tombolSimpan = QPushButton('Simpan', self)
        tombolSimpan.clicked.connect(self.simpanBukuHarian)

        self.toolbar.addWidget(tombolBuka)
        self.toolbar.addWidget(tombolSimpan)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Aplikasi Buku Harian')
        self.show()

    def bukaBukuHarian(self):
        namaBerkas, _ = QFileDialog.getOpenFileName(self, 'Buka Buku Harian', '', 'Catatan Teks (*.txt)')

        if namaBerkas:
            try:
                with open(namaBerkas, 'r') as berkas:
                    teks = berkas.read()
                    self.editorTeks.setPlainText(teks)
                    QMessageBox.information(self, 'Berhasil', 'Entri buku harian dibuka.')
            except Exception as e:
                QMessageBox.warning(self, 'Kesalahan', f'Tidak dapat membuka entri buku harian: {str(e)}')

    def simpanBukuHarian(self):
        namaBerkas, _ = QFileDialog.getSaveFileName(self, 'Simpan Buku Harian', '', 'Catatan Teks (*.txt)')

        if namaBerkas:
            try:
                with open(namaBerkas, 'w') as berkas:
                    teks = self.editorTeks.toPlainText()
                    berkas.write(teks)
                    QMessageBox.information(self, 'Berhasil', 'Entri buku harian disimpan.')
            except Exception as e:
                QMessageBox.warning(self, 'Kesalahan', f'Tidak dapat menyimpan entri buku harian: {str(e)}')

    def ubahUkuranFont(self, ukuran):
        teksFormat = self.editorTeks.currentCharFormat()
        teksFormat.setFontPointSize(int(ukuran))
        self.editorTeks.mergeCurrentCharFormat(teksFormat)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AplikasiBukuHarian()
    sys.exit(app.exec_())
