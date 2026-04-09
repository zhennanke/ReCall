# Copyright 2024 Bytedance Ltd. and/or its affiliates
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import pathlib

import setuptools
from setuptools import setup, find_packages

base_dir = pathlib.Path(__file__).parent

with open(base_dir / "README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

version_file = os.path.join("src", "version")
with open(version_file, encoding="utf-8") as f:
    version = f.read().strip()

setup(
    name="recall",
    version=version,
    author="Bytedance ltd.",
    author_email="",
    description="ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={"": ['py.typed']},
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "setuptools<69.3.0",
        "transformers>=4.49.0",
        "datasets>=3.3.2",
        "torchdata==0.11.0",
        "numpy>=2.2.4",
        "peft>=0.15.0",
        "vllm==0.8.4",
        "timm>=1.0.15",
        "latex2sympy2_extended>=1.10.1",
        "math_verify>=0.7.0",
    ],
)