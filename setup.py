from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''


setup(name='porteira',
      version='0.2',
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
      keywords='xml xsd schema validation lxml xmltodict porteira',
      author='SciELO',
      author_email='scielo-dev@googlegroups.com',
      maintainer='SciELO Team',
      maintainer_email='scielo-dev@googlegroups.com',
      url='https://github.com/scieloorg/porteira',
      download_url='https://github.com/scieloorg/porteira/archive/master.zip',
      license='LICENSE.txt',
      test_suite='porteira',
      tests_require=['nose'],
      platforms='Windows, Unix and MacOS',
      install_requires=[
        "xmltodict",
        "lxml",
        ],
    )
