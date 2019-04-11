from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Product, Category, SubCategory

class RegistarForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

        def save(self, commit=True):
            #   Ainda não vai salvar o form porque ainda não acabamos de editar o models
            user = super(RegistarForm, self).save(commit=False)
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']

            # Depois de tudo  tar feito ja podemos guardar
            if commit:
                user.save()

            return user


class EditarPerfilForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )


class InserirProductoForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class InserirCategoriaForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class InserirSubCategoriaForm(forms.ModelForm):

    class Meta:
        model = SubCategory
        fields = '__all__'
