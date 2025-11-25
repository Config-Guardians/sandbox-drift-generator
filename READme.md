# Running Instructions for sandbox
1. Bootstrap should run first since it's required for infra (No makefile for bootstrap yet)
2. Makefile is available to run infra sandbox
    - Commands will looke like
        ```bash
        make init
        make validate

# Running Instructions for drift generator
1. Go into the drift folder of the repository, you should see a main.py file in your working directory
2. Run the following command
   ```bash
   python main.py
3. This will open up the TUI, from which you can simply follow the instructions to utilize the drift generator to it's full capacity.

# Pre-requisites
In order to run these commands, you will need to generate an AWS access key and have aws-cli call that profile 'FYP', this key must have full access to the following services:
1. FullS3Access
2. FullIAMAccess
3. FullVPCAccess
   
# Structure of the repository
## bootstrap folder
The bootstrap folder is a one-time setup. Its job is to provision the backend resources Terraform needs to store state and enforce locks.
It spins up the following:
- S3 -> To store the terraform.tfstate file
- DynamoDB Table -> To utilise when locking the state

## infra folder
The infra folder houses the sandbox which will be utilised to test the Config-Guardian application.
Services implemented for scenarios:
1. S3 Buckets
2. IAM Identities
3. Security Groups (Coupled with a micro EC2)

This will spin up a secure baseline infrastructure.

## drift folder
This folder houses the configuration drift generator. The idea is to have apply and revert scripts to introduce misconfigurations into the secure baseline created from the infra folder.
### plan:
- Have separate folders with a pair of apply and revert scripts to introduce the misconfigurations, and safely revert it back to secure state.
- Have an interactive CLI (TUI) which would allow us to use a command to run any script
- Have a global controller to manage recipes and introduce stress testing, chaos mode which selects and applies randomly multiple recipes and applies it to the cloud at the same time.

## completed:
- Infra (Done)
    - S3 storage scenario (Done)
    - SG network scenario (Done)
    - IAM identity scenario (Done)
- Bootstrap (Done)
- Drift Generator (Done)
    - S3 apply/revert recipes [3] (Done)
    - IAM apply/revert recipes [3] (Done)
    - SG apply/revert recipes [2] (Done)
