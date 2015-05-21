from setuptools import setup, find_packages


with open('README.rst') as readme:
    long_description = ''.join(readme).strip()


setup(
    name='rsocks',
    version='0.3.0',
    author='Jiangge Zhang',
    author_email='tonyseek@gmail.com',
    description='A SOCKS reverse proxy server.',
    long_description=long_description,
    url='https://github.com/tonyseek/rsocks',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages(),
    platforms=['Any'],
    install_requires=[
        'PySocks>=1.5',
        'eventlet>=0.17',
        'click>=3.3',
        'toml.py>=0.1',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'rsocks=rsocks.cli:main',
        ],
    },
)
