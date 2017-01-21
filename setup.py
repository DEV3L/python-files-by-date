from setuptools import setup, find_packages

setup(
    name='files-by-daae',
    packages=find_packages(),
    version='0.1',
    description='Moves files from one directory into another grouping by created month',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-files-by-date',
    download_url='https://github.com/DEV3L/python-files-by-date/tarball/0.1',
    keywords=['dev3l', 'file management'],  # arbitrary keywords
    install_requires=[
        'pytest==2.9.2'
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    entry_points={
        'console_scripts': [
            'files-by-date = run'
        ]},
)
