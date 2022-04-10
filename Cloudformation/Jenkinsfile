pipeline {
  agent any 
  environment {
    registry= "ctorio/registration"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  stages {
    stage('Clone repository') {
      steps{
        echo 'Making sure we have the repository cloned to our workspace'
        checkout scm
      }
    }
    stage('Checking python version') {
      steps {
        sh 'python --version'
      }
    }
    stage('Installing requirements'){
      steps{
        sh 'pip install --user -r src/requirements.txt'
      }
    }
    stage('Perform tidylint') {
      steps {
        sh 'tidy -q -e src/templates/*.htm' 
      }
    }
    stage('Perform pylint') {
      steps {
        sh 'pylint --disable=R,C src/server.py' 
      }
    }
    stage('Build Docker'){
      steps {
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Upload to AWS S3') {
      steps {
          withAWS(region:'us-west-2',credentials:'aws-upload') {
          sh 'echo "Uploading content with AWS creds"'
              s3Upload(pathStyleAccessEnabled: true, payloadSigningEnabled: true, file:'src', bucket:'project-pipeline-ci-cd')
          }
      }
    }
    stage('Upload to AWS EKS') {
      steps {
          withAWS(region:'us-west-2',credentials:'aws-jenkins') {
            sh "aws eks --region us-west-2 update-kubeconfig --name RegistrationEKS-i9LpCZLtgHqS"
            sh "kubectl apply -f infrastructure/aws-auth-cm.yaml"
            sh "kubectl set image deployments/registration registration=${registry}:latest"
            sh "kubectl apply -f infrastructure/capstone-app-deployment.yml"
            sh "kubectl get nodes"
            sh "kubectl get pods"
            sh "aws cloudformation update-stack --stack-name registration-worker-nodes --template-body file://infrastructure/worker_nodes.yml --parameters file://infrastructure/worker_nodes_parameters.json --capabilities CAPABILITY_IAM"
          }
      }
    }
    stage('System prune') {
      steps{
        sh "docker system prune -f"
      }
    }
    
  }
}
