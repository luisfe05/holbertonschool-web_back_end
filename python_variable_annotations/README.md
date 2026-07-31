# Python - Variable Annotations

## Description
This project covers Python 3 type annotations: annotating function parameters, return values, and variables with basic and complex types (`typing.List`, `Union`, `Tuple`, `Callable`, `Iterable`, `Sequence`), duck typing, and validating annotated code with `mypy`. Every module, class, and function includes a real-sentence docstring, and each script is `pycodestyle` compliant.

## Tasks

| Task | Description | File |
| :--- | :--- | :--- |
| **0. Basic annotations - add** | Type-annotated `add(a: float, b: float) -> float`. | `0-add.py` |
| **1. Basic annotations - concat** | Type-annotated `concat(str1: str, str2: str) -> str`. | `1-concat.py` |
| **2. Basic annotations - floor** | Type-annotated `floor(n: float) -> int`. | `2-floor.py` |
| **3. Basic annotations - to string** | Type-annotated `to_str(n: float) -> str`. | `3-to_str.py` |
| **4. Define variables** | Annotated module-level variables: `a: int`, `pi: float`, `i_understand_annotations: bool`, `school: str`. | `4-define_variables.py` |
| **5. Complex types - list of floats** | Type-annotated `sum_list(input_list: List[float]) -> float`. | `5-sum_list.py` |
| **6. Complex types - mixed list** | Type-annotated `sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float`. | `6-sum_mixed_list.py` |
| **7. Complex types - string and int/float to tuple** | Type-annotated `to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]`. | `7-to_kv.py` |
| **8. Complex types - functions** | Type-annotated `make_multiplier(multiplier: float) -> Callable[[float], float]`. | `8-make_multiplier.py` |
| **9. Let's duck type an iterable object** | Annotate `element_length` using `Iterable[Sequence]` and `List[Tuple[Sequence, int]]`. | `9-element_length.py` |

## Author
* **Luis Gonzalez** - Holberton School
