import unittest
import gobject
import mafw

class MySourcePlugin(mafw.Source):
    __gtype_name__ = 'MySourcePlugin'
    
class MyRendererPlugin(mafw.Renderer):
    __gtype_name__ = 'MyRendererPlugin'
  
class TestMafwRegistry(unittest.TestCase):
    def test_get_instance(self):
        reg = mafw.Registry.get_instance()
        self.assertTrue(isinstance(reg, mafw.Registry))

    def test_get_sources(self):
        reg = mafw.Registry.get_instance()
        x1 = gobject.new(MySourcePlugin, uuid = 'MySourcePlugin1')
        x2 = gobject.new(MySourcePlugin, uuid = 'MySourcePlugin2')
        reg.add_extension(x1)
        reg.add_extension(x2)
        self.assertEquals(set(reg.get_sources()), set([x1, x2]))

    def test_get_renderers(self):
        reg = mafw.Registry.get_instance()
        x1 = gobject.new(MyRendererPlugin, uuid = 'MyRendererPlugin1')
        x2 = gobject.new(MyRendererPlugin, uuid = 'MyRendererPlugin2')
        reg.add_extension(x1)
        reg.add_extension(x2)
        self.assertEquals(set(reg.get_renderers()), set([x1, x2]))
        
    def test_list_plugins(self):
        # FIXME: test currently fails because list_plugins() is always
        # returning a empty list (even on C).
        reg = mafw.Registry.get_instance()
        x1 = gobject.new(MyRendererPlugin, uuid = 'MyPlugin1')
        x2 = gobject.new(MySourcePlugin, uuid = 'MyPlugin2')
        reg.add_extension(x1)
        reg.add_extension(x2)
        self.assertEquals(set(reg.list_plugins()), set([x1, x2]))

if __name__ == "__main__":
    unittest.main()
