class Pessoa:
  def __init__(self, nome, idade) -> None:
      self.nome = nome
      self.idade = idade


      
  def abrirOlho(self, text):
    print('Abrindo os olhos...' + text)
      
pessoa1 = Pessoa('Vinícius', 32)

pessoa1.abrirOlho(input('Digite um texto aqui: '))