# Webhooks

Webhooks allow real-time notifications to be sent to your server when specific events occur.

## Supported Events
- `account.created`
- `transaction.completed`

## Setup
1. Go to your dashboard.
2. Navigate to **Webhooks**.
3. Enter your server URL.

## Signature Verification
We sign every webhook request with a secret.

### Example:
```bash
X-Signature: sha256=abcdef123456
