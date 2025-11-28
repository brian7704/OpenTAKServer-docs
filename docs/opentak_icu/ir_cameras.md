# IR Cameras

OpenTAK ICU supports devices with built-in IR cameras. It has been tested on the Ulefone Armor X13, Armor 22, and Armor 26 Ultra.
If you try a different model, please let us know if it worked or not on the [Discord server](https://discord.gg/6uaVHjtfXN) or by opening an issue on
the [GitHub repo](https://github.com/brian7704/OpenTAK_ICU/issues).

## Root

Due to how the IR camera's LEDs are controlled, root is required to enable or disable them. OpenTAK ICU controls them
by running the following commands as root.

```shell
# Disable the IR LEDs
echo 0 > /sys/class/flash_irtouch/flash_irtouch_data/irtouch_value
echo 0 > /sys/class/flashlight_core/flashlight/flashlight_irtorch

# Enable the IR LEDs
echo 1 > /sys/class/flash_irtouch/flash_irtouch_data/irtouch_value
echo 1 > /sys/class/flashlight_core/flashlight/flashlight_irtorch
```
