from typing import Optional, List

import time

import httpx

from ._spinner import spinner
from ._models import Email, Message


class DisposableMail:
    _client: httpx.Client

    base_url = "https://www.disposablemail.com"
    headers = {"X-Requested-With": "XMLHttpRequest"}

    def __init__(self) -> None:
        self._client = httpx.Client(base_url=self.base_url, headers=self.headers)

    def close(self) -> None:
        if hasattr(self, "_client"):
            self._client.close()

    def __enter__(self) -> "DisposableMail":
        return self

    def __exit__(self, *args) -> None:
        self.close()

    def get_email(self) -> Email:
        response = self._client.get("/index/index")
        data = response.json()
        return Email.from_dict(data)

    def get_mailbox(self) -> List[Message]:
        response = self._client.get("/index/refresh")
        data = response.json()
        return list(map(Message.from_dict, data))

    def get_message(self, message_id: int) -> str:
        response = self._client.get(f"/email/id/{message_id}")
        return response.text

    def wait_message(self, *, attempts: int = 10, delay: float = 3) -> Optional[Message]:
        try:
            while attempts > 0:
                with spinner(f"Waiting message. Attempts left: {attempts}"):
                    if len(mailbox := self.get_mailbox()) > 1:
                        print(f"\r", end="\033[K", flush=True)
                        return mailbox.pop(0)
                    attempts -= 1
                    time.sleep(delay)
            else:
                print(f"\r", end="\033[K", flush=True)
                return None
        except KeyboardInterrupt:
            pass
