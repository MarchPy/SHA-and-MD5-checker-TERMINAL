import hashlib
from sys import argv
from os import system



class Core:
    def __init__(self, path):
        system("clear")
        self.path = path

    def _sha256(self):
        try:
            with open(self.path, "rb") as file:
                bytes = file.read()
                return hashlib.sha256(bytes).hexdigest()
        except FileNotFoundError:
            print("""
            OPS... Não foi possivél encontrar o arquivo especificado.
            """)

    def _sha512(self):
        try:
            with open(self.path, "rb") as file:
                bytes = file.read()
                return hashlib.sha512(bytes).hexdigest()

        except FileNotFoundError:
            print("""
            OPS... Não foi possivél encontrar o arquivo especificado.
            """)
            
    def _md5(self):
        try:
            with open(self.path, "rb") as file:
                bytes = file.read()
                return hashlib.md5(bytes).hexdigest()
        except FileNotFoundError:
            print("""
            OPS... Não foi possivél encontrar o arquivo especificado.
            """)


if __name__ == "__main__":
    params = argv
    if params != ["checker.py"]:
        if params == ["checker.py", "-h"]:
            print("""
            -p,  Caminho do arquivo
            -t, tipo de criptografia (SHA256, SHA512, MD5)
            
            """)

        elif "-p" in params and "-t" in params:
            if "-p" in params:
                local_param = params.index("-p")
                path = params[local_param+1]
                app = Core(path=path)

            if "-t" in params:
                local_param = params.index("-t")
                try:
                    type_crypt = params[local_param+1]
                    if type_crypt == "sha256":
                        hash = app._sha256()
                        if hash is not None:
                            print(f"\nSHA256: {hash}\n")

                    elif type_crypt == "sha512":
                        hash = app._sha512()
                        if hash is not None:
                            print(f"\nSHA512: {hash}\n")

                    elif type_crypt == "md5":
                        hash = app._md5()
                        if hash is not None:
                            print(f"\nMD5: {hash}\n")

                    else:
                        print("\nOPS... Veja as opções diponíveis: [SHA256, SHA512, MD5]\n")
                        
                except IndexError:
                    print('\nOPS... O paramentro "-t" deve ser especificado.\n')

        else:
            print("\nVocê deve especificar o tipo e o caminho do arquivo.\n")
    else:
            print("""
            -p,  Caminho do arquivo
            -t, tipo de criptografia (SHA256, SHA512, MD5)
            """)
