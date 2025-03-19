# MUG-U
MUG-U is a Multimodal Large Language Model (MLLM) that supports text, image, and video inputs, enabling powerful understanding, reasoning, and generation capabilities. Developed by the Shopee MUG team, MUG-U leverages the latest advancements and cutting-edge technologies in multimodal modeling.

# Release
**2024.02.15** We released the MUG-U API.

# Model
|            Model            |    Date    |                                           API                                            |                     Note                     |
| :-------------------------: | :--------: | :-------------------------------------------------------------------------------------------: | :------------------------------------------: |
| MUG-U-7B | 2025.02.06 | [infer](./infer_api.py) |                  Qwen2.5-7B                  |

# How to Use?
```python
python infer_api.py
```

# Performance

|Benchmark|MUG-U-7B|
|:---:|:---:|
|MMBench-V1.1<sub>test</sub>|81.8|
|MMStar|66.6|
|MMMU<sub>val</sub>|54.3|
|MathVista<sub>testmini</sub>|74.8|
|HallBench<sub>avg</sub>|51.3|
|AI2D<sub>test</sub>|88.9|
|OCRBench|91.1|
|MMVet|63|
|Average|71.5|



