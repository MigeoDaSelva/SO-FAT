import sys
sys.path.append("./")
from processos.arquivo import Arquivo
from processos.metadado import Metadado
from nucleo.asciizinho import Asciizinho
from hardware.controlador import Controlador
from hardware.disco_rigido import DiscoRigido


if __name__ == "__main__":

    map = Asciizinho()
    disco = DiscoRigido()
    discos = [disco]
    controlador = Controlador(discos)
    controlador.disco_atual = disco
    text = "Bom dia, desconhecidos."
    nome = "ola.txt"
    arquivo = Arquivo(data=list(), metadados=Metadado())

    for t in text:
        arquivo.data.append(map.to_byte[t])

    arquivo.metadados.nome = nome
    
    print(controlador.disco_atual.buffer[0:100])

    controlador.escrita(disco=0, arquivo=arquivo)

    arquivo1 = Arquivo(data=list(), metadados=Metadado())

    arquivo1.metadados.inicio = arquivo.metadados.inicio

    arquivo2 = controlador.leitura(disco=0, arquivo=arquivo1)

    palavra = str()
    for byte in arquivo2.data:
        palavra += "".join([map.to_latter[byte]])
    
    print()
    print(palavra)
    print()
    print(controlador.disco_atual.buffer[0:100])
