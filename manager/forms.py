from django import forms

from manager.models import File, File_two, File_diskont


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file')


class Prie_File_Form(forms.ModelForm):
    class Meta:
        model = File_two
        fields = ('name', 'file')
class Diskont_File_Form(forms.ModelForm):
    class Meta:
        model = File_diskont
        fields = ('name', 'file')
