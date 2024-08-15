---
icon: at
description: >-
  Use utility decorators to reduce your code boiler plate, by annotating your
  models and views
---

# Decorators

```python
from sparky_utils.decorators import str_meta


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
