from distutils.core import setup
setup(
  name = 'bbp',         # How you named your package folder (MyLib)
  packages = ['bbp'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GPLv3', 
  description = 'A wrapper for boto3 paginators to iterate per resource',
  author = 'Matthew Davis',
  author_email = 'bbp@mdavis.xyz',
  url = 'https://github.com/mlda065/bbp',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/mlda065/bbp/archive/v_01.tar.gz',
  keywords = ['boto3', 'boto', 'AWS', 'Amazon', 'paginator', 'pagination', 'page', 'api', 'cloud'],
  install_requires=['boto3'],
  classifiers=[ # https://pypi.org/classifiers/
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
