
from setuptools import setup

setup(

    name ='Math_Juan',                  # Nombre de la distribución: carpeta que contendrá a los paquetes
    version ='1.0',                     # Versión del paquete
    packages = ['Math_package_Juan'],   # Paquetes que se incluyen (ES LO MÁS IMPORTANTE)
    # install_requires=[                # Librerías necesarias
    #     'numpy',
    #     'requests'
    # ],
    author ='Juan Irisarri',
    # author_email='tu_email@example.com',
    description ='Paquete de ejemplo',
    # long_description=open('README.md').read(),
    # long_description_content_type='text/markdown',
    # url='https://github.com/tu_usuario/tu_repositorio',
    # classifiers=[
    #     'Programming Language :: Python :: 3',
    #     'License :: OSI Approved :: MIT License',
    #     'Operating System :: OS Independent',
    # ],
    python_requires='>=3.8' # no obligatorio
)
