pipeline {
    agent any

    tools {
        maven 'Maven-3'
    }

    environment {
        GEMINI_API_KEY = credentials('GEMINI_API_KEY')
    }

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Lohi2005/ai-chatbot-devops3.git'
            }
        }

        stage('Build with Maven') {
            steps {
                bat 'mvn -v'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t ai-chatbot .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 -e GEMINI_API_KEY=%GEMINI_API_KEY% ai-chatbot'
            }
        }

    }
}
