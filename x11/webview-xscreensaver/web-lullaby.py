#!/usr/bin/env python2
import sys
import os
import webkit
import gtk
from gtk import gdk


class GsThemeWindow(gtk.Window):
    __gtype_name__ = 'GsThemeWindow'

    def __init__(self, width, height, title):
        self.__default_width = width
        self.__default_height = height
        self.__default_title = title

        super(GsThemeWindow, self).__init__()

        self.connect('destroy', gtk.main_quit)

    def do_realize(self):
        ident = os.environ.get('XSCREENSAVER_WINDOW')

        if ident is None:
            self.window = gdk.Window(
                self.get_parent_window(),
                width=self.allocation.width,
                height=self.allocation.height,
                window_type=gdk.WINDOW_TOPLEVEL,
                event_mask=self.get_events() | gdk.EXPOSURE_MASK,
                wclass=gdk.INPUT_OUTPUT,
                title=self.__default_title
            )

            self.set_size_request(self.__default_width, self.__default_height)
            self.connect('delete-event', self.on_destroy)

        else:
            self.window = gdk.window_foreign_new(int(ident, 16))
            self.window.set_events(gdk.EXPOSURE_MASK | gdk.STRUCTURE_MASK)

            x, y, w, h, depth = self.window.get_geometry()
            self.size_allocate(gdk.Rectangle(x, y, w, h))
            self.set_default_size(w, h)
            self.set_size_request(w, h)

            self.set_decorated(False)

        self.window.set_user_data(self)
        self.style.attach(self.window)
        self.set_flags(self.flags() | gtk.REALIZED)

    def on_destroy(self, widget, *data):
        """
        :return: True: no, don't close
        :rtype: bool
        """

        message_dialog = gtk.MessageDialog(
            parent=self,
            flags=gtk.DIALOG_MODAL & gtk.DIALOG_DESTROY_WITH_PARENT,
            type=gtk.MESSAGE_QUESTION,
            buttons=gtk.BUTTONS_OK_CANCEL,
            message_format='Click on \'Cancel\' to leave the application open.'
        )
        message_dialog.show_all()
        result = message_dialog.run()
        message_dialog.destroy()

        return result == gtk.RESPONSE_CANCEL


class Screensaver(object):
    def __init__(self, title):
        self.__title = title

        self.__window = None
        self.__browser = None

    def __webview_on_javascript_console_message(self, webview, message, line, sourceid):
        return True  # True prevents calling original handler

    def __webview_on_title_change(self, webview, title):
        browser_title = webview.get_title()

        new_title = self.__title
        if browser_title is not None:
            new_title = '{}: {}'.format(self.__title, browser_title)

        self.__window.set_title(new_title)

    def start(self, url):
        self.__window = GsThemeWindow(800, 600, self.__title)
        self.__browser = webkit.WebView()

        self.__browser.connect('console-message', self.__webview_on_javascript_console_message)
        self.__browser.connect('notify::title', self.__webview_on_title_change)

        # self.__browser.set_border_width(0)
        self.__browser.set_double_buffered(True)
        self.__browser.set_transparent(True)
        self.__browser.set_editable(False)
        # self.__browser.set_view_mode(False)
        self.__browser.set_view_source_mode(False)

        settings = self.__browser.get_settings()
        # settings.set_property('enable_accelerated_compositing', True)
        # settings.set_property('enable_webgl', True)
        settings.set_property('enable_default_context_menu', False)

        self.__window.add(self.__browser)

        self.__browser.open(url)
        self.__window.show_all()
        gtk.main()


def get_url(arg):
    """
    :type arg: str
    :rtype: str
    """

    if '://' in arg:
        return arg

    if arg.startswith('/'):
        return arg

    base_dir = os.path.abspath(os.path.dirname(__file__))

    return os.path.join('file://', base_dir, arg)


def main(args):
    """
    :rtype: int
    """
    url = 'http://google.com'
    if len(args) > 0:
        url = get_url(args[0])

    Screensaver(title='Screensaver').start(url)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
