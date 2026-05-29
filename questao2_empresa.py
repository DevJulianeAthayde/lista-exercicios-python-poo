class Empresa:

    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):

        self.funcionarios.append(funcionario)

    def listar_funcionarios(self):

        print(f"\n===== FUNCIONÁRIOS DA EMPRESA {self.nome} =====")

        for funcionario in self.funcionarios:
            funcionario.mostrar_dados()
            print("-" * 40)

    def mostrar_folha_pagamento(self):

        print("\n===== FOLHA DE PAGAMENTO =====")

        for funcionario in self.funcionarios:

            pagamento = funcionario.calcular_pagamento()

            print(
                f"{funcionario.nome} -> "
                f"R$ {pagamento:.2f}"
            )
