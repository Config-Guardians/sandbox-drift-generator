TF = terraform -chdir=infra

init:
	$(TF) init

validate:
	$(TF) validate

plan: 
	$(TF) plan -var-file=infra/envs/dev.tfvars

apply:
	$(TF) apply -var-file=infra/envs/dev.tfvars

destroy:
	$(TF) destroy -var-file=infra/envs/dev.tfvars

output:
	$(TF) output -json > infra/outputs.json

.PHONY: init validate plan apply destroy output # These are not files