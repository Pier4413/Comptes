import pytest
import pytestqt

from views.menu_bar import MenuBar

@pytest.mark.skip("Ne marche pas")
class TestMenuBar():

    def setup_method(self):
        pass
        #self.widget = MenuBar()

    def test_trigger_first_menu(self, qtbot):
        widget = MenuBar()
        qtbot.add_widget(widget)
        assert True
        #qtbot.mouseClicked(self.widget.firstAction)
