import paramiko
import warnings
from cryptography.utils import CryptographyDeprecationWarning

warnings.filterwarnings("ignore", category=CryptographyDeprecationWarning)


def connect_to_server(hostname, port, username, password):
    try:
        # SSH client oluşturma
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname, port=port, username=username, password=password)
        return ssh_client
    except Exception as e:
        print(f"Bağlantı hatası: {str(e)}")
        return None

def upload_file(ssh_client, local_path, remote_path):
    try:
        # SFTP client oluşturma
        sftp_client = ssh_client.open_sftp()
        sftp_client.put(local_path, remote_path)
        sftp_client.close()
        print(f"{local_path} dosyası {remote_path} olarak yüklendi.")
    except Exception as e:
        print(f"Dosya yükleme hatası: {str(e)}")

def main():
    hostname = "example.com"
    port = 22
    username = "kullanici_adi"
    password = "sifre"
    local_path = "/yerel/dosya/yolu"
    remote_path = "/uzak/dosya/yolu"

    ssh_client = connect_to_server(hostname, port, username, password)
    if ssh_client:
        upload_file(ssh_client, local_path, remote_path)
        ssh_client.close()

if __name__ == "__main__":
    main()
