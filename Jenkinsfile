pipeline {
    agent any

    environment {
        // Docker settings
        DOCKER_REGISTRY = "gcr.io"
        PROJECT_ID = "mizizi"
        NAME = "beulahcity_com_web"
        GIT_SHA = sh (script: "git log -n 1 --pretty=format:'%H'", returnStdout: true)
        STAGE = "${env.BRANCH_NAME == "master" ? "prod" : "staging"}"
        GCR_IMAGE = "$DOCKER_REGISTRY/$PROJECT_ID/$NAME/$STAGE"
        GCR_IMAGE_SHA = "$GCR_IMAGE:$GIT_SHA"
        GCR_IMAGE_LATEST = "$GCR_IMAGE:latest"
        TARGET_SERVER = "10.133.249.13"
        DEPLOYMENT_FILE = "${env.BRANCH_NAME == "master" ? "docker-compose.prod.yaml" : "docker-compose.staging.yaml"}"
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '4'))
    }

    stages {
        stage('Build Image') {
            steps {
                // Run the Docker tool to build the image
                script {
                    docker.withTool('docker') {
                        docker.build(NAME, "-t beulahcity_com_web ./")
                    }
                }
            }
        }

        stage('Publish Image') {
            steps {
                script {
                    withCredentials([[$class: 'FileBinding', credentialsId: "mizizi-gcr-keyfile", variable: 'GCR_KEY_FILE']]) {
                        sh "docker login -u _json_key --password-stdin https://gcr.io < $GCR_KEY_FILE \
                        && docker tag $NAME $GCR_IMAGE_SHA \
                        && docker push $GCR_IMAGE_SHA \
                        && docker tag $NAME $GCR_IMAGE_LATEST \
                        && docker push $GCR_IMAGE_LATEST"
                    }
                }
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    docker.withServer("tcp://$TARGET_SERVER:2345") {
                        withCredentials([[$class: 'FileBinding', credentialsId: "mizizi-gcr-keyfile", variable: 'GCR_KEY_FILE']]) {
                            sh "docker login -u _json_key --password-stdin https://gcr.io < $GCR_KEY_FILE \
                            && docker pull $GCR_IMAGE_LATEST \
                            && docker stack deploy -c $DEPLOYMENT_FILE beulahcity_com --with-registry-auth \
                            && docker system prune -f"
                        }
                    }
                }
            }
        }
        stage('Clean Build Server') {
            steps {
                script {
                    sh "docker rmi $GCR_IMAGE_SHA"
                }
            }
        }
    }
}
