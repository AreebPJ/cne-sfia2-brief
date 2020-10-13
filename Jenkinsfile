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
                    ssh ubuntu@ip-172-31-32-24 <<EOF
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
            stage('clone repo'){
                steps{
                    sh '''
                    ssh ubuntu@ip-172-31-32-24<<EOF
		    rm -rf cne-sfia2-brief
                    git clone https://github.com/AreebPJ/cne-sfia2-brief.git
EOF
                    '''
            }
        }
            stage('Front end testing'){
                steps{
                withCredentials([string(credentialsId: 'DATABASE_URI', variable: 'DB_URI'), string(credentialsId: 'TEST_DATABASE_URI', variable: 'TDB_URI'), string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'DB_PASSWORD'), string(credentialsId: 'SECRET_KEY', variable: 'SK')]) {
                     sh '''
                     ssh ubuntu@ip-172-31-32-24<<EOF
                     cd cne-sfia2-brief
                     export DATABASE_URI=$DATABASE_URI
                     export TEST_DATABASE_URI=$TEST_DATABASE_URI
                     export SECRET_KEY=$SECRET_KEY
                     export MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
                     docker-compose up -d
             	     sleep 20
                     cd frontend/tests
                     docker-compose exec -T frontend pytest --cov application > frontendpytest.txt
EOF
                                 '''
                                 }
                            }
                    }
            stage('Backend testing'){
                steps{
                withCredentials([string(credentialsId: 'DATABASE_URI', variable: 'DB_URI'), string(credentialsId: 'TEST_DATABASE_URI', variable: 'TDB_URI'), string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'DB_PASSWORD'), string(credentialsId: 'SECRET_KEY', variable: 'SK')]) {
                    sh '''
                    ssh ubuntu@ip-172-31-32-24<<EOF
                    cd cne-sfia2-brief
		    export DATABASE_URI=$DATABASE_URI
		    export TEST_DATABASE_URI=$TEST_DATABASE_URI
                    export SECRET_KEY=$SECRET_KEY
                    export MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD
                    cd backend/tests
		    docker-compose exec -T backend pytest --cov application > backendpytest.txt
EOF
                    '''
                        }
                    }
                }          
            }
        } 
