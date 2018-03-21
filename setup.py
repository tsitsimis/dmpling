from setuptools import setup
# from distutils.core import setup

setup(name='dmpling',
      packages=['dmpling'],
      version='0.0.1',
      description='Dynamic Movement Primitives in Python',
      author='Theodore Tsitsimis',
      author_email='th.tsitsimis@gmail.com',
      url='https://github.com/tsitsimis/dmpling',
      download_url='https://github.com/tsitsimis/dmpling/archive/0.0.1.tar.gz',
      keywords=['robotics', 'motion planning', 'imitation learning'],
      license='MIT',
      install_requires=[
          'numpy'
      ],
      zip_safe=False
      )
