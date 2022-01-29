from openpyxl import load_workbook
import sys


def gerar_id(numberEnd, excelName):
    ficheiro = load_workbook(excelName)
    aba_ativa = ficheiro.active

    for celula in range(1):
        for i in range(int(numberEnd)):
            linha = i + 2
            aba_ativa[f"A{linha}"] = i + 1

    ficheiro.save(excelName)


if __name__ == '__main__':
    # if len(sys.argv) < 2:
    #    sys.exit("Número de parâmetros inválido..")
    #else:
        gerar_id(int(sys.argv[1]), sys.argv[2])
        sys.exit("OK")
    