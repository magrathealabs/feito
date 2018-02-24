from setuptools import setup

requires = [
    'requests==2.18.4',
    'GitPython==2.1.8',
    'prospector==0.12.7'
]

setup(
    name='feito',
    version='0.1',
    description='Automated code review in Python',
    url='http://github.com/magrathelabs/feito',
    author='Magrathea Labs',
    license='MIT',
    packages=['feito'],
    zip_safe=False,
    install_requires=requires
)