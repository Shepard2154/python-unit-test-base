pipeline {
    agent {
        docker {
            image 'python:latest'
            args '-u root'
        }
    }

    stages {
        stage("deps") {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test + Coverage') {
            steps {
                sh '''
                    coverage run -m unittest discover -v
                    coverage report
                    coverage html
                '''
            }
        }
    }
}
