import json
import os
import sys


# DEV: In `python3` we raise `JSONDecodeError` instead of `ValueError` on a bad parse
json_decode_error = ValueError
if sys.version_info.major == 3:
    json_decode_error = json.decoder.JSONDecodeError


class MetaFlaskEnv(type):
    def __init__(cls, name, bases, dict):
        """
        MetaFlaskEnv class initializer.

        This function will get called when a new class which utilizes this metaclass is defined,
        as opposed to when it is initialized.
        """
        super(MetaFlaskEnv, cls).__init__(name, bases, dict)

        # Get our internal settings
        prefix = dict.get('ENV_PREFIX', '')
        as_json = dict.get('AS_JSON', True)

        # Override default configuration from environment variables
        for key, value in os.environ.items():
            # Only include environment keys that start with our prefix (if we have one)
            if not key.startswith(prefix):
                continue

            # Strip the prefix from the environment variable name
            key = key[len(prefix):]

            # Attempt to parse values as JSON if requested (default behavior)
            # DEV: This will ensure that doing `PREFIX_PORT=8000` will result in `int(8000)` and not `str(8000)`
            if as_json:
                try:
                    value = json.loads(value)
                except json_decode_error:
                    pass

            # Update our config with the value from `os.environ`
            setattr(cls, key, value)
