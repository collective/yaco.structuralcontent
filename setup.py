from setuptools import setup, find_packages
import os

version = "1.0a1"

setup(
    name="yaco.structuralcontent",
    version=version,
    description="Structural Content",
    long_description=open("README.rst").read()
    + "\n"
    + open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.0",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Lock, structural, content",
    author="Juan A. Diaz",
    author_email="jdiaz@menttes.com",
    url="https://github.com/collective/yaco.structuralcontent",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["yaco"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "plone.app.z3cform",
        # -*- Extra requirements: -*-
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            # Plone KGS does not use this version, because it would break
            # Remove if your package shall be part of coredev.
            # plone_coredev tests as of 2016-04-01.
            "plone.testing>=5.0.0",
            "plone.app.robotframework[debug]",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
