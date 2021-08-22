from setuptools import setup

setup(name='shiptost',
      version='0.0.0',
      description='Shiptost API Wrapper',
      long_description=open('README.rst').read(),
      url='https://github.com/FormerlyChucks/shiptost',
      author='diogenesjunior',
      author_email='diogenesjunior@protonmail.com',
      packages=['shiptost'],
      zip_safe=False,
      keywords='Shitpost API',
      install_requires=['requests'],
      include_package_data=True
      )
