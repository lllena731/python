import sys
from PyQt4 import QtGui

class main_win(QtGui.QMainWindow):
    
    def __init__(self):
        super(main_win, self).__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        
        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open File', self)
        openFile.setShortcut('Ctrl+o')
        openFile.setStatusTip('Open a New IR File')
        openFile.triggered.connect(self.openFile)

        exitAction = QtGui.QAction(QtGui.QIcon('quit.png'), 'Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Quit the Application')
        exitAction.triggered.connect(self.close)

        self.statusBar()
    
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(openFile)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        toolbar.addAction(openFile)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('IR Analysis and Rendering')
        self.show()

    def openFile(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

def main():
    app = QtGui.QApplication(sys.argv)
    main_prog = main_win()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
