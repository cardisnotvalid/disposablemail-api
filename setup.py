from setuptools import setup, find_packages
from pathlib import Path


VERSION = "0.0.1"
DESCRIPTION = "DisposableMail API wrapper"
LONG_DESCRIPTION = Path(__file__).cwd().joinpath("README.md").read_text()


setup(
    name="disposablemail",
    version=VERSION,
    author="Danil Krivoshapkin",
    author_email="deadcardinal293@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["httpx"],
    keywords=[
        "python",
        "api",
        "api-wrapper",
        "tempmail",
        "temp-mail",
        "tempmail-api",
        "temp-mail-api",
        "disposablemail",
        "disposable-email",
    ],
)
