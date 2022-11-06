output "rds-hostname" {
  description = "Hostname of RDS instance"
  value       = aws_db_instance.admin-demand-db.address
  sensitive   = false
}

output "rds-port" {
  description = "Port of RDS instance"
  value       = aws_db_instance.admin-demand-db.port
  sensitive   = false
}

output "rds-username" {
  description = "Username of RDS instance"
  value       = aws_db_instance.admin-demand-db.username
  sensitive   = false
}
