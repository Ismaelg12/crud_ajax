from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model   = Book
        fields  = '__all__'
        widgets = {
            'agenda'      : forms.DateInput(attrs={'class': 'form-control','required': 'true'}),
            'hora_inicio' : forms.TimeInput(attrs={'class': 'form-control input-rounded'}),
            'hora_fim'    : forms.TimeInput(attrs={'class': 'form-control','required': 'true'}),
            'sala'        : forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true'}),
            'paciente'    : forms.TextInput(attrs={'class': 'form-control','cols' : "10", 'rows': "3",}), 
            'convenio'    : forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true'}),
            'profissional': forms.Select(attrs={'class':'selectpicker','data-style':'select-with-transition',
                'data-size':7,'data-live-search':'true','required': 'true'}),
            'telefone'    : forms.TextInput(attrs={'class': 'form-control','required': 'true'}),
           # 'status'      : forms.Select(attrs={'class': 'form-control','readonly':'readonly'}),
            'observacao'  : forms.Textarea(attrs={'class': 'form-control','cols' : "10", 'rows': "3",}), 
        }
    