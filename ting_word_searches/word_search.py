from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    """Aqui irá sua implementação"""
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        occurrences = []
        with open(file["nome_do_arquivo"], "r") as f:
            lines = f.readlines()
            for j, line in enumerate(lines):
                if word.lower() in line.lower():
                    occurrences.append({"linha": j + 1})
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    result = []

    for i in range(len(instance)):
        file = instance.search(i)
        occurrences = []
        with open(file["nome_do_arquivo"], "r") as f:
            lines = f.readlines()
            for j, line in enumerate(lines):
                if word.lower() in line.lower():
                    occurrences.append(
                        {"linha": j + 1, "conteudo": line.replace("\n", "")}
                    )
        if occurrences:
            result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return result
