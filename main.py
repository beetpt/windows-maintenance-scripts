import customtkinter as ctk
import os
import sys
import webbrowser
import subprocess
from ctypes import windll
from PIL import Image
from styles import COLORS, FONTS
from database2 import DATA

# --- FUNÇÃO PARA CAMINHOS NO EXE ---
def resource_path(relative_path):
    """ Obtém o caminho absoluto para os recursos, funciona em Dev e PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

try:
    # Melhora a nitidez do texto em ecrãs de alta resolução (DPI)
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

class SoftwareTecnico(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- CONFIGURAÇÕES DE VERSÃO E TÍTULO ---
        self.versao = "2.1.5"
        self.title(f"Software Assistência Técnica")

        # --- ÍCONE DO PROGRAMA (CORRIGIDO PARA EXE) ---
        icon_path = resource_path("icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except:
                pass

        # Iniciar em ecrã inteiro (maximizado)
        self.after(0, lambda: self.state('zoomed'))
        self.bind("<Escape>", lambda e: self.destroy())
        ctk.set_appearance_mode("dark")

        # Configuração da Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button_objects = []
        self.sidebar_buttons = {}
        self.pesquisa_ativa = False

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=300, corner_radius=0, fg_color=COLORS["sidebar_bg"])
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.lbl_logo = ctk.CTkLabel(self.sidebar, text="SOFTWARE TÉCNICO", font=FONTS["titulo"],
                                     text_color=COLORS["amarelo_torrado"])
        self.lbl_logo.pack(pady=(40, 5))

        ctk.CTkLabel(self.sidebar, text=f"Versão {self.versao} | Autor: Carlos Macão",
                     font=("Segoe UI", 11, "italic"),
                     text_color="#555").pack(pady=0)

        # --- BARRA DE PESQUISA ---
        self.search_container = ctk.CTkFrame(self.sidebar, fg_color="#1a1a1a", height=40, corner_radius=8,
                                             border_width=1, border_color="#333")
        self.search_container.pack(fill="x", padx=20, pady=20)

        self.lbl_lupa = ctk.CTkLabel(self.search_container, text=" 🔍 ", font=("Segoe UI", 14), text_color="#888")
        self.lbl_lupa.pack(side="left", padx=(5, 0))

        self.entry_search = ctk.CTkEntry(
            self.search_container,
            placeholder_text="Pesquisar ferramenta...",
            fg_color="transparent",
            border_width=0,
            height=35,
            placeholder_text_color="#666"
        )
        self.entry_search.pack(side="left", fill="x", expand=True)
        self.entry_search.bind("<KeyRelease>", self.filtrar_pesquisa)

        self.cat_scroll = ctk.CTkScrollableFrame(self.sidebar, fg_color="transparent")
        self.cat_scroll.pack(fill="both", expand=True, padx=10, pady=10)

        self.btn_sair = ctk.CTkButton(self.sidebar, text="SAIR [ESC]", fg_color="#400", hover_color="#600",
                                      font=FONTS["menu"], command=self.destroy)
        self.btn_sair.pack(fill="x", padx=20, pady=20)

        # --- PAINEL PRINCIPAL ---
        self.main_view = ctk.CTkFrame(self, fg_color=COLORS["bg_black"], corner_radius=0)
        self.main_view.grid(row=0, column=1, sticky="nsew")

        self.cat_title = ctk.CTkLabel(self.main_view, text="SELECIONE UMA CATEGORIA",
                                      font=("Segoe UI Black", 28), text_color=COLORS["verde_ghost"])
        self.cat_title.pack(pady=30)

        self.scroll_pane = ctk.CTkScrollableFrame(self.main_view, fg_color="transparent")
        self.scroll_pane.pack(fill="both", expand=True, padx=40, pady=0)
        self.scroll_pane.grid_columnconfigure((0, 1), weight=1)

        # --- RODAPÉ ---
        self.footer = ctk.CTkFrame(self.main_view, fg_color="transparent", height=50)
        self.footer.pack(fill="x", side="bottom", pady=20, padx=40)

        self.mail_link = ctk.CTkLabel(self.footer, text="📧 beet88@hotmail.com", font=("Segoe UI Semibold", 12),
                                      text_color=COLORS["azul_brilhante"], cursor="hand2")
        self.mail_link.pack(side="right", padx=15)
        self.mail_link.bind("<Button-1>", lambda e: webbrowser.open("mailto:beet88@hotmail.com"))

        self.lbl_cont = ctk.CTkLabel(self.footer, text="CONTACTO:", font=("Segoe UI Black", 13), text_color="#BBBBBB")
        self.lbl_cont.pack(side="right", padx=(0, 10))

        self.gerar_sidebar()
        self.after(200, lambda: self.lbl_logo.focus_set())

    # (Funções filtrar_pesquisa, gerar_sidebar, carregar_cat, gerar_botoes permanecem iguais)
    def filtrar_pesquisa(self, event=None):
        termo = self.entry_search.get().lower().strip()
        if not termo:
            if self.pesquisa_ativa:
                self.pesquisa_ativa = False
                cat_atual = list(DATA.keys())[0]
                for nome, btn in self.sidebar_buttons.items():
                    if btn.cget("text_color") == COLORS["amarelo_torrado"]:
                        cat_atual = nome
                        break
                self.carregar_cat(cat_atual)
            return
        self.pesquisa_ativa = True
        self.cat_title.configure(text="RESULTADOS DA PESQUISA")
        resultados = []
        for categoria in DATA.values():
            for nome, cmd in categoria:
                if termo in nome.lower():
                    resultados.append((nome, cmd))
        self.gerar_botoes(resultados)

    def gerar_sidebar(self):
        for cat in DATA.keys():
            btn = ctk.CTkButton(self.cat_scroll, text=cat, fg_color="transparent",
                                text_color=COLORS["azul_brilhante"], font=FONTS["menu"],
                                hover_color=COLORS["verde_ghost"], anchor="w", height=45,
                                command=lambda c=cat: self.carregar_cat(c))
            btn.pack(fill="x", pady=2)
            self.sidebar_buttons[cat] = btn
        if DATA: self.carregar_cat(list(DATA.keys())[0])

    def carregar_cat(self, cat):
        if not self.pesquisa_ativa:
            self.cat_title.configure(text=cat.upper())
        for nome, btn in self.sidebar_buttons.items():
            btn.configure(text_color=COLORS["amarelo_torrado"] if nome == cat else COLORS["azul_brilhante"])
        if not self.pesquisa_ativa:
            self.gerar_botoes(DATA[cat])

    def gerar_botoes(self, lista):
        for btn in self.button_objects: btn.destroy()
        self.button_objects = []
        row, col = 0, 0
        for nome, cmd in lista:
            btn = ctk.CTkButton(self.scroll_pane, text=nome, height=75, font=FONTS["botao"],
                                fg_color=COLORS["card_bg"], border_width=1, border_color="#222",
                                hover_color=COLORS["verde_ghost"], text_color="white")
            btn.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
            btn.configure(command=lambda c=cmd, b=btn: self.executar(c, b))
            self.button_objects.append(btn)
            col = (col + 1) % 2
            if col == 0: row += 1

    def executar(self, cmd, botao_clicado):
        for btn in self.button_objects:
            btn.configure(text_color="white")

        if botao_clicado:
            botao_clicado.configure(text_color=COLORS["amarelo_torrado"])
            self.update_idletasks()

        try:
            # 1. LIMPEZA DA STRING
            # Remove o "explorer.exe " se estiver no início para não confundir o startfile
            cmd_clean = cmd.replace('explorer.exe ', '').strip()

            # 2. TRATAR PROTOCOLOS (ms-settings:, windowsdefender:, etc)
            # Estes comandos NÃO funcionam bem com Popen, mas funcionam com startfile
            if ":" in cmd_clean and not "\\" in cmd_clean:
                os.startfile(cmd_clean)
                return

            # 3. TRATAR MODO GOD (shell:::)
            if "shell:::" in cmd_clean:
                # Força o explorer a abrir o GUID
                subprocess.Popen(f'explorer.exe {cmd_clean}', shell=True)
                return

            # 4. COMANDOS DE ADMIN (CMD / POWERSHELL)
            if cmd_clean in ["cmd_admin", "powershell_admin"]:
                exe = "cmd.exe" if cmd_clean == "cmd_admin" else "powershell.exe"
                windll.shell32.ShellExecuteW(None, "runas", exe, None, None, 1)
                return

            # 5. COMANDOS QUE COMEÇAM COM CMD (Ex: cmd /k sfc...)
            if cmd_clean.lower().startswith("cmd"):
                args = cmd_clean[3:].strip()
                windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", args, None, 1)
                return

            # 6. EXECUTÁVEIS, MSC E CONTROL PANEL (Ex: taskmgr, services.msc, ncpa.cpl)
            # O ShellExecuteW com "runas" garante que abrem como ADMIN
            res = windll.shell32.ShellExecuteW(None, "runas", cmd_clean, None, None, 1)

            # Se falhar (caminho não encontrado), tenta via shell normal
            if res <= 32:
                subprocess.Popen(cmd_clean, shell=True)

        except Exception as e:
            print(f"Erro ao executar: {e}")

if __name__ == "__main__":
    app = SoftwareTecnico()
    app.mainloop()