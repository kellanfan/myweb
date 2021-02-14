pipeline {
    agent none
    stages {
        stage('docker-build') {
            agent any
            steps {
                sh ''' cd /var/jenkins_home/workspace/My_Pipeline_main
                docker build -t hub.kellan.com/kellan/myweb .
                '''
            }
        }
    }
}