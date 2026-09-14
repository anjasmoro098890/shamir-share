# shamir-share

> sss · quorum · backup

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-3776AB)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Build](https://img.shields.io/badge/build-passing-brightgreen)]()

Shamir-style share coordinator — quorum count, local vault.

## Features

- HD derivation along m/48'/0'/0' for BTC
- Passphrase-wrapped vault stored as local JSON
- Deterministic address codec (SHA-256 simulation, no live keys)
- Fee estimator with low / medium / high presets
- Balance sync against a stub RPC client
- Click CLI with vault, account and portfolio commands

## Prerequisites

- Python 3.11+
- Git

## Getting Started

```bash
git clone <repo-url>
cd shamir-share
python -m pip install -e .
python -m shamirshare --help
```

## CLI Usage

```bash
shamirshare create-vault --name "Main"
# Create an encrypted local vault

shamirshare list-vaults
# List vault files in the storage directory

shamirshare add-account --label Savings
# Derive the next HD account

shamirshare sync
# Refresh stub balances

shamirshare balance
# Print account table

shamirshare portfolio
# Show coin + stub USD total
```

## Project Structure

```
shamirshare/
  crypto/          seed, derive, address
  chain/           stub RPC and fee table
  storage/         vault JSON
  services/        wallet + sync
  cli.py           click entry
tests/             pytest
```

## Configuration

Defaults live in `shamirshare/config.py` (`WalletConfig`).

| Setting | Default | Description |
|---------|---------|-------------|
| `network` | `mainnet` | mainnet / testnet |
| `rpc_endpoint` | `offline` | BTC node URL (unused in stub mode) |
| `storage_dir` | `.wallets` | Local vault directory |
| `derivation_path` | `m/48'/0'/0'` | BIP path |

## Tests

```bash
python -m pytest -q
```

## Background

Backup desks search shamir, not multisig-wallet.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.


---

## Topics

![shamir](https://img.shields.io/badge/shamir-111827?style=flat-square) ![share](https://img.shields.io/badge/share-111827?style=flat-square) ![shamir-share](https://img.shields.io/badge/shamir%20share-111827?style=flat-square) ![cryptocurrency](https://img.shields.io/badge/cryptocurrency-111827?style=flat-square) ![wallet](https://img.shields.io/badge/wallet-111827?style=flat-square) ![blockchain](https://img.shields.io/badge/blockchain-111827?style=flat-square) ![web3](https://img.shields.io/badge/web3-111827?style=flat-square) ![bitcoin](https://img.shields.io/badge/bitcoin-111827?style=flat-square)

`shamir` `share` `shamir-share` `cryptocurrency` `wallet` `blockchain` `web3` `bitcoin` `ethereum` `hd-wallet` `open-source` `python`

Search: shamir-share · sss · quorum · backup · Shamir-style share coordinator — quorum count, local vault.

---

<sub>Shamir-style share coordinator — quorum count, local vault.</sub>
