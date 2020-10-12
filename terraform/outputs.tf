
output "jenkins" {
  value = aws_instance.jenkins.public_dns
}
output "test" {
  value = aws_db_instance.test.id
}


