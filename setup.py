from distutils.core import setup

setup(
    name='bucket',
    version='0.1.0',
    #packages=['bucket'],
    install_requires=[],
    dependency_links=[],
    description='CLI for auto "bucket"ing files by moving to proper directory filtered by type of file.',
    author='Jeff Nagasuga',
    author_email='jeffrey.nagasuga@disney.com',
    url='http://github.com/nagasuga/bucket',
    keywords=[],
    classifiers=[],
    scripts=['bin/bucket'],
)
