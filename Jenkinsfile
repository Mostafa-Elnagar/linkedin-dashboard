#!/usr/bin/env groovy

def appName = 'linkedin-dashboard'
def dockerImage = "linkedin-dashboard:1.${BUILD_NUMBER}"
def containerName = 'linkedin-dashboard-container'
def appPort = '8050'
def hostPort = '8050'

node('agent-02') {
    try {
        stage('Checkout') {
            echo "Starting build for ${appName}"
            checkout scm
            echo "Code checkout completed"
        }
        
        stage('Build Docker Image') {
            echo "Building Docker image: ${dockerImage}"
            
            // Build the Docker image
            sh "docker build -t ${dockerImage} ."
            
            echo "Docker image built successfully"
        }
        
        stage('Stop Existing Container') {
            echo "Stopping existing container if running"
            
            // Stop and remove existing container if it exists
            sh "docker stop ${containerName} || true"
            sh "docker rm ${containerName} || true"
            
            echo "Existing container stopped/removed"
        }
        
        stage('Deploy Application') {
            echo "Deploying ${appName} application"
            
            // Run the new container
            sh """
                docker run -d \
                    --name ${containerName} \
                    -p ${hostPort}:${appPort} \
                    --restart unless-stopped \
                    ${dockerImage}
            """
            
            echo "Application deployed successfully"
        }
        
        stage('Health Check') {
            echo "Performing health check"
            
            // Wait a moment for the app to start
            sleep(10)
            
            // Check if the container is running
            def containerStatus = sh(
                script: "docker ps --filter name=${containerName} --format '{{.Status}}'",
                returnStdout: true
            ).trim()
            
            if (containerStatus) {
                echo "Container is running: ${containerStatus}"
                
                // Test if the application is responding
                def response = sh(
                    script: "curl -s -o /dev/null -w '%{http_code}' http://localhost:${hostPort} || echo '000'",
                    returnStdout: true
                ).trim()
                
                if (response == '200') {
                    echo "Application is healthy and responding on port ${hostPort}"
                } else {
                    echo "Application deployed but health check failed (HTTP ${response})"
                }
            } else {
                error "Container failed to start"
            }
        }
        
        stage('Cleanup') {
            echo "Cleaning up old images"
            
            // Remove old images to save disk space
            sh "docker image prune -f"
            
            echo "Cleanup completed"
        }
        
        echo "Pipeline completed successfully! ${appName} is now running on port ${hostPort}"
        
    } catch (Exception e) {
        echo "Pipeline failed: ${e.getMessage()}"
        
        // Cleanup on failure
        sh "docker stop ${containerName} || true"
        sh "docker rm ${containerName} || true"
        
        currentBuild.result = 'FAILURE'
        throw e
    }
}
