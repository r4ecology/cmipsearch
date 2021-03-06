from setuptools import Command, find_packages, setup


DESCRIPTION = "Search and download CMIP data"
LONG_DESCRIPTION = """
**cmipsearch** is a Python package providing tools for searching and downloading CMIP data.

"""

PROJECT_URLS = {
    "Bug Tracker": "https://github.com/r4ecology/cmipsearch/issues",
    "Documentation": "https://cmipsearch.readthedocs.io/en/latest",
    "Source Code": "https://github.com/r4ecology/cmipsearch",
}

#REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]


setup(name='cmipsearch',
      version='0.1.0',
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      python_requires='>=3.6.1',
      classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

      project_urls=PROJECT_URLS,
      url = "https://github.com/r4ecology/cmipsearch",
      author='Robert Wilson',
      maintainer='Robert Wilson',
      author_email='rwi@pml.ac.uk',

      packages = ["cmipsearch"],
      setup_requires=[
        'setuptools',
        'setuptools-git',
        'wheel',
    ],
      install_requires = "pandas",
      include_package_data=True,
      package_data={'': ['data/*.csv']},
      zip_safe=False)




