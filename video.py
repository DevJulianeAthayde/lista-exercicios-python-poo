from midia import Midia

class Video(Midia):

    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)

        self.resolucao = resolucao

    def reproduzir(self):
        """
        Implementação específica para vídeos.
        """

        print(
            f"▶️ Reproduzindo vídeo '{self.titulo}' "
            f"em resolução {self.resolucao}"
        )
