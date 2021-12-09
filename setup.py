from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="arquivos_base_criar_pacote_python",
    version="0.1.0",
    author="Wesley Steve",
    author_email="wesley.silva23@hotmail.com",
    maintainer="Wesley Steve",
    maintainer_email="wesley.silva23@hotmail.com",
    license="GPL",
    description="arquivos_base_criar_pacote_python",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)
