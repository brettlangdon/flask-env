import os


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
        load_all = dict.get('ENV_LOAD_ALL', False)

        # Override default configuration from environment variables
        for key, value in os.environ.items():
            # Only include environment keys that start with our prefix (if we have one)
            if not key.startswith(prefix):
                continue

            # Strip the prefix from the environment variable name
            key = key[len(prefix):]

            # Unless we specify that we want to load all environment variables
            #   only load variables that we have predefined on our object
            if not load_all and not hasattr(cls, key):
                continue

            # If value is "true" or "false", parse as a boolean
            # Otherwise, if it contains a "." then try to parse as a float
            # Otherwise, try to parse as an integer
            # If all else fails, just keep it a string
            if value.lower() in ('true', 'false'):
                value = True if value.lower() == 'true' else False
            elif '.' in value:
                try:
                    value = float(value)
                except ValueError:
                    pass
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass

            # Update our config with the value from `os.environ`
            setattr(cls, key, value)
