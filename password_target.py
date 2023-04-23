from dataclasses import dataclass

# TODO finish this to be a proper data class
# TODO read about pydantic


@dataclass
class PasswordTarget:
    """
    Represents a password target

    Attributes
    ----------
    name : str
    min_uppers : int
    min_lowers : int
    min_digits : int
    length : int
    """

    name: str
    min_uppers: int = 0
    min_lowers: int = 0
    min_digits: int = 0
    length: int = 0

    def __init__(self, password_target_name: str) -> None:
        self.name = password_target_name
