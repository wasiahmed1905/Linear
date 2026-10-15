pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Stage') {
            steps {
                sh 'docker compose down --remove-orphans || true'
                sh 'docker compose pull'
                sh 'docker compose up -d'
                sh 'sleep 5 && curl -f http://localhost:5000/health || exit 1'
            }
        }
    }

    post {
        success {
            echo 'Deployment successful — API is UP on port 5000.'
        }
        failure {
            echo 'Deployment failed.'
        }
    }
}
