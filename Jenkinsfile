pipeline {
    agent any
    
    stages {
        stage('Build Docker Image') {
            steps {
                // Build a Docker image from your Dockerfile
                script {
                    def customImage = docker.build('my-ism-docker-image:latest', '-f ./Dockerfile .')
                }
            }
        }
        
        stage('Deploy Docker Container') {
            steps {
                script {
                    def myContainer = docker.image('my-ism-docker-image:latest').run('-p 8080:80')
                }
            }
        }
    }
    
    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
