from dataclasses import dataclass, field


@dataclass
class Metadado:

    nome: str = field(init=False)
    inicio: int = field(init=False)

    def __eq__(self, other) -> bool:
        return self.nome == other.nome and self.inicio == other.inicio
