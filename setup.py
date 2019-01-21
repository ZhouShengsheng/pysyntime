import re
from setuptools import setup, find_packages

with open('pysyntime/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        f.read(), re.MULTILINE).group(1)

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.readlines()

setup(
    name='pysyntime',
    version=version,
    description='SynTime implementation in Python.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/ZhouShengsheng/pysyntime',
    author='Zhou Shengsheng',
    author_email='szhou006@e.ntu.edu.sg',
    # license='MIT',
    classifiers=[
        # 'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
)
