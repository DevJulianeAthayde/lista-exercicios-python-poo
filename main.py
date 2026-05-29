from video import Video
from podcast import Podcast
from texto_narrado import TextoNarrado
from plataforma import Plataforma

# Criação da plataforma
plataforma = Plataforma("EducaTech")

# Criação das mídias
video = Video(
    "Python Orientado a Objetos",
    45,
    "1080p"
)

podcast = Podcast(
    "Tecnologia em Debate",
    60,
    "Carlos Silva"
)

texto = TextoNarrado(
    "História da Computação",
    30,
    "Português"
)

# Adicionando mídias
plataforma.adicionar_midia(video)
plataforma.adicionar_midia(podcast)
plataforma.adicionar_midia(texto)

# Listagem
plataforma.listar_midias()

# Reprodução
plataforma.reproduzir_todas()
