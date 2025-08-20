# aba de seleção da pasta a ser copiada do pc
import oss
import shutil
import datetime
import tkinter.filedialog as  fidia

pasta_com_arquivos = fidia.askdirectory()

lista_arquivos = os.listdir(pasta_com_arquivos)

# aba de seleção da pasta de destino
pasta_de_backup = fidia.askdirectory()

caminho_pasta_de_backup = "backup-"+os.path.basename(pasta_com_arquivos)

caminho_completo_pasta_de_backup = f"{pasta_de_backup}/{caminho_pasta_de_backup}"

if not os.path.exists(caminho_completo_pasta_de_backup):
    os.mkdir(caminho_completo_pasta_de_backup)

data_hora_atual = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")

# execução da cópia dos arquivos
for arquivo in lista_arquivos:
    caminho_completo_arquivo_origem = f"{pasta_com_arquivos}/{arquivo}"
    caminho_completo_arquivo_backup = f"{caminho_completo_pasta_de_backup}/{data_hora_atual}/{arquivo}"
    if "." in arquivo:
        shutil.copy2(caminho_completo_arquivo_origem, caminho_completo_arquivo_backup)
    elif f"{caminho_pasta_de_backup}" != arquivo:
        shutil.copytree(caminho_completo_arquivo_origem, caminho_completo_arquivo_backup)

