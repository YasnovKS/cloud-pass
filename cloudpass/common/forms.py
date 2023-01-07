from django import forms
import re
from cloudpass.settings import PLACEHOLDER


class MainForm(forms.Form):
    search_field = forms.CharField(label='',
                                   max_length=1000,
                                   widget=(forms.TextInput
                                           (attrs={'class': 'input-field',
                                                   'size': '100',
                                                   'placeholder': PLACEHOLDER}
                                            )
                                           )
                                   )

    def clean_search_field(self):
        value = self.cleaned_data['search_field']
        pattern = r'https://[\w+|\.]*\/.+'
        match = re.fullmatch(pattern, value)
        if not match:
            raise forms.ValidationError('Ссылка должна соответствовать'
                                        ' формату: https://xxxx.ru/x/...'
                                        )
        return value
