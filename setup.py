import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyvsysrewards',
    version='0.0.1',
    author='Chapman Shoop',
    author_email='chapman.shoop@gmail.com',
    description='A library for calculating VSystem Supernode Rewards',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/belovachap/pyvsysrewards',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License'
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)