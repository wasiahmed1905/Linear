pipeline {
    agent any
    triggers {
        // Triggers the pipeline via the GitHub webhook[cite: 7]
        githubPush() 
    }
    stages {
        stage('Build') {
            steps {
                // Pulls your specific repository
                git branch: "main", url: "https://github.com/wasiahmed1905/Linear.git"
                
                // Ensures the API is down initially, then brings it up[cite: 7]
                sh "docker compose down"
                sh "docker compose up -d"
            }
        }
    }
}
