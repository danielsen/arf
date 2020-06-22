import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="arf-mime",
	version="1.1.0",
	author="Dan Nielsen",
	author_email="dnielsen@fastmail.fm",
	description="An absctract representation of ARF messages.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/danielsen/arf",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 2",
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	python_requires='>=2.7'
)