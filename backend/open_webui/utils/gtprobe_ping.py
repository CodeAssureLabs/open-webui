"""Ping side of the probe helpers."""

from open_webui.utils.gtprobe_pong import pong


def ping(depth: int = 0) -> str:
    return "ping" if depth <= 0 else pong(depth - 1)
