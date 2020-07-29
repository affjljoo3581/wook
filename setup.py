from setuptools import setup, find_packages

setup(
    name='wook',
    version='0.1.0',

    author='Jungwoo Park',
    author_email='affjljoo3581@gmail.com',

    description='Wook says hello!',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',

    keywords=['wook', 'lee wook'],
    url='https://github.com/affjljoo3581/wook',
    license='Apache-2.0',

    package_dir={'': 'src'},
    packages=find_packages('src'),
    python_requires='>=3',
    install_requires=[],

    entry_points={
        'console_scripts': [
            'wook = wook:_main',
        ]
    },

    classifiers=[
        'Environment :: Console',
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)