from flask import Flask, render_template, redirect, request
from todo_app.data.view_model import ViewModel
from todo_app.flask_config import Config
from todo_app.data.trello_items import get_items, move_item_to_done
from todo_app.data.mongo_items import add_item

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    @app.route('/')
    def index():
        items = get_items()
        view_model = ViewModel(items)
        return render_template('index.html', view_model = view_model)

    @app.route('/add_new_items', methods=['POST'])
    def add_new_item():
        new_item_title = request.form.get('Title')
        add_item (new_item_title)
        return redirect('/')

    @app.route('/complete-items/<todo_id>', methods=['POST'])
    def complete_item(todo_id):
        move_item_to_done(todo_id)
        return redirect('/')

    return app