from django import forms
import re


class MainForm(forms.Form):
    search_field = forms.CharField(label='Введите ссылку',
                                   max_length=1000,
                                   help_text='https://...',
                                   )

    def clean_search_field(self):
        value = self.cleaned_data['search_field']
        pattern = r'https://[\w+|\.]*\/\w+\/.*'
        match = re.fullmatch(pattern, value)
        if not match:
            raise forms.ValidationError('Ссылка должна соответствовать'
                                        ' формату: https://xxxx.ru/x/xxxxx'
                                        )
        return value
