from django.db import models

# Create your models here.
class Agendamento(models.Model):
    PRIORITARIO_CHOICES = [
                (1, 'Pessoas com 60 anos ou mais institucionalizadas'),
                (2, 'Pessoas com Deficiência Institucionalizadas'),
                (3, 'Povos indígenas Vivendo em Terras Indígenas'),
                (4, 'Trabalhadores de Saúde'),
                (5, 'Pessoas de 90 anos ou mais'),
                (6, 'Profissionais da educação'),
            ]
    
    LOCAL_CHOICES = [
                (1, 'UFPI'),
                (2, 'HU'),
                (3, 'Zona sul'),
                (4, 'Zona norte'),
                (5, 'Zona Leste'),
                (6, 'Centro'),
            ]
    
    VACINA_CHOICES = [
                (1, 'Astrazeneca'),
                (2, 'Pfizer'),
                (3, 'Jhonson'),
                (4, 'Covaxin'),
            ]
    
    SEXO_CHOICES = [
                ('M', 'Masculino'),
                ('F', 'Feminino'),
            ]
    
    HORARIO_CHOICES = [
                (8, 8),
                (9, 9),
                (10, 10),
                (11, 11),
                (12, 12),
                
                (14, 14),
                (15, 15),
                (16, 16),
                (17, 17),
                (18, 18),
            ]
        
    nome = models.CharField('Nome do paciente', max_length=250)
    cpf = models.CharField('Informe seu CPF ', max_length=250)
    grupo_prioritario = models.IntegerField(verbose_name='Informe o grupo Prioritário', choices=PRIORITARIO_CHOICES)
    
    rg = models.CharField('RG', max_length=250, null=True, blank=True)
    cns = models.CharField('Núme. CNS', max_length=250, null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=10, choices=SEXO_CHOICES)
    data_nascimento = models.DateField('Data Nascimento')
    celular = models.CharField('Núm. celular', max_length=250)
    cep = models.CharField('CEP', max_length=250, null=True, blank=True)
    logradouro = models.CharField('Logradouro', max_length=250)
    numero = models.CharField('Número', max_length=250, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=250)
    uf = models.CharField('UF', max_length=250)
    cidade = models.CharField('Cidade', max_length=250)
    
    vacina = models.IntegerField('Vacina', choices=VACINA_CHOICES)
    
    local_primeira_vacina = models.IntegerField('Local primeira vacina', choices=LOCAL_CHOICES)
    data_primeira_vacina = models.DateField('Data e hora primeira vacina')
    hora_primeira_vacina = models.IntegerField('Horário primeira vacina', choices=HORARIO_CHOICES)
    
    local_segunda_vacina = models.IntegerField('Local segunda vacina', choices=LOCAL_CHOICES, null=True, blank=True)
    data_segunda_vacina = models.DateField('Data e hora segunda vacina', null=True, blank=True)
    hora_segunda_vacina = models.IntegerField('Horário segunda vacina', choices=HORARIO_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return str(self.nome)

    class Meta:
        verbose_name = 'Vacina agendada'
        verbose_name_plural = 'Vacinas agendadas'
        