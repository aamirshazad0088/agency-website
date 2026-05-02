import os, glob

directory = r'd:\agency website'
html_files = glob.glob(os.path.join(directory, '*.html'))

mobile_nav_blog = '<a href="blog.html" class="block font-[\'Manrope\'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Blog</a>'
mobile_nav_new = mobile_nav_blog + '''
<a href="connect.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Connect</a>
<a href="contact.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Contact Us</a>'''

footer_privacy = '<a class="font-[\'Manrope\'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="#">Privacy Policy</a>'
footer_new = '''<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="connect.html">Connect</a>
<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="contact.html">Contact Us</a>
''' + footer_privacy

for file_path in html_files:
    if os.path.basename(file_path) == 'code.html': continue
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if mobile_nav_blog in content and '<a href="connect.html" class="block' not in content:
        content = content.replace(mobile_nav_blog, mobile_nav_new)
        modified = True
        
    if footer_privacy in content and 'href="connect.html">Connect</a>\n<a class="font-[\'Manrope\'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D]' not in content:
        content = content.replace(footer_privacy, footer_new)
        modified = True
        
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {os.path.basename(file_path)}")
