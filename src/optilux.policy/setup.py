from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='optilux.policy',
      version=version,
      description="PP4D example project",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Alex Volkov',
      author_email='alex@flamy.ca',
      url='http://flamy.ca/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['optilux'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'Plone',
        'Products.PloneFormGen',
        'optilux.theme',
      ],
      extras_require={
        'test':['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )