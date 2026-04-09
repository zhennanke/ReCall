bruno测试
# ReCall

<div align="center">
<img src="assets/model.png" width="35%">
</div>

Official implementation of [ReCall: Learning to Reason with Tool Call for LLMs via Reinforcement Learning](https://arxiv.org/abs/2503.19470). 

## Updates
- [2025/03/26] We release the [paper](https://arxiv.org/abs/2503.19470), [code](https://github.com/Agent-RL/ReCall), [dataset](https://huggingface.co/datasets/Agent-RL/ReCall), and [models](https://huggingface.co/Agent-RL/ReCall).

## Requirements
```
python 3.10+
```

## Install
```bash
git clone https://github.com/Agent-RL/ReCall.git
cd ReCall
pip install -e .
```

## Data Preparation
#### Tool Calling
```bash
mkdir -p data/tool_calling
python scripts/tool_calling_data_prepare.py
```

#### Search
```bash
mkdir -p data/search
python scripts/search_data_prepare.py
```

## Training
Please install [veRL](https://github.com/volcengine/verl) and prepare a ray cluster environment.

#### Tool Calling
```bash
bash scripts/reinforce_tool.sh
```

#### Search
```bash
bash scripts/reinforce_search.sh
```

## Evaluation
Please install [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF).

#### Tool Calling
```bash
bash scripts/evaluate_tool.sh
```

#### Search
```bash
bash scripts/evaluate_search.sh
```

## Citation
```bibtex
@article{zheng2025recall,
  title={ReCall: Learning to Reason with Tool Call for LLMs via Reinforcement Learning},
  author={Zheng, Nanke and Du, Yibing and Wu, Lianwei and Wang, Deyi and Xie, Xiangpeng and Fan, Yuchen and Zhou, Shanghang},
  journal={arXiv preprint arXiv:2503.19470},
  year={2025}
}
```