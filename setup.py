from setuptools import setup
from setuptools import find_packages
import versioneer

# README #
def readme():
    with open('README.md') as f:
        return f.read()

AUTHORS = [
    ("Nicholas Leach", "nicholas.leach@stx.ox.ac.uk"),
    ("Stuart Jenkins", "stuart.jenkins@wadham.ox.ac.uk"),
    ("Chris Smith", "c.j.smith1@leeds.ac.uk"),
    ("Richard Millar", "richard.millar@ouce.ox.ac.uk"),
    ("Zeb Nicholls", "zebedee.nicholls@climate-energy-college.org"),
    ("Myles Allen", "myles.allen@ouce.ox.ac.uk"),
]

setup(
    name='fair',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Python package to perform calculations with the FaIR simple climate model',
    long_description=readme(),
    keywords='simple climate model temperature response carbon cycle emissions forcing',
    url='https://github.com/OMS-NetZero/FAIR',
    author=", ".join([author[0] for author in AUTHORS]),
    author_email=", ".join([author[1] for author in AUTHORS]),
    license='Apache 2.0',
    packages=find_packages(exclude=['docs*']),
    package_data={'': ['*.csv']},
    python_requires='>=3.6, <4',
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
        'numexpr',
        'scipy',
        'tqdm',
    ],
    extras_require = {
        'examples': ['jupyter', 'seaborn', 'matplotlib'],
    },
    zip_safe=False,
)
