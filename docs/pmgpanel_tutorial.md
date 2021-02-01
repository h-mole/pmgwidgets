# Quick-Layout widget: `PMGPanel`


## Demostration

```python
from qtpy.QtWidgets import QApplication
from pmgwidgets import PMGPanel

views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
         ('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150)),
         ('number_ctrl', 'height', 'How High could This Plane fly?', 12000, 'm', (10, 20000)),
         ('check_ctrl', 'sport', 'do you like sport', True),
         ('combo_ctrl', 'plane_type', 'Fighters(Ordered by production time)', 'f22', ['f22', 'j20', 'su57'],
          ['Lockheed-Martin f22', '成都 j20', 'Сухо́й su57']),
         ('color_ctrl', 'color', 'Which color do u like?', (0, 200, 0))]
if __name__ == '__main__':
    app = QApplication([])
    panel = PMGPanel(views=views)

    panel.show()
    print('Panel Value', panel.get_value())
    app.exec_()

```

Run this demo code and get the window in result:

![](figures\settings_panel.png)

## Data structure to create a `PMGPanel`

As the example above shown, you just need a json-like data to create this UI.

There are two ways-`strict` and `simple` ,to write it, and firstly I'd like to introduce the strict one.
### Strict way to create widgets form.
```python
from qtpy.QtWidgets import QApplication
from pmgwidgets import PMGPanel

views = [
    {"type": 'line_ctrl', 'name': 'name', 'title': 'What\'s your name?', 'init': 'hzy'},
    {'type': 'number_ctrl', 'name': 'age', 'title': 'How old are you?', 'init': 88,
     'unit': 'years old', 'range': (0, 150)},
    {'type': 'number_ctrl', 'name': 'height', 'title': 'How High could This Plane fly?', 'init': 12000,
     'unit': 'm', 'range': (10, 20000)},
    {'type': 'check_ctrl', 'name': 'sport', 'title': 'do you like sport', 'init': True},
    {'type': 'combo_ctrl', 'name': 'plane_type', 'title': 'Fighters(Ordered by production time)', 'init': 'f22',
     'choices': ['f22', 'j20', 'su57'], 'texts': ['Lockheed-Martin f22', '成都 j20', 'Сухо́й su57']},
    {'type': 'color_ctrl', 'name': 'color', 'title': 'Which color do u like?', 'init': (0, 200, 0)}
]
if __name__ == '__main__':
    app = QApplication([])
    panel = PMGPanel(views=views)

    panel.show()
    print('Panel Value', panel.get_value())
    app.exec_()
```
From the code above, it's obvious that a `dict` such as

 `{"type": 'line_ctrl', 'name': 'name', 'title': 'What\'s your name?', 'init': 'hzy'}` 

stands for a parameter-tuning widget shown below:

![](figures/name_widget_on_settings_panel.png)

And the outer `list` contains all `dicts`.

### Simple  way

Simple way is like this:

```python
views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
         ('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150)),
         ('number_ctrl', 'height', 'How High could This Plane fly?', 12000, 'm', (10, 20000)),
         ('check_ctrl', 'sport', 'do you like sport', True),
         ('combo_ctrl', 'plane_type', 'plane type', 'f22', ['f22', 'f18', 'j20', 'su57'],
          ['f22战斗机', 'f18战斗轰炸机', 'j20战斗机', 'su57战斗机']),
         ('color_ctrl', 'color', 'Which color do u like?', (0, 200, 0))]
```

The data are formatted like this:

(widget_type, widget_name, hint_information, initial_value, other_informations...)

the widgets are listed at the following link below:

[Widgets List](docs/pmgpanel_widgets.md)

## Create a Quick-layout Panel
We have talked that, generally, `pmgwidgets` uses a json-like data structure. To be simplified, we call just call it "json". The Json is a `list`, arranging UI elements in top-down order.

It's recommended to pass the json into `PMGPanel` when creating the panel like this:
```
views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
             ('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
sp = PMGPanel(views=views, layout_dir='v')
```
Also, the json could be sent to the panel by the `set_items` method after creating the `PMGPanel` like this:

    views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
             ('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
    sp = PMGPanel()
    sp.set_items(views)

NOTE:  Method `set_items` could be called multiple times. However if `PMGPanel`it's not empty when calling it, the widgets added before will be **cleared**.

## Place widgets in another axis (Nested widgets)

![](figures/nested_lists_to_place_widgets.png)

    from pmgwidgets import PMGPanel
    import sys
    from qtpy.QtWidgets import QApplication
    app = QApplication(sys.argv)
    views = [
        [
            ('eval_ctrl', 'code_eval', 'Evaluate this code', 123 + 456, 'normal'),
            ('eval_ctrl', 'code_eval2', 'Evaluate this code', (1, 2, 3), 'safe')
        ],
        ('keymap_ctrl', 'key_map2', 'Key For Find', 'Ctrl+F'),
    ]
    sp2 = PMGPanel(views=views, layout_dir='v')
    sp2.set_items(views)
    sp2.show()
    sys.exit(app.exec_())

NOTE:

The json in the code above has an outer-list and inner-list, and the inner list, as a **sub-list** of the outer, has two description tuples( two  `eval_ctrl`s).

Yet **It's not supported to embed a sub-list in the inner-list**.

## Get a Widget

call  ``get_ctrl(ctrl_name:str)``method of PMGPanel, you could get the widget above.

Example:
```python
views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
		('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
sp = PMGPanel(views=views, layout_dir='v')
name_widget = sp.get_ctrl('name')
```
NOTE：If widget doesn't exist, the method returns `None` . 


## Get All Values 

Call the  ``get_value()`` method of PMGPanel，and it returns a dict , where the key is the widget name, and the value is the widget's parameter value.

If the user did not modify the value of one widget, the value of the widget will equal to the initial value. 

For example, the examples before returns this:
```python
print(sp.get_value())
{'name': 'hzy', 'age': 88.0, 'height': 12000.0, 'sport': True, 'plane_type': 'f22', 'color': (0, 200, 0)}
```

## Get value of one Widget

Use `get_value` and `set_value` method of a control widget after getting it.
```python
views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
sp = PMGPanel(views=views, layout_dir='v')
name_widget = sp.get_ctrl('name')
name_widget.get_value()
```
## Set value of one widget

```python
views = [('line_ctrl', 'name', 'What\'s your name?', 'James'),
('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
sp = PMGPanel(views=views, layout_dir='v')
name_widget = sp.get_ctrl('name')
name_widget.set_value("John")
```
The params passed in set_value method should has the same type as the initial value.

## Set value of multiple param widgets

```python
views = [('line_ctrl', 'name', 'What\'s your name?', 'James'),
('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150)),
('number_ctrl', 'age2', 'How old are you?', 88, 'years old', (0, 150))
]
sp = PMGPanel(views=views, layout_dir='v')
sp.set_value({'name':'hzy','age':123})
```
NOTE:
- An exception will be thown if key not exist in `set_value` method

## Set parameters of one widget

Call  ``set_params(*params)`` method.

``params`` 指的是从表格的 ``初始值`` 列之后的几项。比如选择菜单的选项、数据型输入框的范围。

控件的参数指的就是从第5项开始（含第5项）以后的内容。比如对于一个数值型控件：

Example:
```python
views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
sp = PMGPanel(views=views, layout_dir='v')
num_widget = sp.get_ctrl('name')
if num_widget is not None:
num_widget.set_params('years old',(10,145))
```
以上示例就是把年龄范围从0~150岁设置到了10~145岁。如果你不希望改变其他设置（比如这里的 ``'years old'`` ）， 将原有的值重新写一遍就可以了。


## Enable and Disable a widget

``` 
views = [('line_ctrl', 'name', 'What\'s your name?', 'hzy'),
('number_ctrl', 'age', 'How old are you?', 88, 'years old', (0, 150))]
sp = PMGPanel(views=views, layout_dir='v')
sp.get_ctrl('name').setEnabled(False) # Disable widget 'name'
sp.get_ctrl('name').setEnabled(True)  # Enable it
```