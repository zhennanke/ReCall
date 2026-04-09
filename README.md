bruno测试
# ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning & ReCall: Learning to Reason with Tool Call for LLMs via Reinforcement Learning

<p align="center">
  <img src="./assets/search-R1.png" width="100%" />
</p>

ReSearch and ReCall are effective post-training methods to improve the reasoning and search engine/tool-calling capabilities of large language models. 

- ReSearch is a reinforcement learning post-training method for enhancing LLM reasoning with interleaved search engine use. By introducing **strategic search and information filtering reward** into the RL training process, ReSearch improves both search engine utilization and final answer quality. It achieves superior performance on seven benchmarks and effectively scales with both model and data size. For example, ReSearch based on [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) achieves average gains of **6.4%** over the base model and **4.6%** over [Search-R1](https://github.com/PeterGriffinJin/Search-R1).
- ReCall is a reinforcement learning post-training method for enhancing LLM reasoning with interleaved tool calls. By incorporating **tool efficiency rewards** and **format compliance rewards**, ReCall significantly improves model performance on both open-domain and domain-specific tasks involving tool use.

## Updates
- [2025/04/15]:  We release our paper [ReCall](https://arxiv.org/pdf/2504.10420).
- [2025/04/15]:  We release our paper [ReSearch](https://arxiv.org/pdf/2503.19470).
- [2025/03/28]:  We release [verl-tool](https://github.com/volcengine/verl/tree/main/verl/tools), a lightweight framework for tool-calling and search engine interaction integrated into [veRL](https://github.com/volcengine/verl).
- [2025/03/13]:  We release [Open Search Tool](https://github.com/agentica-project/open-search-tool), a web search framework enabling multiple open web search engines and local crawling.

## Install
```bash
git clone https://github.com/agentica-project/Recall.git
cd Recall
bash scripts/install_vllm_sglang_verl.sh
```

## Training Data Preparation
We release our search-augmented [question-answer preference pairs dataset](https://huggingface.co/datasets/agentica-org/DeepScaleR-Preview-Dataset), our [strategy synthetic data](https://huggingface.co/datasets/agentica-org/ReSearch-StrategyData), and our [tool-calling preference pairs dataset](https://huggingface.co/datasets/agentica-org/ReCall-PreferenceData).

For custom data preparation, please refer to [Qwen2.5-Math train data preprocess](./src/data_preprocess/README_qwen.md) and [DeepScaleR train data preprocess](./src/data_preprocess/README.md).

## Inference and Evaluation
For details on usage and evaluation of ReSearch, please see [Inference and Evaluation for ReSearch](./src/training/verl/README.md).

For details on usage and evaluation of ReCall, please see [Inference and Evaluation for ReCall](./src/training/verl/README.md).

## Citation
```bibtex
@article{jin2025research,
  title={ReSearch: Learning to Reason with Search for LLMs via Reinforcement Learning},
  author={Jin, Peiqi and Wang, Yibo and Zhao, Hangyu and Duan, Xin and He, Yinan and Chen, Weizhu and Zhou, Kaitao and Zhou, Bowen and Rao, Jinfeng and Xie, Xing},
  journal={arXiv preprint arXiv:2503.19470},
  year={2025}
}

@article{jin2025recall,
  title={ReCall: Learning to Reason with Tool Call for LLMs via Reinforcement Learning},
  author={Jin, Peiqi and Wang, Yibo and Xu, Bing and Liu, Yidong and Duan, Xin and He, Yinan and Chen, Weizhu and Zhou, Kaitao and Rao, Jinfeng and Xie, Xing},
  journal={arXiv preprint arXiv:2504.10420},
  year={2025}
}
```