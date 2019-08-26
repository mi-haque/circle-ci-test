from setuptools import setup, find_packages

import version

setup(
    name="nu-ds-pipelines",
    version=version.get_version(),
    description="Programmatically author, schedule and monitor Data science pipelines/models",
    url="https://github.com/circle-ci-test",
    author_email='[mohammed.haque@news.co.uk]',
    packages=find_packages(exclude=["tests"]),
    install_requires=[

    ],
    package_data={
        '': ["*/conf/*yaml"]
    }

)
