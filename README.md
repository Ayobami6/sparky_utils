## Sparky Utils

### Utility Package for Python and Django Projects

Reduce your code repetition using fine grained utility package for python and Django projects


#### Installation
```bash
pip install sparky-utils
```

#### View all available utility modules

```python3
import sparky_utils
print(sparky_utils.list_modules())
```

```python
['decorators', 'exceptions', 'list_modules', 'response']
```

#### User decorator

```python
from sparky_utils import str_meta


"""
 will add __str__ method the returns name property if has and id if not and Meta class
 def __str__(self):
    return self.name or self.id

class Meta:
    verbose_name = model_name
    verbose_name_plural = model_name + 's'
"""
@str_meta 
class FoodCategory(models.Model):
    name = models.CharField(max_length=100)
```




