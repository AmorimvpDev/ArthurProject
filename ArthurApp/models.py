from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField(max_length = 50)
    telefone = models.CharField(max_length = 14, blank = True, null = True)
    cidade = models.CharField(max_length = 70)

    class Meta:
        verbose_name_plural = 'Fornecedores'
    
    def __str__(self):
        # return (f'{self.nome} {self.telefone} {self.cidade}')
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length = 20)

    def __str__(self):
        return self.nome

class Produto(models.Model):

    CORES = [ #maiusculo pq n vou modificar
        ('BRC', 'Branco'),
        ('PRT', 'Preto'),
        ('AMA', 'Amarelo'),
        ('VRD', 'Verde'),
        ('VML', 'Vermelho'),
        ('AZL', 'Azul'),
        ('LGB', 'LGBT')
    ]

    nome = models.CharField(max_length= 50) #aceita ate 50 letras
                #campo p colocar nome 
    descricao = models.TextField(max_length = 8000, verbose_name = 'Descrição') #8000 caracteres
                #campo de texto
    preco = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Preço') #jeito q vai exibir
                                                #ate 2 casas decimais
    estoque = models.IntegerField()
                    #so aceita numero
    peso = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0)
                                                            #os produtos q ja existem vao vim com o peso 0
    lancamento = models.BooleanField(verbose_name = 'Lançamento')
                #False or True
    data_de_validade = models.DateField(blank = True, null = True)
                                #nao é obrigatorio    #nao é obrigatorio     
                                #responder no site    #responder no banco de dados
    cor = models.CharField(max_length = 3, blank = True, null = True, choices = CORES)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True)
            #consigo criar                #Oq ele faz quando deleto o produto
            #mesmo sem entrar no codigo
    fornecedor = models.ManyToManyField(Fornecedor)
                        #muitos relacionamentos, esta envolvida com varias tabelas