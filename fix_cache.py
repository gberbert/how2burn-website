import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r') as f:
        content = f.read()
    
    # Replace anything matching style.css?v=X.X
    content = re.sub(r'style\.css\?v=[0-9\.]+', 'style.css?v=1.6.9', content)
    # Also replace bare style.css
    content = content.replace('href="style.css"', 'href="style.css?v=1.6.9"')
    
    with open(file, 'w') as f:
        f.write(content)
print('Updated cache busters.')
