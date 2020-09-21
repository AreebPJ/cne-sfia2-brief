pipeline{
        agent any
        environment {
            app_version = 'v1'
            rollback = 'true'
        }
        stages{
            stage('Build Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("apanj/frontend")
                        }
                    }
                }          
            }
            stage('Tag & Push Image'){
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
            stage('Build Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("apanj/backend")
                        }
                    }
                }          
            }
            stage('Tag & Push Image'){
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
            stage('Build Image'){
                steps{
                    script{
                        if (env.rollback == 'false'){
                            image = docker.build("apanj/database")
                        }
                    }
                }          
            }
            stage('Tag & Push Image'){
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
            stage('Deploy App'){
                steps{
                    sh "docker-compose up -d"
                }
            }
        }    
}

