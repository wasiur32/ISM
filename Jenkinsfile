pipeline {
    agent any
    
    stages {
        stage('Docker Compose Down') {
            steps {
                sh 'sudo docker-compose down'
            }
        }
        stage('Docker Compose Build') {
            steps {
                sh 'sudo docker-compose build'
            }
        }
        stage('Docker Compose Up') {
            steps {
                sh 'sudo docker-compose up -d'
            }
        }
    }
    
    post {
        success {
            echo 'Docker Compose operations successful!'
        }
        failure {
            echo 'Docker Compose operations failed!'
        }
    }
}
