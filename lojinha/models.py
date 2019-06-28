from django.db import models

# Create your models here.

class Bolo(models.Model):
    sabores_opcoes = [

        ('ch','chocolate'),
        ('mr', 'Morango'),
        ('pr', 'Prestígio'),
        ('bn', 'Baunilha'),
        ('nh', 'Ninho'),
        ('cr', 'Churros'),
    ]

    recheios_opcoes = [

        ('br', 'Brigadeiros'),
        ('dl', 'Doce de leite'),
        ('fv', 'Frutas Vermelhas'),
        ('nt', 'Nutella'),
        ('bj', 'Beijinho'),
        ('nh', 'Ninho'),
    ]

    coberturas_opcoes = [

        ('gr', 'Granulado'),
        ('ct', 'Chantilly'),
        ('mr', 'Morango')
    ]

    sabor = models.CharField(max_length=2, choices=sabores_opcoes)
    recheio = models.CharField(max_length=2, choices=recheios_opcoes)
    coberturas = models.CharField(max_length=2, choices=coberturas_opcoes, default='src')
    peso = models.DecimalField(decimal_places=2, max_digits=3, default=1.00)
    nome = models.CharField(max_length=100)
   
    # o self é o this do javascript !
    def __str__(self): 
        return self.nome

class Pedido(models.Model):
    pagamento_opcoes = [
        ('av', 'Pagamento à vista'),
        ('p2', 'Parcelado em 2 vezes'),
        ('p3', 'Parcelado em 3 vezes')
    ]
    
    cpf = models.CharField(max_length=11,)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    cartao = models.IntegerField()
    pagamento = models.CharField(max_length=2,
     choices=pagamento_opcoes, default='av')

    def __str__(self):
        return