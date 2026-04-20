pipeline {
    agent any
    
    environment {
        IMAGE_NAME = "vk0908/my-app"
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
        stage('Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-cred',
                    usernameVariable: 'Docker_USER',
                    passwordVariable: 'Docker_PASS'
                )]) {
                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME:$TAG
                    '''
                }
                
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
