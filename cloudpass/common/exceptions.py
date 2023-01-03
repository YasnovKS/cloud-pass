class ResponseException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if not self.message:
            return ('Возникла проблема при поиске файла, '
                    'проверьте правильность ссылки.\n'
                    'Если проблема повторяется. напишите в техподдержку '
                    '(кнопка сверху).')
        return self.message
