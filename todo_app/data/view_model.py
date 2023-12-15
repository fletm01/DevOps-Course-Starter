from todo_app.data.item import Item


class ViewModel:
    def __init__(self, items: list[Item]):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def todo_items(self):
        return []

    @property
    def doing_items(self):
        return []

    @property
    def done_items(self) -> list[Item]:
        output = []

        for item in self._items:
            if item.status == "Done":
                output.append(item)

        return output