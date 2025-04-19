from setuptools import setup, find_packages

setup(
    name="eval-rag",
    version="0.0.1",
    description="A comprehensive evaluation toolkit for assessing Retrieval-Augmented Generation (RAG) outputs using linguistic, semantic, and fairness metrics",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Mohamed Shaad",
    author_email="shaadclt@gmail.com",
    url="https://github.com/shaadclt/Eval-RAG",
    packages=find_packages(),
    install_requires=[
        "torch",
        "sacrebleu",
        "rouge-score",
        "bert-score",
        "transformers",
        "nltk",
        "textblob",
        "textstat",
 
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
)