import setuptools
import subprocess
import os

cf_remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)
assert "." in cf_remote_version

assert os.path.isfile("cf_remote/version.py")
with open("cf_remote/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{cf_remote_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cf-remote",
    version=cf_remote_version,
    author="Northern.tech, Inc.",
    author_email="contact@northern.tech",
    description="Tooling to deploy CFEngine (and much more)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cfengine/cf-remote",
    packages=setuptools.find_packages(),
    package_data={"cf_remote": ["VERSION"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["cf-remote = cf_remote.main:main"]},
    install_requires=[
        "cryptography >= 3.4.4",
        "fabric >= 2.6.0",
        "paramiko >= 2.7.2",
        "requests >= 2.25.1",
        "apache-libcloud >= 3.3.1",
    ],
)
