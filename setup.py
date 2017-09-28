from setuptools import setup, find_packages

setup(
    name='pcornet',
    version='0.1dev',
    packages=find_packages(),
    package_data = {'':['datasets/*.txt']},
    license='BSD 2-Clause License',
    author='Ben Neely',
    description='A "batteries included" approach to data science projects that utlize the PCORnet common data model,',
    install_requires=[
        'numpy==1.13.1',
        'SQLAlchemy==1.0.13',
        'marshmallow-sqlalchemy==0.13.1',
        'Faker==0.7.18',
        'factory-boy==2.9.2',
        'psycopg2==2.7.3',
        'pandas==0.20.3'],
)