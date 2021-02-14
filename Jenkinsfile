pipeline {
    agent none
    stages {
        stage('build') {
            agent {
                docker {
                    image 'python'
                }
            }
            steps {
                sh 'pip install Flask flask-restful psycopg2 pyyaml requests lxml -i http://pypi.douban.com/simple --trusted-host pypi.douban.com'
            }
        }
        stage('Start')
            agent any
            steps {
                sh 'flask run --host=0.0.0.0 --port=80'
            }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}