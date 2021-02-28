from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.behaviors import DragBehavior
from kivy.properties import BooleanProperty
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.core.window import Window


class HoverBehavior(object):
    """Hover behavior.
    :Events:
        `on_enter`
            Fired when mouse enter the bbox of the widget.
        `on_leave`
            Fired when the mouse exit the widget
    """

    hovered = BooleanProperty(False)
    border_point = ObjectProperty(None)
    '''Contains the last relevant point received by the Hoverable. This can
    be used in `on_enter` or `on_leave` in order to know where was dispatched the event.
    '''

    def __init__(self, **kwargs):
        self.register_event_type('on_enter')
        self.register_event_type('on_leave')
        Window.bind(mouse_pos=self.on_mouse_pos)
        super(HoverBehavior, self).__init__(**kwargs)

    def on_mouse_pos(self, *args):
        if not self.get_root_window():
            return  # do proceed if I'm not displayed <=> If have no parent
        pos = args[1]
        # Next line to_widget allow to compensate for relative layout
        inside = self.collide_point(*self.to_widget(*pos))
        if self.hovered == inside:
            # We have already done what was needed
            return
        self.border_point = pos
        self.hovered = inside
        if inside:
            self.dispatch('on_enter')
        else:
            self.dispatch('on_leave')

    def on_enter(self):
        pass

    def on_leave(self):
        pass


Factory.register('HoverBehavior', HoverBehavior)

from kivy.properties import StringProperty

class DraggableImage(DragBehavior, HoverBehavior, Image):

    name = StringProperty("")

    def __init__(self, **args):
        super(DraggableImage, self).__init__(**args)
        self.source_file = ""
        self.is_on_hover = False

    def on_enter(self):
        self.source_file = self.source
        self.source = "green.png"
        self.is_on_hover = True
        print(self.name)

    def on_leave(self):
        self.source = self.source_file
        self.is_on_hover = False
        print(self.name)

    def on_touch_up(self, touch):
        if self.is_on_hover:
            print(self.name)



class TestApp(App):
    def build(self):
        pass


if __name__ == '__main__':
    TestApp().run()