from django import forms
from sistema.models import Paciente

# Checagem de email
# checagem de senha
# checagem de dado inserido

# Formulário do Médico (usado para cadastro e edição)
class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ['nome', 'sobrenome', 'email', 'telefone', 'cpf', 'mensagem']
        # criacao_data e ativo não aparecem: são preenchidos automaticamente.
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'cpf': 'CPF',
            'mensagem': 'Mensagem',
        }