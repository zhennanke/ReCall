from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

with open('src/version', 'r', encoding='utf-8') as f:
    version = f.read().strip()

setup(
    name='recall',
    version=version,
    packages=find_packages(),
    install_requires=[
        'transformers==4.50.3',
        'datasets==3.5.0',
        'trl==0.16.0',
        'vllm==0.8.4',
        'flash_attn==2.7.4.post1',
        'math_verify==0.7.0',
        'liger-kernel==0.5.6',
        'wandb==0.19.9',
        'numpy==1.26.4',
        'peft==0.15.1',
        'deepspeed==0.16.7',
        'accelerate==1.6.0',
    ],
    python_requires='>=3.10',
    include_package_data=True,
    package_data={'': ['version']},
    description='ReCall: Learning to Reason with Tool Call for LLMs via Reinforcement Learning',
    long_description=readme,
    long_description_content_type='text/markdown',
)