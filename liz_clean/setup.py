from setuptools import setup, find_packages

setup(
    name='functions',
    version='0.1.0dev',
    author='Christopher Agard',
    author_email='cragard@gmail.com',
    description="Python library for cleaning CC lizard data",
    packages=find_packages(),
    scripts=['lizsort.py', 'mindate.py',
             'smallest.py', 'validate.py',
             'label_pattern.py', 'make_str.py',
             'replace_pattern.py', 'report_pattern.py'],
    install_requires=['pandas', 'numpy']
)
