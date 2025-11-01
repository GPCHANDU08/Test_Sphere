pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python Virtualenv') {
      steps {
        // on Linux/macOS agents
        sh '''
          python3 -m venv venv || python -m venv venv
          . venv/bin/activate
          pip install --upgrade pip
          pip install -r TestSpheree/requirements.txt
          pip install webdriver-manager pytest-html
        '''
      }
    }

    stage('Run Tests') {
      steps {
        // run tests (headless)
        sh '''
          . venv/bin/activate
          # ensure a display is available (Xvfb required on Linux agents)
          Xvfb :99 -screen 0 1920x1080x24 & sleep 1
          export DISPLAY=:99
          pytest TestSpheree/tests/test_saucedemo_login.py --html=TestSpheree/reports/jenkins_report.html --self-contained-html -q
        '''
      }
    }

    stage('Archive Reports') {
      steps {
        archiveArtifacts artifacts: 'TestSpheree/reports/**', allowEmptyArchive: false
      }
    }
  }

  post {
    always {
      echo "Build finished with status: ${currentBuild.currentResult}"
    }
  }
}
