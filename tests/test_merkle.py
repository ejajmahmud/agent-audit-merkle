"""Unit tests for MerkleAuditLedger."""
import unittest
from agent_audit_merkle.merkle import MerkleAuditLedger

class TestMerkleAudit(unittest.TestCase):
    def test_merkle_tree(self):
        l = MerkleAuditLedger()
        l.append_event("act1", {"data": 1})
        l.append_event("act2", {"data": 2})
        root = l.get_root_hash()
        self.assertTrue(len(root) == 64)
        self.assertTrue(l.verify_integrity())

        # Simulate tampering
        l.events[0]["details"]["data"] = 999
        self.assertFalse(l.verify_integrity())

if __name__ == "__main__":
    unittest.main()
