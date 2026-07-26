# Implementation discovery and accepted update

The external KMS supports disabling a key before revocation, but revocation is permanent and the provider exposes no undelete or rollback operation.

The security lead and data-platform owner have accepted this correction:

- Before revocation, pause batch work and continue dual-key reads; the old key can be re-enabled.
- Revocation is the point of no return.
- After revocation, recovery is roll-forward: restore affected ciphertext from the tested backup if needed, then re-encrypt with the new key.
- The restore rehearsal and record-count reconciliation must pass before revocation.

This update supersedes the original claim that the old key can always be reactivated.
