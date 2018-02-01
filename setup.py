from setuptools import setup

setup(
    name='yourscript',
    version=hello.__version__,
    py_modules=['hello'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=hello:cli
    ''',
)
