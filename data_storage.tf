#terraform {
#  required_providers {
#    google = {
#      source = "hashicorp/google"
#    }
#  }
#}
#
provider "google" {
  credentials = file("/home/chanez/documents/cloud/projet-m2-ia-churn-prediction-7d60af1299c7.json")
  project = "projet-m2-ia-churn-prediction"
}

## Crée un bucket GCS
#resource "google_storage_bucket" "my_bucket" {
#  name          = "ecommerce-data-bucket-storage"
#  location      = "EU"
#  force_destroy = false
#}

## Charge le fichier CSV dans le bucket GCS
#resource "google_storage_bucket_object" "object" {
#  name   = "Ecommerce_dataset.csv"
#  bucket = google_storage_bucket.my_bucket.name
#  source = "/home/chanez/documents/cloud/Ecommerce_dataset.csv"
#}

resource "google_bigquery_dataset" "Test" {
  dataset_id = "Test_ecommerce"
  description = "test"
  location = "EU"
}


# Crée une table BigQuery externe
resource "google_bigquery_table" "new_table" {
  dataset_id = google_bigquery_dataset.Test.dataset_id
  table_id   = "ecommerce_new"

  external_data_configuration {
    source_format = "CSV"
    autodetect    = true
    source_uris   = ["gs://mybucket/ecom_churn.csv /ecom_churn.csv"]
  }
}