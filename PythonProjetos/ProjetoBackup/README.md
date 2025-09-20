# 🗂️ Backup Automático de Pastas em Python

Este projeto é um script simples em **Python** criado para treinar conceitos de manipulação de arquivos, diretórios e uso de interface gráfica com **Tkinter**.  
Ele permite que o usuário selecione uma pasta no computador e faça o backup automático de todos os arquivos e subpastas em uma pasta de destino escolhida, organizando-os com a data e hora da cópia.

---

## 🚀 Funcionalidades

- Seleção da **pasta de origem** (onde estão os arquivos).
- Seleção da **pasta de destino** (onde o backup será salvo).
- Criação de uma subpasta `backup-nomeDaPasta` no diretório de destino.
- Organização dos backups em pastas nomeadas com **data e hora**.
- Cópia de arquivos e diretórios preservando a estrutura original.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Módulos padrão**:
  - `os` → manipulação de caminhos e diretórios.
  - `shutil` → cópia de arquivos e pastas.
  - `datetime` → marcação com data e hora.
  - `tkinter.filedialog` → seleção de pastas via interface gráfica.

---

## 📦 Como Usar

1. Certifique-se de ter o **Python 3** instalado.
2. Baixe/clique com o botão direito no código e salve em um arquivo, por exemplo:  
   ```bash
   py Proj-Backup.py
