from setuptools import setup, find_packages

setup(
    name="mpl-magick",
    version="0.9.5",
    packages=find_packages(), # Bu 'src' klasörünü bulur
    entry_points={
        'console_scripts': [
            'mpl=src.main:main',  # Terminal 'mpl' deyince src/main.py içindeki main()'i çalıştırır.
        ],
    },
)
