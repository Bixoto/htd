# htd

**htd** stands for **h**uman **t**ime **d**elta and is a micro-library to parse strings such as `7d4h`
into `timedelta(days=7, hours=4)`.

## Install

    pip install htd

With Poetry:

    poetry add htd

## Usage

```python
import htd

htd.parse("7d")
# => datetime.timedelta(days=7)
```
