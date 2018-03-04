from setuptools import setup

requires = [
    'requests==2.18.4',
    'GitPython==2.1.8',
    'prospector==0.12.7'
]

setup(
    name='feito',
    version='0.0.4',
    description='Automated code review in Python',
    url='http://github.com/magrathealabs/feito',
    author='Magrathea Labs',
    author_email='contact@magrathealabs.com',
    license='MIT',
    packages=['feito', 'feito/github'],
    zip_safe=False,
    keywords = ['code review', 'good code', 'linter', 'coverage', 'pronto for python'],
    scripts=['bin/feito'],
    install_requires=requires,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ]
)
