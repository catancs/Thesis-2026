# Dataset Card for IFEval

## Dataset Summary
This dataset contains the prompts used in the **Instruction-Following Eval (IFEval)** benchmark for large language models. It contains around 500 "verifiable instructions" such as *"write in more than 400 words"* and *"mention the keyword of AI at least 3 times"* which can be verified by heuristics. 

To load the dataset, run:

```python
from datasets import load_dataset

ifeval = load_dataset("google/IFEval")
```

## Supported Tasks and Leaderboards
The IFEval dataset is designed for evaluating chat or instruction fine-tuned language models and is one of the core benchmarks used in the Open LLM Leaderboard.

## Languages
The data in IFEval are in English (BCP-47 `en`).

---

## Dataset Structure

### Data Instances
An example of the `train` split looks as follows:

```json
{
    "key": 1000,
    "prompt": "Write a 300+ word summary of the wikipedia page \"https://en.wikipedia.org/wiki/Raymond_III,_Count_of_Tripoli\". Do not use any commas and highlight at least 3 sections that has titles in markdown format, for example *highlighted section part 1*, *highlighted section part 2*, *highlighted section part 3*.",
    "instruction_id_list": [
        "punctuation:no_comma",
        "detectable_format:number_highlighted_sections",
        "length_constraints:number_words"
    ],
    "kwargs": [
        {
            "num_highlights": null,
            "relation": null,
            "num_words": null,
            "num_placeholders": null,
            "prompt_to_repeat": null,
            "num_bullets": null,
            "section_spliter": null,
            "num_sections": null,
            "capital_relation": null,
            "capital_frequency": null,
            "keywords": null,
            "num_paragraphs": null,
            "language": null,
            "let_relation": null,
            "letter": null,
            "let_frequency": null,
            "end_phrase": null,
            "forbidden_words": null,
            "keyword": null,
            "frequency": null,
            "num_sentences": null,
            "postscript_marker": null,
            "first_word": null,
            "nth_paragraph": null
        },
        {
            "num_highlights": 3,
            "relation": null,
            "num_words": null,
            "num_placeholders": null,
            "prompt_to_repeat": null,
            "num_bullets": null,
            "section_spliter": null,
            "num_sections": null,
            "capital_relation": null,
            "capital_frequency": null,
            "keywords": null,
            "num_paragraphs": null,
            "language": null,
            "let_relation": null,
            "letter": null,
            "let_frequency": null,
            "end_phrase": null,
            "forbidden_words": null,
            "keyword": null,
            "frequency": null,
            "num_sentences": null,
            "postscript_marker": null,
            "first_word": null,
            "nth_paragraph": null
        },
        {
            "num_highlights": null,
            "relation": "at least",
            "num_words": 300,
            "num_placeholders": null,
            "prompt_to_repeat": null,
            "num_bullets": null,
            "section_spliter": null,
            "num_sections": null,
            "capital_relation": null,
            "capital_frequency": null,
            "keywords": null,
            "num_paragraphs": null,
            "language": null,
            "let_relation": null,
            "letter": null,
            "let_frequency": null,
            "end_phrase": null,
            "forbidden_words": null,
            "keyword": null,
            "frequency": null,
            "num_sentences": null,
            "postscript_marker": null,
            "first_word": null,
            "nth_paragraph": null
        }
    ]
}
```

### Data Fields
The data fields are as follows:

- `key`: A unique ID for the prompt.
- `prompt`: Describes the task the model should perform.
- `instruction_id_list`: An array of verifiable instructions. See Table 1 of the paper for the full set with their descriptions.
- `kwargs`: An array of arguments used to specify each verifiable instruction in `instruction_id_list`.

---

## Data Splits
| Split | Count |
|:---|:---:|
| `train`  | 541 |

## Licensing Information
The dataset is available under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0).

## Citation Information
```bibtex
@misc{zhou2023instructionfollowingevaluationlargelanguage,
      title={Instruction-Following Evaluation for Large Language Models}, 
      author={Jeffrey Zhou and Tianjian Lu and Swaroop Mishra and Siddhartha Brahma and Sujoy Basu and Yi Luan and Denny Zhou and Le Hou},
      year={2023},
      eprint={2311.07911},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2311.07911}, 
}
```

---

Source: [Google IFEval Model Card](https://huggingface.co/datasets/google/IFEval)