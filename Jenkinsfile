pipeline {
    agent any 

    stages {
        stage('Build') { 
            steps { 
                echo "Build..."
		sh 'sudo docker login -u ${USRDOCKERHUB} -p ${PASSDOCKERHUB}'
		sh 'sudo docker build -t telegramfriend:${BUILD_NUMBER} .'
		sh 'sudo docker tag telegramfriend:${BUILD_NUMBER} correiabrux/telegramfriend:${BUILD_NUMBER}'
		sh 'sudo docker push correiabrux/telegramfriend:${BUILD_NUMBER}'
            }
        }
        stage('Test'){
            steps {
                 echo "Test"
            }
        }
        stage('Deploy') {
            steps {
                echo "Deploy"
                sh 'gcloud container clusters get-credentials mycluster --zone us-central1-a --project myclusterk8s'
                sh 'kubectl set image deployment/telegramfriend telegramfriend=correiabrux/telegramfriend:${BUILD_NUMBER}'
            }
        }
    }
}
