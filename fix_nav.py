import os, glob

directory = r'd:\agency website'
html_files = glob.glob(os.path.join(directory, '*.html'))

mobile_about = """<a href="about.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">About Us</a>\n"""
mobile_target = """<a href="contact.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Contact Us</a>"""

footer_about = """<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="about.html">About Us</a>\n"""
footer_target = """<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="contact.html">Contact Us</a>"""

for file_path in html_files:
    if os.path.basename(file_path) in ['code.html', 'about.html']: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if mobile_target in content:
        if '<a href="about.html" class="block' not in content:
            content = content.replace(mobile_target, mobile_about + mobile_target)
            modified = True
            
    if footer_target in content:
        if 'href="about.html">About Us</a>' not in content:
            content = content.replace(footer_target, footer_about + footer_target)
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed mobile/footer nav in {os.path.basename(file_path)}")
