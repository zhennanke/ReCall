from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("src/version", "r", encoding="utf-8") as f:
    version = f.read().strip()

setup(
    name="recall",
    version=version,
    description="ReSearch and ReCall: RL for reasoning with search and tool use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "accelerate==1.8.1",
        "datasets==2.21.0",
        "numpy==1.26.4",
        "peft==0.16.0",
        "torch",
        "transformers",
        "trl",
        "vllm==0.8.4",
        "wandb",
    ],
)