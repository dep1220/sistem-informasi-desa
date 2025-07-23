# from django import forms
# from .models import Warga

# class WargaForm(forms.ModelForm):
#     class Meta:
#         model = Warga
#         # Tampilkan semua field dari model Warga di form
#         fields = '__all__'
#         # Kecualikan field yang terisi otomatis
#         exclude = ['tanggal_dibuat']


from django import forms
from .models import Warga

class WargaForm(forms.ModelForm):
    class Meta:
        model = Warga
        fields = '__all__'
        exclude = ['tanggal_dibuat']
        
        # Menambahkan class bootstrap ke setiap widget form
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nik': forms.TextInput(attrs={'class': 'form-control'}),
            'jenis_kelamin': forms.Select(attrs={'class': 'form-select'}),
            'tempat_lahir': forms.TextInput(attrs={'class': 'form-control'}),
            'tanggal_lahir': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'agama': forms.TextInput(attrs={'class': 'form-control'}),
            'pekerjaan': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }