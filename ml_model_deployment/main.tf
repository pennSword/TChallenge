
# To deploy the resources, follow these steps:
# (1) Ensure you have Terraform installed and initialized (terraform init).
# (2) Execute terraform apply to create the resources. Terraform will prompt for confirmation before proceeding.


terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 3.0"
    }
  }
}

provider "google" {
  credentials = file("<path_to_service_account_key_json>")
  project     = "fluid-brook-344319"
  region      = "us-central1"
}

resource "google_vertex_model" "mnist_model" {
  display_name = "MNIST Model"
  artifact_uri = "gs://<bucket_name>/<model_directory>"
}

resource "google_vertex_ai_endpoint" "endpoint" {
  name         = "mnist-endpoint"
  display_name = "prediction-mnist-endpoint"
  description  = "A MNIST vertex ai endpoint in Google Cloud Platform"
  location     = "us-central1"
  region       = "us-central1"
  labels       = {
    label-one = "value-one"
  }
  network      = "projects/${data.google_project.project.number}/global/networks/${data.google_compute_network.vertex_network.name}"
  encryption_spec {
    kms_key_name = "kms-name"
  }
  depends_on   = [
    google_service_networking_connection.vertex_vpc_connection
  ]
}

resource "google_service_networking_connection" "vertex_vpc_connection" {
  network                 = data.google_compute_network.vertex_network.id
  service                 = "servicenetworking.googleapis.com"
  reserved_peering_ranges = [google_compute_global_address.vertex_range.name]
}

resource "google_compute_global_address" "vertex_range" {
  name          = "address-name"
  purpose       = "VPC_PEERING"
  address_type  = "INTERNAL"
  prefix_length = 24
  network       = data.google_compute_network.vertex_network.id
}

data "google_compute_network" "vertex_network" {
  name       = "network-name"
}

resource "google_kms_crypto_key_iam_member" "crypto_key" {
  crypto_key_id = "kms-name"
  role          = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
  member        = "serviceAccount:service-${data.google_project.project.number}@gcp-sa-aiplatform.iam.gserviceaccount.com"
}

output "endpoint_id" {
  value = google_vertex_endpoint.my_endpoint.id
}
data "google_project" "project" {}
