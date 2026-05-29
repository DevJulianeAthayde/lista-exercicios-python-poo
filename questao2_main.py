from empresa import Empresa
from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado

empresa = Empresa("Tech Solutions")

assalariado = FuncionarioAssalariado(
    "Ana",
    "111.111.111-11",
    5000
)

horista = FuncionarioHorista(
    "Carlos",
    "222.222.222-22",
    160,
    35
)

comissionado = FuncionarioComissionado(
    "Marcos",
    "333.333.333-33",
    50000,
    10
)

empresa.adicionar_funcionario(assalariado)
empresa.adicionar_funcionario(horista)
empresa.adicionar_funcionario(comissionado)

empresa.listar_funcionarios()

empresa.mostrar_folha_pagamento()
