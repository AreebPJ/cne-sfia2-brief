 
pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'false'
        }
        stages{
            stage('clone repo'){
                steps{
                    sh '''
                    ssh areebpanjwani09@35.242.153.141 <<EOF
                    rm -rf cne-sia2-brief
                    git clone https://github.com/AreebPJ/cne-sfia2-brief.git
EOF
                    '''
            }
        }
            stage('Build Images'){
                steps{
                withCredentials([string(credentialsId: 'DATABASE_URI', variable: 'DB_URI'), string(credentialsId: 'TEST_DATABASE_URI', variable: 'TDB_URI'), string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'DB_PASSWORD'), string(credentialsId: 'SECRET_KEY', variable: 'SK')]) {
                    sh '''
                    ssh areebpanjwani09@35.242.153.141<<EOF
                    cd cne-sfia2-brief
                    export DATABASE_URI=${DATABASE_URI}
                    export TEST_DATABASE_URI=$TEST_DATABASE_URI
                    export SECRET_KEY=${SECRET_KEY}
                    export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
                    docker-compose build 
EOF
                    '''
                        }
                    }
                }
            stage('Deploy App using k8'){
                steps{
                withCredentials([string(credentialsId: 'DATABASE_URI', variable: 'DB_URI'), string(credentialsId: 'TEST_DATABASE_URI', variable: 'TDB_URI'), string(credentialsId: 'MYSQL_ROOT_PASSWORD', variable: 'DB_PASSWORD'), string(credentialsId: 'SECRET_KEY', variable: 'SK')]) {
                    sh '''
                    ssh areebpanjwani09@35.242.153.141<<EOF
                    cd cne-sfia2-brief
                    export DATABASE_URI=${DATABASE_URI}
                    export TEST_DATABASE_URI=$TEST_DATABASE_URI
                    export SECRET_KEY=${SECRET_KEY}
                    export MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
                    kubectl apply -f kubernetes 
EOF
                    '''
                         }
                    }
            }

        } 
}
