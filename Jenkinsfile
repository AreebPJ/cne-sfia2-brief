pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'true'
        }
        stages{
            stage('Install Docker and Docker-Compose'){
                steps{
                    sh '''
                    ssh areebpanjwani09@34.105.155.158 <<EOF
                    curl https://get.docker.com | sudo bash 
                    sudo usermod -aG docker $(whoami)
                    sudo apt update
                    sudo apt install -y curl jq
                    version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
                    sudo curl -L "https://github.com/docker/compose/releases/download/${version}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                    sudo chmod +x /usr/local/bin/docker-compose
EOF
                    '''
  
            }
        }
            stage('Build frontend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("apanj/frontend")
                        }
                    }
                }          
            }
            stage('Tag & Push frontend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                                image.push("${env.app_version}")
                            }
                        }
                    }
                }          
            }
            stage('Build backend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("apanj/backend")
                        }
                    }
                }          
            }
            stage('Tag & Push backend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                                image.push("${env.app_version}")
                            }
                        }
                    }
                }          
            }
            stage('Build database Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("apanj/database")
                        }
                    }
                }          
            }
            stage('Tag & Push database Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                                image.push("${env.app_version}")
                            }
                        }
                    }
                }          
            }
            stage('Build nginx Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("nginx:latest")
                        }
                    }
                }          
            }
            stage('Deploy App'){
                steps{
                    sh "docker-compose up -d"
                }
            }
        }    
}

