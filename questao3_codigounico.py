# ============================================================
# ARQUIVO: notificador.py
# Classe abstrata Notificador
# ============================================================

from abc import ABC, abstractmethod

class Notificador(ABC):

    @abstractmethod
    def notificar(self, mensagem):
        pass


# ============================================================
# ARQUIVO: notificador_email.py
# Classe NotificadorEmail
# ============================================================

class NotificadorEmail(Notificador):

    def notificar(self, mensagem):

        print(f"📧 E-mail enviado: {mensagem}")


# ============================================================
# ARQUIVO: notificador_sms.py
# Classe NotificadorSMS
# ============================================================

class NotificadorSMS(Notificador):

    def notificar(self, mensagem):

        print(f"📱 SMS enviado: {mensagem}")


# ============================================================
# ARQUIVO: notificador_app.py
# Classe NotificadorApp
# ============================================================

class NotificadorApp(Notificador):

    def notificar(self, mensagem):

        print(f"🔔 Notificação no aplicativo: {mensagem}")


# ============================================================
# ARQUIVO: central_notificacoes.py
# Classe CentralNotificacoes
# ============================================================

class CentralNotificacoes:

    def __init__(self):
        self.notificadores = []

    def adicionar_notificador(self, notificador):

        self.notificadores.append(notificador)

    def enviar_para_todos(self, mensagem):

        for notificador in self.notificadores:
            notificador.notificar(mensagem)


# ============================================================
# ARQUIVO: main.py
# Programa Principal
# ============================================================

central = CentralNotificacoes()

email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

central.enviar_para_todos(
    "Seu curso foi atualizado!"
)
