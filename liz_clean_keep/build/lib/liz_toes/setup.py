from setuptools import setup, find_packages

setup(
    name='liz_toes',
    version='0.1.2',
    author='Christopher Agard',
    author_email='cragard@gmail.com',
    description="Python library for cleaning CC lizard data",
    packages=find_packages(),
    scripts=['label_pattern.py', 'make_str.py', 'replace_pattern.py', 'report_pattern.py', 'setup.py'],
    install_requires=['pandas', 'numpy']
)
