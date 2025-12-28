#!/usr/bin/env python3
import gi
import subprocess

gi.require_version("Gtk", "3.0")
gi.require_version("AyatanaAppIndicator3", "0.1")

from gi.repository import Gtk, AyatanaAppIndicator3 as AppIndicator3

APPINDICATOR_ID = "brightness-control"

def set_brightness(value):
    subprocess.run(
        ["ddcutil", "setvcp", "10", str(value)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

class BrightnessApp:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            APPINDICATOR_ID,
            "display-brightness-symbolic",
            AppIndicator3.IndicatorCategory.SYSTEM_SERVICES,
        )

        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())

    def build_menu(self):
        menu = Gtk.Menu()

        for level in [10, 25, 50, 75, 100]:
            item = Gtk.MenuItem(label=f"{level}%")
            item.connect("activate", self.set_level, level)
            menu.append(item)

        menu.append(Gtk.SeparatorMenuItem())

        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", Gtk.main_quit)
        menu.append(quit_item)

        menu.show_all()
        return menu

    def set_level(self, widget, level):
        set_brightness(level)

if __name__ == "__main__":
    BrightnessApp()
    Gtk.main()

