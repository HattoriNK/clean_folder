from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.9.0',
      description='script for clean folder',
      url='https://github.com/HattoriNK/clean_folder',
      author='Hattori',
      author_email='lethalshot13@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clear-folder = clean_folder.clean:']}
      )