class Input:
    def is_valid(self):
        return self.__validate()

    def __validate(self):
        raise NotImplementedError

    def compile(self):
        raise NotImplementedError
