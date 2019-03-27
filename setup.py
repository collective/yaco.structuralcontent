from setuptools import setup, find_packages
import os

version = "1.0a1"

setup(
    name="yaco.structuralcontent",
    version=version,
    description="Structural Content",
    long_description=open("README.txt").read()
    + "\n"
    + open(os.path.join("docs", "HISTORY.txt")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=["Framework :: Plone", "Programming Language :: Python"],
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
    entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
