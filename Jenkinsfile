pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ai-chatbot .'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker run -d -p 5000:5000 ai-chatbot'
            }
        }

    }
}
