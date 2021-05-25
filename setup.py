from setuptools import find_packages, setup

setup(
    name="breathe_in",
    version="1.0",
    packages=find_packages(),
    license="Private",
    description="4 7 8 Breathing technique to calm your mind",
    author="sukhbinder",
    author_email="sukh2010@yahoo.com",
    entry_points={
        'console_scripts': ['breathe = breath_in.breadth:main']
    },
    install_requires=["keyboard"],


)
