import os, glob

directory = r'd:\agency website'
html_files = glob.glob(os.path.join(directory, '*.html'))

desktop_about = """<a class="nav-link font-['Manrope'] text-sm font-semibold tracking-tight text-slate-600 hover:text-[#193868] transition-colors" href="about.html" data-page="about">About Us</a>\n"""
mobile_about = """<a href="about.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">About Us</a>\n"""
footer_about = """<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="about.html">About Us</a>\n"""
js_about = "\nif(d==='about'&&page==='about.html')a=true;"

# Where to insert
desktop_target = """<a class="nav-link font-['Manrope'] text-sm font-semibold tracking-tight text-slate-600 hover:text-[#193868] transition-colors" href="contact.html" data-page="contact">Contact Us</a>"""
mobile_target = """<a href="contact.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Contact Us</a>"""
footer_target = """<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="contact.html">Contact Us</a>"""
js_target = "if(d==='contact'&&page==='contact.html')a=true;"

for file_path in html_files:
    if os.path.basename(file_path) in ['code.html', 'about.html']: continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Desktop Nav
    if desktop_target in content and 'href="about.html"' not in content:
        content = content.replace(desktop_target, desktop_about + desktop_target)
        modified = True
        
    # Mobile Nav
    if mobile_target in content and 'href="about.html"' not in content:
        content = content.replace(mobile_target, mobile_about + mobile_target)
        modified = True
        
    # Footer
    if footer_target in content and 'href="about.html"' not in content:
        content = content.replace(footer_target, footer_about + footer_target)
        modified = True
        
    # JS
    if js_target in content and "d==='about'" not in content:
        content = content.replace(js_target, js_target + js_about)
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added About Us tab to {os.path.basename(file_path)}")
