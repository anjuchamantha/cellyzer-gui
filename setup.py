from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="cellyzer-gui",
    version="1.0.0",
    description="GUI for Cellyzer,a CDR(Call Data Records) data analyzing library",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/anjuchamantha/cellyzer---CDR-data-analyzer",
    project_urls={
        "Documentation": "https://anjuchamantha.github.io/cellyzer---CDR-data-analyzer/",
        "Source Code": "https://github.com/anjuchamantha/cellyzer---CDR-data-analyzer",
    },
    author="Team Cellyzer",
    author_email="chamantha97anju@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["cellyzer_gui"],
    include_package_data=True,
    install_requires=[
        "cellyzer >= 1.1.1",
        "dash == 1.10.0",
        "dash_admin_components == 0.1.4",
        "dash_bootstrap_components == 0.9.2",
    ],
    entry_points={
        "console_scripts": [
            "cellyzer-gui = cellyzer_gui.gui:main"
        ]
    }
)
