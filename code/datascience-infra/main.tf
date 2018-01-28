provider "aws" {
  region = "us-east-1"
}

terraform {
  backend "s3" {
    bucket = "terraform-states"
    key    = "global/datascience_hub/terraform.tfstate"
    region = "us-east-1"
    encrypt= true
    dynamodb_table = "terraform-state-lock"
  }
}

data "aws_vpc" "default_vpc" {
    default = true
}

var "instance_name" {}
var "key_path" {}
var "sg_id" {}


resource "aws_instance" "datascience_hub" {
    ami                         = "ami-b63769a1"
    availability_zone           = "us-east-1d"
    ebs_optimized               = false
    instance_type               = "t2.small"
    monitoring                  = false
    key_name                    = "default"
    vpc_security_group_ids      = ["${var.key_path}"]
    associate_public_ip_address = true
    source_dest_check           = true

    root_block_device {
        volume_type = "gp2"
        volume_size = 50
        delete_on_termination = true
    }

    connection {
        type = "ssh"
        user = "ubuntu"
        private_key = "${file("${var.key_path}")}"
        timeout = "2m"
        agent = false
    }

    provisioner "local-exec" {
        command = <<EOF
        ansible-playbook data-science-playbook.yml --key-file=${var.key_path} --user=ubuntu -b -i "${self.public_ip}"
        EOF
    }

    tags {
        "Name" = "${var.instance_name}"
        "deployment-type" = "terraform"
    }

}
