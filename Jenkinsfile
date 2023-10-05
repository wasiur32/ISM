pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Build your application
                sh 'make build'
            }
        }
        stage('Deploy') {
            steps {
                // Deploy your application
                sh 'make deploy'
            }
        }
    }
}
