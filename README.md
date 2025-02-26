# MUG-U
MUG-U is a Multimodal Large Language Model (MLLM) that supports text, image, and video inputs, enabling powerful understanding, reasoning, and generation capabilities. Developed by the Shopee MUG team, MUG-U leverages the latest advancements and cutting-edge technologies in multimodal modeling.

# Release
**2024.02.15** We released the MUG-U API.

|            Model            |    Date    |                                           API                                            |                     Note                     |
| :-------------------------: | :--------: | :-------------------------------------------------------------------------------------------: | :------------------------------------------: |
| MUG-U-7B | 2025.12.06 | [infer](./infer_api.py) |                  Qwen2.5-7B                  |

# How to Use?
```python
python infer_api.py
```

# Performance

|Benchmark|MUG-U-7B|
|:---:|:---:|
|MMBench-V1.1<sub>test</sub>|82.2|
|MMStar|67.2|
|MMMU<sub>val</sub>|56.3|
|MathVista<sub>testmini</sub>|74.6|
|HallBench<sub>avg</sub>|50.1|
|AI2D<sub>test</sub>|89.0|
|OCRBench|90.5|
|MMVet|61.2|
|Average|71.4|



