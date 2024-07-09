from typing import Dict, Any

from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
    email: str
    password: str

    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> "Email":
        return cls(email=data["email"], password=data["heslo"])


@dataclass(frozen=True)
class Message:
    id: int
    from_: str
    subject_short: str
    subject: str
    elapsed_time: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Message":
        return cls(
            id=int(data["id"]),
            from_=data["od"],
            subject_short=data["predmetZkraceny"],
            subject=data["predmet"],
            elapsed_time=data["kdy"],
        )
