from setuptools import setup, find_packages

setup(
    name='files_by_date',
    packages=find_packages(),
    version='0.1',
    description='This program takes an input directory and outputs the files contained within that directory into '
                'subdirectories in [YYYYMM] format based upon the file create date.',
    author='Justin Beall',
    author_email='jus.beall@gmail.com',
    url='https://github.com/DEV3L/python-package-archetype',
    download_url='https://github.com/DEV3L/python-files-by-date/tarball/0.1',
    keywords=['dev3l', 'files by date', 'sort directory'],  # arbitrary keywords
    install_requires=[
        'pytest'
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
            'files_by_date = files_by_date.main'
        ]},
)
