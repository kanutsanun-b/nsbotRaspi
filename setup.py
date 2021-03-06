from distutils.core import setup
import os.path

setup(
  name = 'nsbotRaspi',         # How you named your package folder (MyLib)
  packages = ['nsbotRaspi'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Read METAR, SPECI and Taf then send to Line application for RASPBERRY PI',   # Give a short description about your library
  long_description='plese read in: https://github.com/kanutsanun-b/nsbotRaspi',
  author = 'Kanutsanun Bouking',                   # Type in your name
  author_email = 'kanutsanun.b@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/kanutsanun-b/nsbotRaspi',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/kanutsanun-b/nsbotRaspi/archive/1.0.0.zip',    # I explain this later on
  keywords = ['NSWEB', 'METAR', 'SPECI', 'TAF', 'Raspberry Pi','kanutsanun bouking'],   # Keywords that define your package best
  install_requires=[
          'schedule', 'requests', 'selenium'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)
