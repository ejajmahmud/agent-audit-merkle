"""Cryptographic Merkle tree audit log."""
import hashlib
import json
from typing import List, Optional

class MerkleAuditLedger:
    def __init__(self):
        self.leaves: List[str] = []
        self.events: List[dict] = []

    def _hash(self, val: str) -> str:
        return hashlib.sha256(val.encode("utf-8")).hexdigest()

    def append_event(self, action: str, details: dict) -> str:
        event_blob = json.dumps({"action": action, "details": details}, sort_keys=True)
        leaf_hash = self._hash(event_blob)
        self.events.append({"action": action, "details": details, "hash": leaf_hash})
        self.leaves.append(leaf_hash)
        return leaf_hash

    def get_root_hash(self) -> str:
        if not self.leaves:
            return ""
        current_level = list(self.leaves)
        while len(current_level) > 1:
            next_level = []
            for i in range(0, len(current_level), 2):
                left = current_level[i]
                right = current_level[i+1] if i + 1 < len(current_level) else left
                next_level.append(self._hash(left + right))
            current_level = next_level
        return current_level[0]

    def verify_integrity(self) -> bool:
        for ev in self.events:
            blob = json.dumps({"action": ev["action"], "details": ev["details"]}, sort_keys=True)
            if self._hash(blob) != ev["hash"]:
                return False
        return True
