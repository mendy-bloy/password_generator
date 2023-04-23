import hashlib
from password_target import PasswordTarget


# TODO maybe turn into a protocol
class PasswordGenerator:
    """
    This class generates passwords based on a password target.

    The password target is represented as:
    password_target = PasswordTarget(target_name)
    The target name is a string.

    The password is generated using the PasswordTarget object and a hash key, which is a string,
    according to the PasswordTarget attributes that represent the password target requirements.

    """

    def generate_password(self, password_target: PasswordTarget, hash_key: str) -> str:
        """
        Generates a password based on a password target and a hash key.

        Args:
            password_target (PasswordTarget): Password target object.
            hash_key (str): input hash key

        Returns:
            str: target generated password
        """

        raw_password = self._generate_raw_password(password_target.name, hash_key)[
            : password_target.length
        ]
        for idx in range(password_target.length):
            raw_password = self._modify_password(password_target, raw_password, idx)
        return raw_password

    def _generate_raw_password(self, password_target_name: str, hash_key: str) -> str:
        """
        Generates a raw password based on a password target name and a hash key.

        Args:
            password_target_name (str): password target name
            hash_key (str): input hash key

        Returns:
            str: raw password
        """
        return str(
            hashlib.sha512((password_target_name + hash_key).encode()).hexdigest()
        )

    def _handle_upper(self, hash_char: chr, password_target: PasswordTarget) -> str:
        """
        Handles a upper case character.

        Args:
            hash_char (chr): given upper case hash character
            password_target (PasswordTarget): object representing password target

        Returns:
            str: manipulated character
        """

        if password_target.min_uppers > 0:
            password_target.min_uppers -= 1
            return hash_char
        elif password_target.min_lowers > 0:
            password_target.min_lowers -= 1
            return hash_char.lower()
        elif password_target.min_digits > 0:
            password_target.min_digits -= 1
            return str(ord(hash_char) % 10)
        return hash_char

    def _handle_lower(self, hash_char: chr, password_target: PasswordTarget) -> str:
        """
        Handles a lower case character.

        Args:
            hash_char (chr): given lower case hash character
            password_target (PasswordTarget): object representing password target

        Returns:
            str: manipulated character
        """
        if password_target.min_lowers > 0:
            password_target.min_lowers -= 1
            return hash_char
        elif password_target.min_uppers > 0:
            password_target.min_uppers -= 1
            return hash_char.upper()
        elif password_target.min_digits > 0:
            password_target.min_digits -= 1
            return str(ord(hash_char) % 10)
        return hash_char

    def _handle_digit(self, hash_char: chr, password_target: PasswordTarget) -> str:
        """
        Handles a digit character.

        Args:
            hash_char (chr): given digit hash character
            password_target (PasswordTarget): object representing password target

        Returns:
            str: manipulated character
        """
        if password_target.min_digits > 0:
            password_target.min_digits -= 1
            return hash_char
        elif password_target.min_uppers > 0:
            password_target.min_uppers -= 1
            return chr(int(hash_char) % 26 + 65)
        elif password_target.min_lowers > 0:
            password_target.min_lowers -= 1
            return chr(int(hash_char) % 26 + 97)
        return hash_char

    def _modify_password(
        self, password_target: PasswordTarget, raw_password: str, index: int
    ) -> str:
        """
        Modifies a password based on a password target and a raw password and an index.

        Args:
            password_target (PasswordTarget): object representing password target
            raw_password (str): raw password
            index (int): index of character to be manipulated

        Returns:
            str: manipulated password
        """
        if raw_password[index].isupper():
            upper = self._handle_upper(raw_password[index], password_target)
            return f"{raw_password[:index]}{upper}{raw_password[index + 1 :]}"
        elif raw_password[index].islower():
            lower = self._handle_lower(raw_password[index], password_target)
            return f"{raw_password[:index]}{lower}{raw_password[index + 1 :]}"
        elif raw_password[index].isdigit():
            digit = self._handle_digit(raw_password[index], password_target)
            return f"{raw_password[:index]}{digit}{raw_password[index + 1 :]}"
