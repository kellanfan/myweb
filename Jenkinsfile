pipeline {
    agent none
    stages {
        stage('docker-build') {
            agent any
            steps {
                sh 'docker build -t hub.kellan.com/kellan/myweb .'
            }
        }
    }
}