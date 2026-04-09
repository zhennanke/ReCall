from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("src/version", "r", encoding="utf-8") as f:
    version = f.read().strip()

requirements = [
    "accelerate==1.3.0",
    "bitsandbytes==0.45.3",
    "datasets==3.2.0",
    "deepspeed==0.16.4",
    "einops==0.8.0",
    "flash_attn==2.7.4.post1",
    "huggingface_hub==0.28.1",
    "liger_kernel==0.5.3",
    "math_verify==0.5.2",
    "ninja==1.11.1.3",
    "numpy==1.26.4",
    "openai==1.66.3",
    "packaging==24.2",
    "pandas==2.2.3",
    "peft==0.14.0",
    "psutil==7.0.0",
    "pybind11==2.13.6",
    "ray==2.43.0",
    "requests==2.32.3",
    "s3fs==2024.9.0",
    "sentencepiece==0.2.0",
    "torch==2.6.0",
    "transformers==4.49.0",
    "trl==0.15.2",
    "vllm==0.8.4",
    "wandb==0.19.7",
]

setup(
    name="recall",
    version=version,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    python_requires=">=3.10",
    long_description=long_description,
    long_description_content_type="text/markdown",
)