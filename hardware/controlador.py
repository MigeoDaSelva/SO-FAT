from typing import List
from dataclasses import dataclass, field
from processos.arquivo import Arquivo
from hardware.disco_rigido import DiscoRigido


@dataclass
class Controlador:
    discos: List[DiscoRigido]
    disco_atual: DiscoRigido = field(init=False)

    def leitura(self, disco: int, arquivo: Arquivo) -> Arquivo:
        self.disco_atual = self.discos[disco]

        blocos = []
        indice = arquivo.metadados.inicio
        while True:
            blocos.append(self.disco_atual.buffer[indice])
            indice = self.disco_atual.tabela_fat[indice]
            if indice == "01000110":
                arquivo.data = blocos
                return arquivo

    def alocacao_de_bytes_no_disco(self, indice_anterior: int, byte: str):

        for indice in range(indice_anterior, len(self.disco_atual.buffer)):
            if self.disco_atual.buffer[indice] == "01000110":
                self.disco_atual.buffer[indice] = byte
                return indice

    def escrita(self, disco: int, arquivo: Arquivo):
        self.disco_atual = self.discos[disco]

        byte = arquivo.data.pop(0)
        indice_anterior = self.alocacao_de_bytes_no_disco(
            indice_anterior=0, byte=byte)
        arquivo.metadados.inicio = indice_anterior

        for byte in arquivo.data:
            indice_atual = self.alocacao_de_bytes_no_disco(
                indice_anterior=indice_anterior, byte=byte)
            self.disco_atual.tabela_fat[indice_anterior] = indice_atual
            indice_anterior = indice_atual
        self.disco_atual.tabela_fat[indice_anterior] = "01000110"
        self.disco_atual.tabela_de_diretorio.append(arquivo.metadados)
        self.disco_atual.escrita()