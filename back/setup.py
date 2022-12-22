from setuptools import setup

setup(
    name="bgpview",
    version="0.1.0",
    author="Sefa Eyeoglu",
    author_email="contact@scrumplex.net",
    description="API client for BGPView.io API",
    license="GPL3",
    keywords="bgpview client library bgp asn as ip",
    url="https://gitlab.com/Scrumplex/pyqis",
    packages=["bgpview"],
    install_requires=["requests"],
    setup_requires=["wheel"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Internet",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
