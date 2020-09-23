pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
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
            stage('clone repo and change directory'){
                steps{
                    sh '''
                    ssh areebpanjwani09@34.105.155.158 <<EOF
                    git clone https://gitlab.com/AreebP/cne-sfia2-brief.git
                    cd cne-sfia2-brief
EOF
                    '''
            }
        }
      
            stage('Build frontend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            cd cne-sfia2-brief/frontend
                            docker build -t apanj/frontend . 
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Tag & Push frontend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            docker push apanj/frontend
                            }
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Build backend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            cd cne-sfia2-brief/backend
                            docker build -t apanj/backend . 
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Tag & Push backend Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            docker push apanj/backend
                            }
EOF
                            ''' 
                        }
                    }
                }          
            }
            stage('Build database Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            cd cne-sfia2-brief/database
                            docker build -t apanj/database . 
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Tag & Push database Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials'){
                            docker push apanj/database
                            }
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Build nginx Image'){
                steps{
                    script{
                            sh '''
                            ssh areebpanjwani09@34.105.155.158 <<EOF
                            cd cne-sfia2-brief
                            docker build -t nginx:latest . 
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Deploy App'){
                steps{
                    sh '''
                    ssh areebpanjwani09@34.105.155.158 <<EOF
                    cd cne-sfia2-brief
                    docker-compose up -d
EOF
                    '''
                }
            }
        }    
}
