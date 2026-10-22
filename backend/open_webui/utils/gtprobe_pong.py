"""Pong side of the probe helpers."""

from open_webui.utils.gtprobe_ping import ping


def pong(depth: int = 0) -> str:
    return "pong" if depth <= 0 else ping(depth - 1)
