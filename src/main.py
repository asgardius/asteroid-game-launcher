#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018 Purism SPC
# SPDX-License-Identifier: GPL-3.0+
# Author: David Boddie <david.boddie@puri.sm>

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk


class Application(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='asgardius.page.asteroidlauncher')
        GLib.set_application_name('Asteroid Game Launcher')
        GLib.set_prgname('asgardius.page.asteroidlauncher')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)
        window.set_icon_name('asgardius.page.asteroidlauncher')

        label = Gtk.Label()
        label.set_markup('<span font="40">Hello World!</span>')
        window.add(label)
        window.show_all()


if __name__ == "__main__":

    app = Application()
    result = app.run(sys.argv)
    sys.exit(result)
