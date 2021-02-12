from setuptools import setup


setup(
    name='Flask-Ethereum',
    version='0.0.1a1',
    url='https://github.com/zatoichi-labs/flask-ethereum',
    license='MIT',
    author='Zatoichi Labs',
    author_email='admin@zatoichilabs.com',
    description='Flask Plugin for Ethereum',
    packages=['flask_ethereum'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'flask',
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
