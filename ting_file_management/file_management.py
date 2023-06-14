import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    try:
        if path_file == "" or not path_file.endswith(".txt"):
            sys.stderr.write("Formato inválido")
        with open(path_file, "r") as f:
            return [line.rstrip() for line in f]
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
