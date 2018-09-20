from setuptools import setup, find_packages
setup(
    name='liz_number',
    version='0.1.1',
    author='Christopher Agard',
    author_email='cragard@gmail.com',
    description="Python library for cleaning CC lizard data",
    packages=find_packages(),
    scripts=['lizsort.py', 'mindate.py', 'smallest.py', 'validate.py'],
    install_requires=['pandas', 'numpy']
)
