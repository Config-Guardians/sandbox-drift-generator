# Call each resource module

module "storage" {
    source         = "./modules/storage"
    project_prefix = var.project_prefix
    tags           = local.common_tags
    test_force_destroy = true
}