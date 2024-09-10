# CICD with AWS

Steps
- clone git repo https://github.com/AbdullahMansoor123/ml_end2end
- cd in ml_end2end
- make a dockerfile
- create github workflow
- create iam user and download access key
- create aws ecr repo and copy URL
- 533267203292.dkr.ecr.us-east-1.amazonaws.com/student_performance
- create ec2 instance
  - update ec2 instance
    - sudo apt-get update -y
    - sudo apt-get update 
    - curl -fsSL https://get.docker.com -o get-docker.sh
    - sudo sh get-docker.sh
    - sudo usermod -aG docker ubuntu
    - newgrp docker
- Creat Runner on github to connect repo with ec2 so every change will be exceuted
  - # Create a folder
  $ mkdir actions-runner && cd actions-runnerCopied! # Download the latest runner package
  $ curl -o actions-runner-linux-x64-2.319.1.tar.gz -L https://github.com/actions/runner/releases/download/v2.319.1/actions-runner-linux-x64-2.319.1.tar.gzCopied!# Optional: Validate the hash
  $ echo "3f6efb7488a183e291fc2c62876e14c9ee732864173734facc85a1bfb1744464  actions-runner-linux-x64-2.319.1.tar.gz" | shasum -a 256 -cCopied! # Extract the installer
  $ tar xzf ./actions-runner-linux-x64-2.319.1.tar.gzCopied!
  Configure
  # Create the runner and start the configuration experience
  $ ./config.sh --url https://github.com/AbdullahMansoor123/cicd_with_aws --token APVVSE5GDZHV4LXDHMV5S5TG4BAIECopied!# Last step, run it!
  $ ./run.sh
  Using your self-hosted runner
  # Use this YAML in your workflow file for each job
  runs-on: self-hosted

- add secret key in github for using aws through github
- 