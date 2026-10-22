"""Ping side of the probe helpers (package root)."""

from open_webui.gtprobe_pong import pong


def ping(depth: int = 0) -> str:
    return "ping" if depth <= 0 else pong(depth - 1)
