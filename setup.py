import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cricket-analysis',
    version='0.1.0',
    author='Siddharth Kumar',
    author_email='siddharth123sk@gmail.com',
    description='Analyse cricket with computer vision',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/siddharthksah/cricket_computer_vision_sports',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'scikit-learn',
        'tensorflow',
        'opencv-python-headless',
        'optuna',
        'pyyaml',
        'torch',
        'torchvision',
        'yacs',
        'tensorboard',
        'torchsummary'
    ],
    entry_points={
        'console_scripts': [
            'cricket_analysis=src.cli:main',
        ],
    },
    project_urls={
        'Bug Tracker': 'https://github.com/siddharthksah/cricket_computer_vision_sports/issues',
        'Source Code': 'https://github.com/siddharthksah/cricket_computer_vision_sports',
    },
    python_requires='>=3.6',
)
