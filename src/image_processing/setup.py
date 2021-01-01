from setuptools import setup
from setuptools import find_packages
package_name = 'image_processing'

setup(
    name=package_name,
    version='0.10.1',
    packages=find_packages(exclude=['test']),
    py_modules=[
        'src.image',
        'src.IPM',
        'VPSNet.testing',
        ],

  
    
    install_requires=['setuptools'],
    zip_safe=True,
    author='Bhuvan Aggarwal',
    author_email='bhuvanaggarwal9@gmail.com',
    maintainer='same',
    maintainer_email='same',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='image processing for parking subsystem',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image = src.image:main',
            'IPM = src.IPM:main',
            'testing = VPSNet.testing:main',

        ],
    },
) 