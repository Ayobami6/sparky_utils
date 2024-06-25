def transform_name(name):
    result = ""
    for char in name:
        if char.isupper() and result:
            result += " "
        result += char
    return result


def str_meta(cls):
    """
    Custom decorator to automatically add __str__ method and Meta class to Django models.
    """

    def __str__(self):
        return getattr(self, "name", str(self.pk))

    cls.__str__ = __str__

    class Meta:
        verbose_name_plural = transform_name(cls.__name__) + "s"
        ordering = ["name"]
        verbose_name = transform_name(cls.__name__)
        db_table = cls.__name__.lower()

    cls.Meta = Meta

    return cls
