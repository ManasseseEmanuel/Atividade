class Pessoa: 
    def init (self,nome,idade):
        self.nome = nome 
        self.idade = idade

class Aluno(Pessoa): 
    def init (self,nome,idade,matricula):
        super().init(nome,idade)
        self.matricula = matricula

    def info (self):
        print ('Informações do aluno')
        print (self.nome,"/", self.idade,"/",self.matricula)

class Professor(Pessoa):
    def init (self,nome,idade,disciplina):
        super().init(nome,idade)
        self.disciplina = disciplina

    def info (self):
        print ('Informações do Professor')
        print (self.nome,"/",self.idade,"/",self.disciplina)

class Func_administrativo(Pessoa): 
    def init (self,nome,idade,cargo):
        super().init(nome,idade)
        self.cargo = cargo

    def info (self):
        print ('Informações do Funcionário administrativo')
        print (self.nome,"/",self.idade,"/",self.cargo)

from sistema_academico import Pessoa 
from sistema_academico import Aluno
from sistema_academico import Professor
from sistema_academico import Func_administrativo

aluno1 = Aluno ('Jose',11,'010')
aluno2 = Aluno ('Maria',13,'011')
prof1 = Professor ('Marcos',27,'Português')
prof2 = Professor ('Laura',23,'Inglês')
fun1 = Func_administrativo ('Camila',28,'Secretária')

aluno1.info()
aluno2.info()
prof1.info()
prof2.info()
fun1.info()
