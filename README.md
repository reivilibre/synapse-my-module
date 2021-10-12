# My Module for Synapse

## Installation

From the virtual environment that you use for Synapse, install this module with:
```shell
pip install path/to/synapse-my-module
```

Then alter your homeserver configuration, adding to your `modules` configuration:
```yaml
modules:
  - module: synapse_my_module.MyModule
    config:
      # Optional: example boolean flag
      example_option: True
```
