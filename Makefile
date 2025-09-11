TF = terraform -chdir=infra

init:
	$(TF) init

validate:
	$(TF) validate

plan: validate
	$(TF) plan -var-file=envs/dev.tfvars

apply: validate
	$(TF) apply -var-file=envs/dev.tfvars

destroy:
	$(TF) destroy -var-file=envs/dev.tfvars

output:
	$(TF) output -json > ../outputs.json

.PHONY: init validate plan apply destroy output # These are not files