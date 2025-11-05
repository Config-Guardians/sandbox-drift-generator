# Call each resource module

module "storage" {
    source         = "./modules/storage"
    project_prefix = var.project_prefix
    tags           = local.common_tags
    test_force_destroy = true
}

module "identity" {
    source         = "./modules/identity"
    project_prefix = var.project_prefix
    tags           = local.common_tags
    test_bucket_arn = module.storage.test_bucket_arn
}

module "network" {
    source         = "./modules/network"
    project_prefix = var.project_prefix
    tags           = local.common_tags
}