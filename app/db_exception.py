
class DuplicationError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
        
class EmptyError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        
class NoneExistError(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
