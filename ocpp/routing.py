import functools


def on(action, *, skip_schema_validation=False):
    """ Function decorator to mark function as handler for specific action.

    This hook's argument are the data that is in the payload for the specific
    action. The hook's return value should be the Payload for that specific
    action and is send to the caller.

    It can be used like so:

        @on(Action.BootNotification):
        def on_boot_notification(charge_point_model, charge_point_vendor, **kwargs): # noqa
            print(f'{charge_point_model} from {charge_point_vendor} has booted.') # noqa

            return call_result(BootNotificationPayload(
                current_time=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S') + "Z", # noqa
                interval=30,
                status="Accepted",
            )

    The decorator takes an optional argument `skip_schema_validation` which
    defaults to False. Setting this argument to `True` will disable schema
    validation of the request and the response of the specific route.

    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        inner._on_action = action
        inner._skip_schema_validation = skip_schema_validation
        return inner
    return decorator


def after(action):
    """ Function decorator to mark function as hook to post-request hook.

    This hook's arguments are the data that is in the payload for the specific
    action.

    It can be used like so:

        @after(Action.BootNotification):
        def after_boot_notification():
            pass

    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        inner._after_action = action
        return inner
    return decorator


def create_route_map(obj):
    """
    Iterates of all attributes of the class looking for attributes which
    have been decorated by the @on() decorator It returns a dictionary where
    the action name are the keys and the decorated functions are the values.

    To illustrate this with an example, consider the following function:

        class ChargePoint:

            @on(Action.BootNotification)
            def on_boot_notification(self, *args, **kwargs):
                pass

            @after(Action.BootNotification)
            def after_boot_notification(self, *args, **kwargs):
                pass


    In this case this returns:

        {
            Action.BootNotification: {
                '_on_action': <reference to 'on_boot_notification'>,
                '_after_action': <reference to 'after_boot_notification'>,
                '_skip_schema_validation': False,
            },
        }

    """
    routes = {}
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        for option in ['_on_action', '_after_action']:
            try:
                action = getattr(attr, option)

                if action not in routes:
                    routes[action] = {}

                # Routes decorated with the `@on()` decorator can be configured
                # to skip validation of the input and output. For more info see
                # the docstring of `on()`.
                if option == '_on_action':
                    routes[action]['_skip_schema_validation'] = \
                        getattr(attr, '_skip_schema_validation', False)

                routes[action][option] = attr

            except AttributeError:
                continue

    return routes
