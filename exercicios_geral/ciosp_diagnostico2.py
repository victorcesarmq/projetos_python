"""
CIOSP — Diagnóstico 5
Sem QSS, sem hook, sem workers. Só a estrutura de navegação.
"""
import sys, os, sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QLabel, QLineEdit, QPushButton, QTabWidget,
    QVBoxLayout, QHBoxLayout, QProgressBar, QMessageBox,
)
from PyQt6.QtCore import Qt, pyqtSignal

PASTA    = r"C:\Contador_CIOSP"
DB_LOCAL = os.path.join(PASTA, "usuarios_backup.db")
os.makedirs(PASTA, exist_ok=True)
with sqlite3.connect(DB_LOCAL) as c:
    c.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT PRIMARY KEY, senha TEXT, tipo INTEGER)")
    c.execute("INSERT OR IGNORE INTO usuarios VALUES ('TESTE','1234',0)")

app = QApplication(sys.argv)
print("[1] app OK")

class TelaLogin(QWidget):
    login_ok = pyqtSignal(str, bool)
    def __init__(self):
        super().__init__()
        v = QVBoxLayout(self)
        v.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.e_u = QLineEdit(); self.e_u.setPlaceholderText("usuario"); v.addWidget(self.e_u)
        self.e_s = QLineEdit(); self.e_s.setPlaceholderText("senha"); self.e_s.setEchoMode(QLineEdit.EchoMode.Password); v.addWidget(self.e_s)
        btn = QPushButton("ENTRAR"); btn.clicked.connect(self._logar); v.addWidget(btn)
        v.addWidget(QLabel("TESTE / 1234"))
    def _logar(self):
        u = self.e_u.text().upper().strip()
        s = self.e_s.text().strip()
        with sqlite3.connect(DB_LOCAL) as conn:
            res = conn.execute("SELECT tipo FROM usuarios WHERE nome=? AND senha=?", (u,s)).fetchone()
        if res: self.login_ok.emit(u, res[0]==1)
        else: QMessageBox.critical(self, "Erro", "Inválido")

print("[2] TelaLogin OK")

class AbaContar(QWidget):
    def __init__(self, usuario):
        super().__init__()
        print("[AbaContar.__init__] inicio")
        v = QVBoxLayout(self)
        print("[AbaContar] QProgressBar...")
        pb = QProgressBar(); pb.setMaximum(80); pb.setValue(0); pb.setTextVisible(False); pb.setFixedHeight(4); v.addWidget(pb)
        print("[AbaContar] QLabel contador...")
        lbl = QLabel("0"); lbl.setAlignment(Qt.AlignmentFlag.AlignCenter); v.addWidget(lbl)
        print("[AbaContar] botoes...")
        brow = QHBoxLayout(); brow.setAlignment(Qt.AlignmentFlag.AlignCenter)
        brow.addWidget(QPushButton("−")); brow.addWidget(QPushButton("+"))
        v.addLayout(brow)
        print("[AbaContar.__init__] fim OK")

print("[3] AbaContar OK")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Diag 5"); self.setFixedSize(400, 560)
        self.stack = QStackedWidget(); self.setCentralWidget(self.stack)
        self.login = TelaLogin(); self.login.login_ok.connect(self._on_login)
        self.stack.addWidget(self.login)
        print("[4] MainWindow OK")

    def _on_login(self, usuario, is_admin):
        print(f"[_on_login] {usuario}")
        principal = QWidget()
        v = QVBoxLayout(principal); v.setContentsMargins(0,0,0,0); v.setSpacing(0)
        print("[_on_login] topbar...")
        bar = QWidget(); bar.setFixedHeight(38)
        bh = QHBoxLayout(bar); bh.addWidget(QLabel(f"● {usuario}")); bh.addStretch()
        btn_s = QPushButton("SAIR"); btn_s.clicked.connect(self._sair); bh.addWidget(btn_s)
        v.addWidget(bar)
        print("[_on_login] QTabWidget...")
        tabs = QTabWidget(); tabs.setDocumentMode(True)
        print("[_on_login] AbaContar...")
        aba = AbaContar(usuario)
        print("[_on_login] addTab...")
        tabs.addTab(aba, "CONTAR")
        print("[_on_login] addWidget tabs...")
        v.addWidget(tabs, 1)
        print("[_on_login] stack...")
        self.stack.addWidget(principal)
        self.stack.setCurrentWidget(principal)
        print("[_on_login] DONE")

    def _sair(self):
        while self.stack.count() > 1:
            w = self.stack.widget(1); self.stack.removeWidget(w); w.deleteLater()
        self.stack.setCurrentIndex(0)

win = MainWindow()
win.show()
print("[5] janela aberta — entre com TESTE / 1234")
sys.exit(app.exec())