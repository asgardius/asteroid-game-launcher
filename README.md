# asteroid-game-launcher

<img src=https://git.asgardius.company/asgardius/asteroid-game-launcher/raw/branch/master/data/asgardius.page.asteroidlauncher.png>

A launcher for a space themed game

# Dependencies

* python
* GTK 3
* VTE 3

# Build dependencies
* Meson
* Ninja

# Install instructions
To build this app

meson . _build

To install

sudo ninja -C _build install

To uninstall

sudo ninja -C _build uninstall
