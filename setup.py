from setuptools import setup

setup(
    name='hello',
    version=hello.__version__,
    py_modules=['hello'],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        hello=hello:cli
    ''',
)
