from .state import dp
from .first_register_echo import dp
from .echo import dp


__all__ = ["dp"]


"""
При создании других файлов в src/commands нужно импортировать из них dp, как это сделано выше.
Ничего изменять в списке публичных объектов (__all__) не нужно.
"""