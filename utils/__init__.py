import random
from dataclasses import dataclass, is_dataclass
from typing import List


def nested_dataclass(*args, **kwargs):

    def wrapper(cls):
        cls = dataclass(cls, **kwargs)
        original_init = cls.__init__

        def fill_fields(fillable_cls, fields_dict):
            for name, value in fields_dict.items():
                field_type = fillable_cls.__annotations__.get(name, None)
                if is_dataclass(field_type) and isinstance(value, dict):
                    new_obj = field_type(**value)
                    fields_dict[name] = new_obj
                elif isinstance(value, List) and hasattr(field_type, "__args__") and is_dataclass(field_type.__args__[0]):
                    list_field_type = field_type.__args__[0]
                    tmp_list = list()
                    for inner_dict in value:
                        if isinstance(inner_dict, dict):
                            inner_dataclass = list_field_type(**inner_dict)
                            inner_dataclass = fill_fields(inner_dataclass, inner_dict)
                            tmp_list.append(inner_dataclass)
                    fields_dict[name] = tmp_list
            return fillable_cls

        def __init__(self, *args, **kwargs):
            fill_fields(self, kwargs)
            original_init(self, *args, **kwargs)
        cls.__init__ = __init__
        return cls
    return wrapper(args[0]) if args else wrapper


def random_or_none(seq):
    if seq:
        return random.choice(seq)
    else:
        return None
