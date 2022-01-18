class mycustomerror(TypeError):
       def __init__(self, message, code):
           super().__init__(f'Error code {code}: {message}')
           self.code = code


raise mycustomerror('We encourted the error', 300)



