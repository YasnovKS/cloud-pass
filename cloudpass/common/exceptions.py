class ResponseException(Exception):
    '''Custom exception for response troubles.'''
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        if not self.message:
            return ('Возникла проблема при поиске файла, '
                    'проверьте правильность ссылки.\n'
                    'Если проблема повторяется. напишите в техподдержку '
                    '(кнопка сверху).')
        return self.message


class WrongLinkException(Exception):
    '''Custom exception for link validation errors.'''
    def __str__(self):
        return ('Введенная ссылка содержит ошибки или предназначена '
                'для сервиса, который не обслуживается данным приложением. '
                'Проверьте правильность ссылки.'
                )
