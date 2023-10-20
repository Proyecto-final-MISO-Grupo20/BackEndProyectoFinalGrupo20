import dataclasses
from datetime import date
from dataclasses import dataclass

@dataclass
class LoginDto:

    username: str
    password: str

    def get_attributes(self):
        return[key.name for key in dataclasses.fields(LoginDto)]
