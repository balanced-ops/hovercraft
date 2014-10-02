from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

tests_require = [
    'nose',
    'nose-cov',
    'mock',
    'webtest',
]

version = '0.0.0'
try:
    import hovercraft
    version = hovercraft.__version__
except ImportError:
    pass


setup(
    name='hovercraft',
    version=version,
    packages=find_packages(),
    install_requires=[
        'click',
        'boto',
        'requests',
        'docker-py',
    ],
    extras_require=dict(
        tests=tests_require,
    ),
    tests_require=tests_require,
    test_suite='nose.collector',
)
