from setuptools import setup

"""The setup script.
# 作者-pamela
"""

setup(
    name='pytest-change-report',
    url='https://github.com/pamela0116/pytest-change-report',
    version='1.0',
    author="pamela",
    author_email='panping0116@hotmail.com',
    description='turn . into √，turn F into x',
    long_description='print result on terminal turn . into √，turn F into x using hook',
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='proprietary',
    py_modules=['pytest_change_report'],
    keywords=[
        'pytest', 'py.test', 'pytest-change-report',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={
        'pytest11': [
            'change-report = pytest_change_report',
        ]
    }
)
