
from todo_app.data.item import Item
from todo_app.data.view_model import ViewModel

def test_done_items_property_only_shows_done_items_and_nothing_else():
    # arrange
    items = [
        Item(1, "Test Item 1", "To Do"),
        Item(2, "Test Item 2", "Doing"),
        Item(3, "Test Item 3", "Done")

    ]
    view_model = ViewModel(items)

    #act
    returned_items = view_model.done_items

    # assert
    assert len(returned_items) == 1
    returned_single_item = returned_items [0]
    assert returned_single_item.status == "Done"