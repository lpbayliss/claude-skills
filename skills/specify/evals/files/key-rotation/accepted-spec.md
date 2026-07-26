# Customer-key rotation specification

- **Artifact status:** Accepted
- **Acceptance authority:** Security lead and data-platform owner
- **Scope:** Rotate customer envelope-encryption keys without interrupting reads or writes.

## Accepted sequence

1. Create and verify the new key.
2. Write new data with the new key while retaining read support for the old key.
3. Re-encrypt existing records in resumable batches.
4. Verify every live record can be decrypted with the new key.
5. Revoke the old key after the accepted 30-day compatibility window.

## Failure handling

If verification fails at any stage, reactivate the old key and roll back the rotation. Restore and record-count reconciliation must be rehearsed before the rotation begins.
