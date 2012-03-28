from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='chapter9.concepts',
      version=version,
      description="Unit & Doc tests for chapter 9 concepts",
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
      url='https://github.com/avolkov/PP4D',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['chapter9'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone'
      ],
      extras_require = {'test':['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
