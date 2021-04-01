from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='MeaxisNetwork',
  version='0.1.4',
  description='A python wrapper for the MeaxisNetwork API.',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://meaxisnetwork.net/create/docs/api/index',  
  author='MeaxisNetwork',
  author_email='meaxis@meaxisnetwork.net',
  license='MIT', 
  classifiers=classifiers,
  keywords='meaxisnetwork', 
  packages=find_packages(),
  install_requires=['requests'],
  include_package_data = True
)