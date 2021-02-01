# -*- coding:utf-8 -*-
# @Time: 2021/2/1 20:27
# @Author: Zhanyi Hou
# @Email: 1295752786@qq.com
# @File: gen_docs.py
from typing import ClassVar
from pmgwidgets.widgets.composited.generalpanel import *
from pmgwidgets import BaseExtendedWidget

g = list(globals().keys())
# class idgetDoc()
md_template = """
### {name}
"""

md_content = ''
for cls_name in g:
    if cls_name.startswith('PMG'):
        w_cls: ClassVar[BaseExtendedWidget] = globals().get(cls_name)
        try:
            if issubclass(w_cls, BaseExtendedWidget):
                template = md_template
                name = w_cls.__name__
                annotations = w_cls.__init__.__annotations__
                doc = w_cls.__init__.__doc__
                template = template.format(name=name)
                template += '#### Args \n'
                for k, v in annotations.items():
                    template += '- {k}: {v}\n'.format(k=k, v=v)
                template += '#### Docs \n\n'
                template += str(doc) + '\n'
                md_content += template
        except TypeError:
            pass
with open('pmgpanel_widgets.md', 'w') as f:
    f.write(md_content)
