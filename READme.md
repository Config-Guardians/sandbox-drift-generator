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

(Optional)
- Thinking of introducing a chaos feature: Randomly select 2 misconfigurations to run randomly -> Stress testing the Config-Guardian application.
- Store the state to avoid the infrastructure from turning completely insecure.

## completed:
- Infra (In progress)
- Bootstrap (In progress)
- Drift Generator (In progress)
    - S3 public apply (Done)
    - S3 public revert (Done)