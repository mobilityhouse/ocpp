import functools


def on(action):
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

    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        inner._on_action = action
        return inner
    return decorator


def after(action):
    """ Function decorator to mark function as hook to post-request hook.

    The hook doesn't receive any argument and its return value is ignored.

    It can be used like so:

        @after(Action.BootNotificaton):
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
            },
        }

    """
    routes = {}
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        for hook in ['_on_action', '_after_action']:
            try:
                action = getattr(attr, hook)

                if action not in routes:
                    routes[action] = {}
                routes[action][hook] = attr

            except AttributeError:
                continue

    return routes
