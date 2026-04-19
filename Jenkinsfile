pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-app"
        TAG = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/vk0809/docker-jenkins.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$TAG .'
            }
        }

        stage('Run') {
            steps {
                sh '''
                docker rm -f my-container || true
                docker run -d -p 5000:5000 --name my-container $IMAGE_NAME:$TAG
                '''
            }
        }

    }
}
