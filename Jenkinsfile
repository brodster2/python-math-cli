pipeline {
    agent {
        docker { image 'python:3-alpine'}
    }
    stages {
        stage('Test') {
            sh 'python3 -m unittest test_*.py'
        }
    }
}