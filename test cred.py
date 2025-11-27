# This file contains intentionally fake, non-functional secrets
# for GitHub Advanced Security (GHAS) alert testing only.

import requests

# --- Fake AWS Access Key ---
AWS_ACCESS_KEY_ID = "AKIAFAKE1234567890AB"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMIFAKESECRETKEY1234567890abcd"

# --- Fake GitHub Personal Access Token (PAT) ---
GITHUB_PAT = "ghp_FAKESECRET1234567890abcdefghijklmnopqrstu"

# --- Fake Azure Key ---
AZURE_CLIENT_SECRET = "azur3clientsecr3tFAKE-1234-5678-ABCDEF123456"

# --- Fake Slack Token ---
SLACK_BOT_TOKEN = "xoxb-123456789012-1234567890123-FAKESECRETKEY"

# --- Fake Google API Key ---
GOOGLE_API_KEY = "AIzaSyFAKE_KEY_FOR_GHAS_TESTING_12345678"

# Sample use of a fake key (won't work)
def call_api():
    url = "https://example.com/api"
    headers = {"Authorization": f"Bearer {GITHUB_PAT}"}
    response = requests.get(url, headers=headers)
    return response.status_code

if __name__ == "__main__":
    print("Testing GHAS secret detection...")
