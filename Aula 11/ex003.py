nome = "Weslley"
cores = {"limpa":"\033[m",
        "azul":"\033[1;34m",
        "amarelo":"\033[1;33m",
        "pretoebranco":"\033[7;37m"
}

print("Olá! Muito prazer em te conhecer, {}{}{}!!".format(cores['pretoebranco'], nome, cores['limpa']))