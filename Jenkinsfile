pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/yourusername/ai-chatbot-devops.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ai-chatbot .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 ai-chatbot'
            }
        }
    }
}
