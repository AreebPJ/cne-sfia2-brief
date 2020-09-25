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
                    ssh areebpanjwani09@34.105.231.62 <<EOF
                    curl https://get.docker.com | sudo bash 
                    sudo usermod -aG docker $(whoami)
                    sudo apt update
                    sudo apt install -y curl jq
                    version=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r '.tag_name')
                    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
                    sudo chmod +x /usr/local/bin/docker-compose
                    sudo chmod 666 /var/run/docker.sock
EOF
                    '''
  
            }
        }
            stage('clone repo and change directory'){
                steps{
                    sh '''
                    ssh areebpanjwani09@34.105.231.62<<EOF
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
                            ssh areebpanjwani09@34.105.231.62<<EOF
                            cd cne-sfia2-brief/frontend
                            docker build -t frontend . 
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
                            ssh areebpanjwani09@34.105.231.62<<EOF
                            cd cne-sfia2-brief/backend
                            docker build -t backend . 
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
                            ssh areebpanjwani09@34.105.231.62 <<EOF
                            cd cne-sfia2-brief/database
                            docker build -t mysql . 
EOF
                            '''
                        }
                    }
                }          
            }
            stage('Deploy App'){
                steps{
                    sh '''
                    ssh areebpanjwani09@34.105.231.62 <<EOF
                    cd cne-sfia2-brief
                    export DATABASE_URI=$DATABASE_URI
                    export SECRET_KEY=$SECRET_KEY
                    export MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
                    docker-compose up -d
EOF
                    '''
                    }
                }
            stage('Testing'){
                steps{
                    sh '''
                    ssh areebpanjwani09@34.105.231.62 <<EOF
                    cd cne-sfia2-brief/frontend/test
                    docker-compose exec frontend pytests --cov application > frontendpytest.txt
                    cd cne-sfia2-brief
                    cd cne-sfia2-brief/backend/test 
                    docker-compose exec frontend pytests --cov application > backendpytest.txt
                    
EOF
                    '''
                    }
                }             
            }

        } 
        
