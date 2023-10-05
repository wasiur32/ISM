pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                // Build your Docker image
                script {
                    def dockerImage = docker.build('my-docker-image:latest', './path/to/Dockerfile', dockerfileDir: '.')
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                // Push the Docker image to a container registry (e.g., Docker Hub)
                sh 'docker push my-docker-image:latest'
            }
        }
        stage('Deploy Docker Container') {
            steps {
                // Deploy the Docker container (e.g., using Docker Compose or Kubernetes)
                sh 'docker-compose up -d'
            }
        }
    }
}
