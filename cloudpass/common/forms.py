from django import forms
import re


class MainForm(forms.Form):
    search_field = forms.CharField(label='http://...',
                                   max_length=250,
                                   help_text='Введите ссылку',
                                   )

    def clean_search_field(self):
        value = self.cleaned_data['search_field']
        pattern = r'https://[\w+|\.]*\/\w+\/\w+'
        match = re.fullmatch(pattern, value)
        if not match:
            raise forms.ValidationError('Ссылка должна соответствовать'
                                        'формату: https://xxxx.ru/x/xxxxx'
                                        )
