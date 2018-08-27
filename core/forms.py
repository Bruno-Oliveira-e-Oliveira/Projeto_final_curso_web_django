from django.forms import ModelForm
from .models import Pessoa,Veiculo,MovimentoRot,MovimentoMens, Mensalista

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MovRotForm(ModelForm):
    class Meta:
        model = MovimentoRot
        fields = '__all__'

class MovMensForm(ModelForm):
    class Meta:
        model = MovimentoMens
        fields = '__all__'
