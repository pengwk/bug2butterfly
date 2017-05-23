from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='bug2butterfly',
      version='0.1',
      description='A notebook to document every bug you write!',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Bug Tracking',
      ],
      keywords='collect bugs',
      url='http://github.com/pengwk/bug2butterfly',
      author='pengwk',
      author_email='pengwk2@gmail.com',
      license='MIT',
      packages=[''],
      install_requires=[
          #'markdown',
      ],
      include_package_data=True,
      zip_safe=False)