# 📦 Versões e Releases

## 🔄 Versão Experimental (EXE)

Uma versão experimental do programa está disponível em formato `.exe` para teste direto, sem necessidade de instalar Python.

### 📥 Como Usar a Versão EXE

1. **Faça download** do ficheiro `.exe` do repositório
2. **Execute como Administrador** (clique direito → "Executar como administrador")
3. **Siga as instruções** do programa

### ✅ Vantagens da Versão EXE
- ✅ Sem necessidade de instalar Python
- ✅ Execução rápida
- ✅ Portável - leve em USB ou envie por email
- ✅ Interface direta

### ⚠️ Nota Importante
- A versão EXE é **experimental**
- Pode conter bugs
- Represente a versão em desenvolvimento
- Se encontrar problemas, reporte-os ou use a versão Python

---

## 🐍 Versões em Python

Para usar a versão mais recente em Python:

### Opção 1: Executar Ficheiros `.py` Diretamente

```bash
# 1. Instale Python (se não tiver)
# Descarregue em: https://www.python.org

# 2. Clone o repositório
git clone https://github.com/beetpt/windows-maintenance-scripts.git
cd windows-maintenance-scripts

# 3. Execute o script
python nome_do_script.py
```

### Opção 2: Converter Python para EXE (PyInstaller)

Se prefere criar um `.exe` personalizado a partir dos ficheiros `.py`:

#### Passo 1: Instale PyInstaller
```bash
pip install pyinstaller
```

#### Passo 2: Crie o EXE
```bash
# Básico (sem ícone)
pyinstaller --onefile --windowed nome_do_script.py

# Com ícone personalizado
pyinstaller --onefile --windowed --icon=icon.ico nome_do_script.py

# Com nome customizado
pyinstaller --onefile --windowed --name="Meu Program" nome_do_script.py
```

#### Passo 3: Encontre o EXE
O ficheiro `.exe` estará em:
```
dist/
├── nome_do_script.exe  ← Use este!
```

#### Passo 4: Distribua
```bash
# O ficheiro está pronto para usar/distribuir
# Pode copiar apenas o .exe ou toda a pasta dist/
```

### Opção 3: Converter para EXE (cx_Freeze)

Alternativa ao PyInstaller:

```bash
# Instale
pip install cx_Freeze

# Crie setup.py (exemplo)
from cx_Freeze import setup, Executable

setup(
    name="MeuPrograma",
    version="1.0",
    description="Manutenção Windows",
    executables=[Executable("meu_script.py")]
)

# Execute
python setup.py build
```

---

## 🔧 Comparação: EXE vs Python

| Aspecto | EXE | Python |
|--------|-----|--------|
| **Instalação** | Nenhuma | Requer Python |
| **Tamanho** | ~50-100 MB | ~5 MB |
| **Portabilidade** | Excelente | Boa |
| **Performance** | Excelente | Boa |
| **Fácil de usar** | Muito | Menos |
| **Modificável** | Não | Sim |
| **Versão mais recente** | Experimental | Sempre |

---

## 📋 Checklist para Converter seu Próprio EXE

- [ ] Tenho Python 3.7+ instalado
- [ ] Tenho o ficheiro `.py` que quero converter
- [ ] Instalei PyInstaller (`pip install pyinstaller`)
- [ ] Testei o script Python antes de converter
- [ ] Criei o EXE com sucesso
- [ ] Testei o EXE no meu computador
- [ ] Tem espaço em disco (~100 MB para compilar)

---

## 🐛 Reportar Bugs

Se encontrar problemas com:

### Versão EXE
1. Anote a mensagem de erro exata
2. Teste com a versão Python também
3. Abra uma _issue_ com:
   - Versão do Windows (7, 10, 11, etc.)
   - Mensagem de erro completa
   - O que estava a fazer quando erro ocorreu

### Versão Python
1. Verifique se tem Python 3.7+ (`python --version`)
2. Teste se as dependências estão instaladas
3. Abra uma _issue_ com:
   - Versão do Python
   - Erro completo do terminal
   - Sistema operativo

---

## 🚀 Dicas Úteis

### Executar EXE a partir do Terminal
```bash
# Abra o Command Prompt no local do EXE
cd C:\Caminho\Para\O\EXE
meu_programa.exe
```

### Agendar Execução (Agendador de Tarefas)
```bash
# Windows permite agendar o EXE para executar automaticamente
# Abra "Agendador de Tarefas" (Task Scheduler)
# Crie nova tarefa e selecione o .exe
```

### Passar Argumentos para EXE
Se o programa suporta argumentos:
```bash
meu_programa.exe --dry-run
meu_programa.exe --verbose
```

---

## 📚 Recursos Úteis

- [PyInstaller Documentação](https://pyinstaller.org/)
- [Python.org](https://www.python.org)
- [cx_Freeze Documentação](https://cx-freeze.readthedocs.io/)

---

**Última atualização:** Junho de 2026
"