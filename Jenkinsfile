pipeline {
    agent {
        docker { image 'python:3-alpine'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest test_*.py'
            }
        }
    }
}