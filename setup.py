import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='PlumedMarkdown',  
     version='0.2',
     install_requires=['markdown','PlumedToHTML'],
     author="Gareth Tribello",
     author_email="gareth.tribello@gmail.com",
     description="An extension for python markdown that allows you inlcude pretified HTML for PLUMED files",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/plumed/PlumedMarkdown.git",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: Freely Distributable",
         "Operating System :: OS Independent",
     ],
 )
