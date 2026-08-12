"""SATAN Connect subsystem.

This package adds the local gateway, device registry, pairing flow, and
protocol definitions used by SATAN AI to reach companion devices.
"""

from .service import SATANConnectService, get_service

__all__ = ["SATANConnectService", "get_service"]
