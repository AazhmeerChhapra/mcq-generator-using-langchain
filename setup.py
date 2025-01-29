from setuptools import find_packages, setup

setup(
    name='MCQgenerator',
    version='0.0.1',
    author='Aazhmmer chhapra',
    author_email='aazhmeerchhapra@gmail.com',
    install_requires= ["openai", "langchain", "python-dotenv", "PyPDF2", "streamlit"],
    packages=find_packages()
)