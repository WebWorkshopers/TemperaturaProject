from setuptools import setup, find_packages


setup(
    name='temproject',
    version='0.1.0',
    packages=find_packages(),

    package_data={
        '': ['*.html'],
    },

    install_requires=['tornado'],
)
