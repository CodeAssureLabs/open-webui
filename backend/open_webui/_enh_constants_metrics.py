from open_webui import constants

def symbol_count() -> int:
    return len([n for n in dir(constants) if not n.startswith('_')])

def has(name: str) -> bool:
    return hasattr(constants, name)
