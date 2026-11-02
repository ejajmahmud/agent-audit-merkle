"""Command line interface for agent-audit-merkle."""
from .merkle import MerkleAuditLedger

def main():
    ledger = MerkleAuditLedger()
    ledger.append_event("exec_command", {"cmd": "pytest"})
    ledger.append_event("file_write", {"path": "main.py"})
    print("Merkle Audit Root:", ledger.get_root_hash())
    print("Ledger Valid:", ledger.verify_integrity())

if __name__ == "__main__":
    main()
