# 📝 Ficheiroiros Pessoais e de Uso Pessoal

Este documento explica os scripts e ficheiros desenvolvidos para uso pessoal neste repositório.

## ⚠️ Importante

Os scripts listados nesta secção foram desenvolvidos **especificamente para o meu ambiente pessoal** e podem **não funcionar no seu computador** sem ajustes.

## 📂 Estrutura de Ficheiros Pessoais

```
windows-maintenance-scripts/
├── README.md                    # Documentação principal
├── PERSONAL.md                  # Este ficheiro
├── .gitignore                   # Ficheiros ignorados pelo Git
└── personal/                    # Pasta para ficheiros pessoais
    ├── backup_pessoal.py
    ├── limpeza_customizada.py
    └── README.md                # Documentação pessoal
```

## 🔧 Como Adaptar Scripts Pessoais

### 1. Revise o Código
```python
# Procure por:
- Caminhos hardcoded (C:\Users\seu_usuario\...)
- Nomes de pastas específicas
- Programas ou ficheiros especiais
```

### 2. Identifique as Customizações
```python
# Exemplo de configuração hardcoded:
BACKUP_FOLDER = "C:\\Users\\beetpt\\Documentos\\Backup"  # ← Alterar!
CLEANUP_EXTENSIONS = [".tmp", ".cache"]                    # ← Customizar?
```

### 3. Adapte ao Seu Ambiente
```python
# Melhor forma - usar configuração:
import os

# Pegue na pasta do utilizador
USER_FOLDER = os.path.expanduser("~")
BACKUP_FOLDER = os.path.join(USER_FOLDER, "Documentos", "Backup")
```

### 4. Teste Primeiro
```bash
# Execute em modo de teste (sem fazer alterações)
python script.py --dry-run

# Ou:
python script.py --preview
```

## 📋 Scripts Pessoais Atuais

| Script | Descrição | Status | Ajustes Necessários |
|--------|-----------|--------|---------------------|
| | A adicionar | | |

## 🚫 O Que NÃO Fazer

- ❌ Não execute scripts sem antes revisar o código
- ❌ Não ignore os avisos de segurança
- ❌ Não execute com permissões de administrador sem razão
- ❌ Não confie em paths automáticos sem testar
- ❌ Não ignore backups - **faça sempre backup primeiro!**

## ✅ Boas Práticas

1. **Sempre faça backup** dos seus dados importantes
2. **Teste em VM ou máquina de teste** primeiro
3. **Revise o código** antes de executar
4. **Use `--dry-run` ou `--preview`** quando disponível
5. **Mantenha logs** do que foi executado
6. **Documente mudanças** que fez no script

## 🔍 Segurança

### Permissões de Administrador
Alguns scripts requerem permissões elevadas:
```bash
# Windows (Executar como Administrador)
Run-As Administrator: python script.py
```

### Ficheiros Sensíveis
Ficheiros sensíveis são **ignorados pelo Git**:
- `secrets.ini` - Credenciais
- `*.env` - Variáveis de ambiente
- `*.personal` - Ficheiros pessoais
- Pasta `personal/` - Ficheiros customizados

## 📞 Suporte

Se encontrar problemas:

1. Verifique o ficheiro `*.log` gerado
2. Revise o código e identifique o problema
3. Adapte conforme necessário
4. Abra uma _issue_ se achar que é um bug geral

## 🤝 Contribuições

Se melhorar um script pessoal e achar que pode ser útil para outros:

1. Remova configurações pessoais
2. Torne-o genérico e configurável
3. Adicione documentação clara
4. Faça um pull request!

---

**Última atualização:** Junho de 2026
