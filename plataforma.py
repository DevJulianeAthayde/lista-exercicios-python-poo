class Plataforma:

    def __init__(self, nome):
        self.nome = nome

        # Lista responsável por armazenar todas as mídias
        self.midias = []

    def adicionar_midia(self, midia):
        """
        Adiciona uma mídia na plataforma.
        """

        self.midias.append(midia)

    def listar_midias(self):
        """
        Percorre todas as mídias cadastradas.
        """

        print(f"\n===== MÍDIAS DA PLATAFORMA {self.nome} =====")

        for midia in self.midias:
            midia.mostrar_info()
            print("-" * 40)

    def reproduzir_todas(self):
        """
        Demonstra POLIMORFISMO.

        Independentemente do tipo da mídia,
        o método reproduzir() será chamado.
        """

        print("\n===== REPRODUZINDO TODAS AS MÍDIAS =====")

        for midia in self.midias:
            midia.reproduzir()
