pipeline {
    agent {
        docker {
            image 'python:latest'
            args '-u root'
        }
    }

    triggers {
        pollSCM('* * * * *')
    }

    stages {
        stage("deps") {
            steps {
                sh 'pip install -r requirements.txt'

            }
        }
    }
}
