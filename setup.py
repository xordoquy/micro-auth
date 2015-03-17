from distutils.core import setup
from setuptools import find_packages


install_requires = [
    'django>1.7',
    'pyzmq',
]

tests_require = [
    'pytest',
    'pytest-cov>=1.4',
    'pytest-django',
    'factory_boy',
]


setup(
    name='microauth',
    version=__import__('microauth').VERSION,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
    },
)
