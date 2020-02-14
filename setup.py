from setuptools import setup

setup(
    name='snapshot-o-naut 3000',
    version='0.1',
    author='Alex Costan',
    author_email='alexcostan13@gmail.com',
    description='Snapshot-O-Naut 3000 is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/Acostan13/AWS-Snapshot-o-naut',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
