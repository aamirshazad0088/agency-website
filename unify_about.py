import os, re

directory = r'd:\agency website'

# Read index.html for standard shell
with open(os.path.join(directory, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

head_match = re.search(r'(<head>.*?</head>)', index_content, re.DOTALL)
head = head_match.group(1) if head_match else ''

nav_match = re.search(r'(<nav.*?</nav>)', index_content, re.DOTALL)
nav = nav_match.group(1) if nav_match else ''

footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

script_match = re.search(r'(<script>\s*\(function\(\).*?</script>)', index_content, re.DOTALL)
script = script_match.group(1) if script_match else ''

# Read about.html to extract main content
with open(os.path.join(directory, 'about.html'), 'r', encoding='utf-8') as f:
    about_content = f.read()

main_match = re.search(r'(<main.*?</main>)', about_content, re.DOTALL)
main_content = main_match.group(1) if main_match else ''

# Construct unified about.html
unified_about = f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
{head}
<body class="bg-background text-on-surface font-body-md antialiased selection:bg-accent-gold/30 selection:text-primary-container">
{nav}
<div class="pt-20">
{main_content}
</div>
{footer}
{script}
</body>
</html>"""

with open(os.path.join(directory, 'about.html'), 'w', encoding='utf-8') as f:
    f.write(unified_about)

print('about.html has been unified with index.html navigation and layout.')
