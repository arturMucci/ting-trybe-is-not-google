import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    """Aqui irá sua implementação"""
    # print(path_file + "\n")
    for index in range(len(instance)):
        result = instance.search(index)
        if result["nome_do_arquivo"] == path_file:
            return

    rows = txt_importer(path_file)

    result = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(rows),
        "linhas_do_arquivo": rows,
    }

    instance.enqueue(result)
    sys.stdout.write(str(result))


def remove(instance: Queue):
    """Aqui irá sua implementação"""
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
        return

    path_file = instance.search(index=0)["nome_do_arquivo"]
    instance.dequeue()
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance: Queue, position):
    """Aqui irá sua implementação"""
    try:
        sys.stdout.write(str(instance.search(position)))
    except IndexError:
        sys.stderr.write("Posição inválida")
