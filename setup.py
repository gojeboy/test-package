import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(name='njabs-models',
                 version='1.0',
                 script='test',
                 author='Njabulo Nsibande',
                 author_email='dev@villagetrader.co.za',
                 description='A models package',
                 long_description=long_description,
                  long_description_content_type="text/markdown",

                 )