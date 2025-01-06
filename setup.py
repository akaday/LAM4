from setuptools import setup, find_packages

setup(
    name='LAM4',  # Name of your project
    version='0.1',
    packages=find_packages(where='lam4'),  # This will find all the packages under the 'lam4' directory
    install_requires=[
        # List of dependencies your project needs
        'pytest',  # Example dependency, replace with others if needed
    ],
    entry_points={
        'console_scripts': [
            'lam4=lam4.src.main:main',  # Assuming you want to run lam4.src.main.main() as the entry point
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.txt', '*.rst', '*.md'],  # Include README, CHANGELOG, etc.
    },
)
