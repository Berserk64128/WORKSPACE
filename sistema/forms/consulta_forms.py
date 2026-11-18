from django import forms
from sistema.models import Consulta

# Checagem de email
# checagem de senha
# checagem de dado inserido

# Formulário do Médico (usado para cadastro e edição)
class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = ['consulta_nova', 'paciente_id', 'medico_id', 'data_consulta',]
        # criacao_data e ativo não aparecem: são preenchidos automaticamente.
        labels = {
            'consulta_nova': 'Consulta_nova',
            'paciente_id': 'Paciente_id',
            'medico_id': 'Medico_id',
            'data_consulta': 'Data_consulta',
        }