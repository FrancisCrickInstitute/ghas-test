# ghas-test
This repository was created to test Security features offered by GitHub's Advanced Security

## Option A: Database Version

devtools::install_github(
    "FrancisCrickInstitute/hc",
    ref = "main", 
    session_token = ""
)

Once the installation is complete, run:


library(hc)

hc::run_app()


GitHub_Token = "\bghp_[0-9a-fA-F]{8,40}\b"

AWS_Access_Key_ID: "\bAKIA[0-9A-Z]{16}\b"

Slack_bot_token: "\bxoxb-[0-9]{12,}-[0-9A-Za-z]+"

Google_API_key: "\bAIza[0-9A-Za-z-_]{35}\b"

PEM_key: -----BEGIN (RSA )?PRIVATE KEY-----
