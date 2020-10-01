pipeline{
        agent any
        stages{
            stage('Clone repo'){
                steps{
                    sh '''
                    ssh ubuntu@ip-172-31-17-85 << EOF
		    rm -rf cne-sfia2-brief
                    git clone https://github.com/AreebPJ/cne-sfia2-brief.git
EOF                 
                    '''
                }
            }
            stage('Install Docker and Docker-Compose'){
                steps{
                    sh '''
                    ssh ubuntu@ip-172-31-20-98 <<EOF
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
         
	    stage('Deploy the application'){
                steps{
                    sh '''
                    ssh ubuntu@ip-172-31-17-85 <<EOF 
                    cd cne-sfia2-brief
                    sudo docker-compose up -d
EOF              
                    '''
                }
            }
        }    
}
