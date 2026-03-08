AI Workflow Automation Setup

1. Install Python 3.10+
2. Clone repository

git clone https://github.com/username/ai-workflow-automation

3. Install dependencies

pip install -r requirements.txt

4. Add environment variables

OPENAI_API_KEY
SLACK_WEBHOOK

5. Run system

python main.py

Optional automation:

crontab -e

*/10 * * * * python main.py