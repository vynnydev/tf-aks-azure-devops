variable "location" {
  type        = string
  description = "App Location"
  default     = "Brazil South"
}

variable "app_name" {
  type        = string
  description = "App name"
  default     = "tf"
}

variable "tags" {
  default = {
    owner      = "vynnydev"
    managed-by = "terraform"
  }
}
