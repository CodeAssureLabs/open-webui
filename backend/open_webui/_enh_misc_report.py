from open_webui.utils import misc

def callables() -> int:
    return len([n for n in dir(misc) if callable(getattr(misc, n, None)) and not n.startswith('_')])
