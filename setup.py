from setuptools import setup
# from distutils.core import setup

setup(name='novel',
      packages=['novel'],
      version='0.0.1',
      description='Novelty detection in Python',
      author='Theodore Tsitsimis',
      author_email='th.tsitsimis@gmail.com',
      url='https://github.com/tsitsimis/lemonpy',
      download_url='https://github.com/tsitsimis/novel/archive/0.0.1.tar.gz',
      keywords=['novelty', 'svm', 'machine learning'],
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',

          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 2.7'
      ],
      install_requires=[
          'numpy',
          'cvxopt'
      ],
      zip_safe=False
      )
