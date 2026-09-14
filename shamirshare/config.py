"""Runtime configuration for shamirshare."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class WalletConfig:
    """Local wallet settings. No remote credentials are stored."""

    network: str = "mainnet"
    rpc_endpoint: str = "offline"
    storage_dir: str = ".wallets"
    derivation_path: str = "m/48'/0'/0'"
    coin: str = "BTC"
    address_prefix: str = "bc1q"

    def storage_path(self) -> Path:
        """Return the vault directory, created on first use."""
        path = Path(self.storage_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path
