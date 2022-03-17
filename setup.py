import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rie_estimator",
    version="v0.0.2-beta",
    author="José Antonio Duarte Mendieta",
    author_email="jose.duarte@cimat.mx",
    description="Function to estimate the oracle RIE corrrelation estimator of a dataset",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jduarte00/rie_estimator",
    py_modules = ['rie_estimator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research",
        'Topic :: Scientific/Engineering :: Mathematics',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial :: Investment'

    ],
    python_requires=">=3",
    install_requires=[
        "pandas",
        "numpy"
    ],
    keywords = 'applied-mathematics finance portfolio-theory correlation-matrices noise-reduction random-matrix-theory'
)
