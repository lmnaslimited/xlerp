from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in xlerp/__init__.py
from xlerp import __version__ as version

setup(
	name="xlerp",
	version=version,
	description="Experience LERP",
	author="LMNAs Cloud Solutions",
	author_email="hello@lmnas.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
