stages {
        stage('Docker Compose Down') {
            steps {
                sh 'docker-compose down'
            }
        }
        stage('Docker Compose Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Docker Compose Up') {
            steps {
                sh 'docker-compose up -d'
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
