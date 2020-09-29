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
                    ssh ubuntu@ip-172-31-28-39 <<EOF
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
                    ssh ubuntu@ip-172-31-28-39 <<EOF
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
                            ssh ubuntu@ip-172-31-28-39<<EOF
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
                            ssh ubuntu@ip-172-31-28-39<<EOF
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
                            ssh ubuntu@ip-172-31-28-39 <<EOF
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
                    ssh ubuntu@ip-172-31-28-39 <<EOF
                    cd cne-sfia2-brief
                    export TEST_DATABASE_URI=mysql+pymysql://root:password@mysql:3306/testdb
                    export DATABASE_URI=mysql+pymysql://root:password@mysql:3306/testdb
                    export SECRET_KEY=password
                    export MYSQL_ROOT_PASSWORD=password
                    docker-compose up -d
EOF
                    '''
                    }

                }
            stage(' Front-end Testing'){
                steps{
                    sh '''
                    ssh ubuntu@ip-172-31-28-39 <<EOF
                    cd cne-sfia2-brief/frontend/tests
                    docker-compose exec -T frontend pytest --cov application > frontendpytest.txt
EOF
                    '''
                    }
                }
            stage('Back-end Testing'){
                steps{
                    sh '''
                    ssh ubuntu@ip-172-31-28-39 <<EOF
                    cd cne-sfia2-brief/backend/tests
                    docker-compose exec -T backend pytest --cov application > backendpytest.txt
EOF
                    '''
                    }
                }

             }              
            
        }

         
        
