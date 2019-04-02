from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

def open_db():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('test.db')
    db.open()
    return db

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.mapper = QtWidgets.QDataWidgetMapper(self)
        self.db = open_db()
        self.model = QSqlQueryModel(self)
        self.model.setQuery('SELECT DISTINCT form FROM test')
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.label, 0, b'text')
        self.mapper.toFirst()

        self.button_left.clicked.connect(self.mapper.toPrevious)
        self.button_right.clicked.connect(self.mapper.toNext)

