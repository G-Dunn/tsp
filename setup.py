from setuptools import setup

setup(name='gpn',
      version='0.0.1',
      install_requires=[
        'numpy==1.22.2',
        'pandas==1.4.1',
        'matplotlib==3.5.1',
        'scipy==1.8.0',
        'seaborn==0.11.2',
        'gurobipy==9.5.1',
        'tqdm==4.62.3',
        'torch==1.11.0',
        'torchvision==0.12.0',
        'torchaudio===0.11.0'
      ]
)

