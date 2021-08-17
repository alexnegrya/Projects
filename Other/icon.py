class Icon:
    def __init__(self, icon):
        if type(icon) == str:
            self.__icon = icon
        else:
            print('Иконка передана в неверном формате!')
    
    def set(self, icon):
        if type(icon) == str:
            self.__icon = icon
        else:
            print('Иконка передана в неверном формате!')
    
    def get(self):
        return self.__icon
