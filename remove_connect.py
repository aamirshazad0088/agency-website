import os, glob

directory = r'd:\agency website'
html_files = glob.glob(os.path.join(directory, '*.html'))

desktop_connect = """<a class="nav-link font-['Manrope'] text-sm font-semibold tracking-tight text-slate-600 hover:text-[#193868] transition-colors" href="connect.html" data-page="connect">Connect</a>\n"""
mobile_connect = """<a href="connect.html" class="block font-['Manrope'] text-sm font-semibold uppercase tracking-wider text-slate-700 hover:text-amber-600 transition-colors no-underline">Connect</a>\n"""
footer_connect = """<a class="font-['Manrope'] text-sm tracking-wide text-slate-400 hover:text-[#E2C08D] transition-colors no-underline" href="connect.html">Connect</a>\n"""
js_connect = "\nif(d==='connect'&&page==='connect.html')a=true;"

for file_path in html_files:
    if os.path.basename(file_path) == 'code.html': continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    if desktop_connect in content:
        content = content.replace(desktop_connect, "")
        modified = True
    else:
        # try without newline
        desktop_connect_no_nl = desktop_connect.strip() + "\n"
        if desktop_connect_no_nl in content:
            content = content.replace(desktop_connect_no_nl, "")
            modified = True
        elif desktop_connect.strip() in content:
            content = content.replace(desktop_connect.strip(), "")
            modified = True
            
    if mobile_connect in content:
        content = content.replace(mobile_connect, "")
        modified = True
    else:
        if mobile_connect.strip() in content:
            content = content.replace(mobile_connect.strip(), "")
            modified = True
            
    if footer_connect in content:
        content = content.replace(footer_connect, "")
        modified = True
    else:
        if footer_connect.strip() in content:
            content = content.replace(footer_connect.strip(), "")
            modified = True
            
    if js_connect in content:
        content = content.replace(js_connect, "")
        modified = True
    else:
        if js_connect.strip() in content:
            content = content.replace(js_connect.strip(), "")
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Removed Connect tab from {os.path.basename(file_path)}")

# Optional: Remove connect.html if it exists
connect_path = os.path.join(directory, 'connect.html')
if os.path.exists(connect_path):
    os.remove(connect_path)
    print("Deleted connect.html")
