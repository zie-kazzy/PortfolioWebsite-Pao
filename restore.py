import json
import re

transcript = '/home/kiuren/.gemini/antigravity-cli/brain/b26330d6-2572-4a5d-a025-ee6a30d0fa9f/.system_generated/logs/transcript_full.jsonl'
with open(transcript) as f:
    lines = f.readlines()

for line in lines:
    data = json.loads(line)
    if data.get('type') == 'VIEW_FILE':
        content = data.get('content', '')
        if 'index.html' in content:
            # Extract lines
            match = re.search(r'Showing lines 1 to \d+\n(.*?)(?:\nThe above content|$)', content, re.DOTALL)
            if match:
                file_lines = match.group(1).strip().split('\n')
                file_lines = [re.sub(r'^\d+:\s', '', l) for l in file_lines if not l.startswith('The following code has been modified')]
                with open('/home/kiuren/Documents/PortfolioWebsite-Pao/index.html', 'w') as out:
                    out.write('\n'.join(file_lines))
                    print("Restored index.html")
        elif 'styles.css' in content:
            match = re.search(r'Showing lines 1 to \d+\n(.*?)(?:\nThe above content|$)', content, re.DOTALL)
            if match:
                file_lines = match.group(1).strip().split('\n')
                file_lines = [re.sub(r'^\d+:\s', '', l) for l in file_lines if not l.startswith('The following code has been modified')]
                with open('/home/kiuren/Documents/PortfolioWebsite-Pao/styles.css', 'w') as out:
                    out.write('\n'.join(file_lines))
                    out.write('\n/* NOTE: Remaining lines of original styles.css were lost */\n')
                    print("Restored styles.css")
