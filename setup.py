from setuptools import find_packages, setup

readme = ''
with open('README.md') as f:
    readme = f.read()


setup(
    name='minecraftstatus',
    author='Infernum1',
    url='https://github.com/Infernum1/minecraftstatus/',
    project_urls={
        "Issue Tracker": "https://github.com/Infernum1/minecraftstatus/issues",
    },
    version="0.0.2",
    license='MIT',
    description='minecraftstatus is an asynchronous wrapper for https://api.iapetus11.me.',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.8.0',
    classifiers=[
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ]
)