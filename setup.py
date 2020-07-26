from distutils.core import setup
setup(
  name = 'pg-notify-webhook',         # How you named your package folder (MyLib)
  # packages = ['pg-notify-webhook'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'LISTEN to Postgres and NOTIFY webhooks',   # Give a short description about your library
  author = 'Vijay Balasubramaniam',                   # Type in your name
  author_email = 'vbalasu@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/vbalasu/pg-notify-webhook',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vbalasu/pg-notify-webhook/archive/1.1.tar.gz',    # I explain this later on
  keywords = ['postgres', 'notify', 'webhook'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'psycopg2-binary',
          'pyyaml'
      ],
  scripts=['bin/pg-notify-webhook'],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)
