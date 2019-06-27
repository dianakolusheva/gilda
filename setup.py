from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(name='gilda',
      version='0.1.0',
      description=('Grounding for biomedical entities with contextual '
                   'disambiguation'),
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/bgyori/gilda',
      author='Benjamin M. Gyori, Harvard Medical School',
      author_email='benjamin_gyori@hms.harvard.edu',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ],
      packages=find_packages(),
      install_requires=['regex', 'pandas'],
      extras_require={'test': ['nose', 'coverage']},
      keywords=['nlp', 'biology']
      )