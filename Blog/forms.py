from django.forms import ModelForm
from .models import bloginfo

class BlogForm(ModelForm):
    class Meta:
        model = bloginfo
        fields = '__all__'