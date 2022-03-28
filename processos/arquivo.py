
from dataclasses import dataclass, field
from processos.metadado import Metadado


@dataclass
class Arquivo:
    data: list
    metadados: Metadado
