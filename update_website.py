import os
import glob
import re

directory = r'd:\agency website'
html_files = glob.glob(os.path.join(directory, '*.html'))

# Content from index.html to extract header and footer
with open(os.path.join(directory, 'index.html'), 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract head
head_match = re.search(r'(<head>.*?</head>)', index_content, re.DOTALL)
head = head_match.group(1) if head_match else ''

# Extract nav
nav_match = re.search(r'(<nav.*?</nav>)', index_content, re.DOTALL)
nav = nav_match.group(1) if nav_match else ''

# Extract footer
footer_match = re.search(r'(<footer.*?</footer>)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

# Extract script
script_match = re.search(r'(<script>\s*\(function\(\).*?</script>)', index_content, re.DOTALL)
script = script_match.group(1) if script_match else ''

# Read code.html to get main content
with open(os.path.join(directory, 'code.html'), 'r', encoding='utf-8') as f:
    code_content = f.read()

main_match = re.search(r'(<main.*?</main>)', code_content, re.DOTALL)
main_content = main_match.group(1) if main_match else ''

contact_html = f"""<!DOCTYPE html>
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

with open(os.path.join(directory, 'contact.html'), 'w', encoding='utf-8') as f:
    f.write(contact_html)

# Create connect.html
connect_main = """
<main class="pt-20">
<section class="relative pt-section-padding pb-24 px-8 overflow-hidden bg-surface-bright border-b border-outline-variant/30 min-h-[80vh] flex items-center">
    <div class="max-w-container-max mx-auto relative z-10 flex flex-col items-center text-center w-full">
        <div class="inline-flex items-center gap-2 px-4 py-2 bg-secondary-fixed text-on-secondary-fixed-variant rounded-full font-label-sm uppercase mb-8 shadow-sm">
            <span class="material-symbols-outlined text-sm icon-fill">connect_without_contact</span>
            CONNECT WITH ZELQAR
        </div>
        <h1 class="font-headline-xl text-headline-xl text-primary-container max-w-4xl mb-6">
            Ready to Build Your Cognitive Infrastructure?
        </h1>
        <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mb-12">
            Book a strategy call to explore how we can automate your operational bottlenecks, or send us a message to discuss custom enterprise solutions.
        </p>
        <div class="flex flex-col sm:flex-row items-center gap-6 justify-center w-full">
            <a class="w-full sm:w-auto inline-flex items-center justify-center px-10 py-5 bg-primary-container text-on-primary rounded-full font-label-sm uppercase tracking-wider hover:bg-primary transition-colors shadow-lg hover:shadow-xl transform hover:-translate-y-1 duration-200" href="#book">
                <span class="material-symbols-outlined mr-2 text-sm">calendar_month</span>
                Book Strategy Call
            </a>
            <a class="w-full sm:w-auto inline-flex items-center justify-center px-10 py-5 bg-transparent border-2 border-primary-container text-primary-container rounded-full font-label-sm uppercase tracking-wider hover:bg-surface-container transition-colors duration-200" href="contact.html">
                <span class="material-symbols-outlined mr-2 text-sm">mail</span>
                Contact Us
            </a>
        </div>
    </div>
    <!-- Decorative background elements -->
    <div class="absolute top-1/2 left-0 -translate-y-1/2 -translate-x-1/4 w-[600px] h-[600px] bg-secondary-container/20 rounded-full blur-3xl -z-10"></div>
    <div class="absolute top-0 right-0 -translate-y-1/4 translate-x-1/4 w-[800px] h-[800px] bg-primary-fixed/20 rounded-full blur-3xl -z-10"></div>
</section>
</main>
"""

connect_html = f"""<!DOCTYPE html>
<html class="scroll-smooth" lang="en">
{head}
<body class="bg-background text-on-surface font-body-md antialiased selection:bg-accent-gold/30 selection:text-primary-container">
{nav}
{connect_main}
{footer}
{script}
</body>
</html>"""

with open(os.path.join(directory, 'connect.html'), 'w', encoding='utf-8') as f:
    f.write(connect_html)

print('contact.html and connect.html created')

# Now update all HTML files to include Connect and Contact Us in the Nav, Mobile Menu, Footer, and JS
html_files = glob.glob(os.path.join(directory, '*.html'))

desktop_nav_blog = '<a class="nav-link font-[\'Manrope\'] text-sm font-semibold tracking-tight text-slate-600 hover:text-[#193868] transition-colors" href="blog.html" data-page="blog">Blog</a>'
desktop_nav_new = desktop_nav_blog + '''
<a class="nav-link font-['Manrope'] text-sm font-semibold tracking-tight text-slate-600 hover:text-[#193868] transition-colors" href="connect.html" data-page="connect">Connect</a>
<a class="nav-link font-['Manrope'] text-sm font-semibold tracking-tight text-slate-600 hover:text-[#193868] transition-colors" href="contact.html" data-page="contact">Contact Us</a>'''

mobile_nav_blog = '<a href="blog.html" class="block font-[\'Manrope\'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Blog</a>'
mobile_nav_new = mobile_nav_blog + '''
<a href="connect.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Connect</a>
<a href="contact.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Contact Us</a>'''

js_blog = "if(d==='blog'&&page==='blog.html')a=true;"
js_new = js_blog + r'''
if(d==='connect'&&page==='connect.html')a=true;
if(d==='contact'&&page==='contact.html')a=true;'''

# Footer updates
# Some have Blog, some don't. All have Privacy Policy.
footer_privacy = '<a class="font-[\'Manrope\'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="#">Privacy Policy</a>'
footer_new = '''<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="connect.html">Connect</a>
<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="contact.html">Contact Us</a>
''' + footer_privacy

for file_path in html_files:
    if os.path.basename(file_path) == 'code.html':
        continue # Don't modify the source code file
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    if desktop_nav_blog in content and 'data-page="connect"' not in content:
        content = content.replace(desktop_nav_blog, desktop_nav_new)
        
    if mobile_nav_blog in content and 'href="connect.html"' not in content:
        content = content.replace(mobile_nav_blog, mobile_nav_new)
        
    if js_blog in content and "d==='connect'" not in content:
        content = content.replace(js_blog, js_new)
        
    if footer_privacy in content and 'href="connect.html"' not in content:
        content = content.replace(footer_privacy, footer_new)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(file_path)}")

print("All updates complete!")
