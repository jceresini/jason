# Tools for working with Jason

## Converting to Jason

Example:

```python
from dataclasses import dataclass
from datetime import date
from typing import Optional

from jason import convert_to_jason


@dataclass
class Employee:
    first_name: str
    last_name: str
    date_of_birth: Optional[date] = None


x = Employee(first_name="John", last_name="Doe")

print(x)
print(convert_to_jason(x))
```

Example output:

```
Employee(first_name='John', last_name='Doe', date_of_birth=None)
Employee(first_name='Jason', last_name='Doe', date_of_birth=None)
```
