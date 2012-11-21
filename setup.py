from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.md')).read()
except IOError:
    README = CHANGES = ''


setup(name='porteira',
      version='0.1',
      description='API responsible for validating XML structures and generate python structures.',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      long_description=README,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Markup :: XML',
        ],
      keywords='Porteira API',
      author='SciELO',
      author_email='scielo-dev@googlegroups.com',
      url='https://github.com/scieloorg/porteira',
      download_url='',
      license='',
      test_suite='test',
      tests_require=['unittest'],
    )
