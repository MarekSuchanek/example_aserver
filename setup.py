from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(
    name='example_aserver',
    version='0.1',
    keywords='web app async server testing',
    description='Example AIOHTTP server for test usage',
    long_description=long_description,
    author='Marek Suchánek',
    author_email='suchama4@fit.cvut.cz',
    license='MIT',
    url='https://github.com/MarekSuchanek/example_aserver',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'example_aserver = myapp:start',
        ]
    },
    install_requires=[
        'aiohttp'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: AsyncIO'
    ],
)
