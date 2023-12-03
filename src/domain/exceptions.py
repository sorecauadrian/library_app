class ValidatorException(Exception):
    def __init__(self, message_list):
        self.__message_list = message_list

    @property
    def message_list(self):
        return self.__message_list

    def __str__(self):
        result = ""
        for message in self.message_list:
            result += message
            result += "\n"
        return result
