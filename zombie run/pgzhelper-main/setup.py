from setuptools import setup, find_packages

setup(
    name='pgzhelper_rw',
    version='1.0.10',
    description="Pygame Zero Helper enhance Pygame Zero with additional capabilities",
    author='Cort + Roboticsware',
    author_email='roboticsware.uz@gmail.com',
    url='https://github.com/roboticsware/pgzhelper/',
    download_url="https://github.com/roboticsware/pgzhelper/archive/refs/heads/master.zip",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["pgzero>=1.2"],
    packages=find_packages(exclude=[]),
    package_data={},
	zip_safe=False,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ],
    keywords=['roboticsware', 'neopia', 'pygame zero'],
)
