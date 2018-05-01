from setuptools import setup

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='lambda_filter_objects',
    version='0.2',
    description='filter a list of objects based on keywords in a string value',
    url='https://github.com/legalthings/lambda_filter_objects',
    author='Mitchel Kerckhaert',
    author_email='mitchel@legalthings.com',
    packages=['lambda_filter_objects'],
    install_requires=[],
    test_suite='nose.collector',
    tests_require = [
      'nose'
    ],
    zip_safe=False)
