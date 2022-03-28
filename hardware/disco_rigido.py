from typing import List
from processos.metadado import Metadado
from dataclasses import dataclass, field
from hardware.singletonzinho import SingletonZinho


@dataclass
class DiscoRigido(SingletonZinho):

    tabela_de_diretorio: List[Metadado] = field(init=False)
    blocos_de_dados: list = field(init=False)
    tabela_fat: dict = field(init=False)
    buffer: list = field(init=False)

    def __post_init__(self):
        buffer_size = 32000
        megabyte = (2**20)*8
        self.buffer = ["01000110"] * buffer_size
        self.blocos_de_dados = ["01000110"] * megabyte
        self.tabela_fat = dict()
        self.tabela_de_diretorio = list()

    def escrita(self):
        for i in range(len(self.buffer)):
            self.blocos_de_dados[i] = self.buffer[i]

    def leitra(self):
        for i in range((self.buffer)):
            self.buffer[i] = self.blocos_de_dados[i]
