import os, glob

old_footer = """<footer class="w-full py-16 bg-[#193868] border-t border-white/10">
<div class="max-w-[1280px] mx-auto flex flex-col md:flex-row justify-between items-center px-8 gap-8">
<a href="index.html" class="text-xl font-bold text-white no-underline">Zorex</a>
<div class="font-['Manrope'] text-sm tracking-wide text-[#E2C08D]">© 2024 Zorex AI Automation Agency. Precision-engineered growth.</div>
<div class="flex flex-wrap justify-center gap-6">"""

new_footer = """<footer class="w-full py-16 bg-[#193868] border-t border-white/10">
<div class="max-w-[1280px] mx-auto flex flex-col md:flex-row justify-between items-start md:items-center px-8 gap-12 md:gap-8">
<div class="flex flex-col gap-4">
<a href="index.html" class="text-2xl font-bold text-white no-underline">Zorex</a>
<div class="flex flex-col gap-2">
<a href="mailto:hello@zorex.com" class="font-['Manrope'] text-sm tracking-wide text-slate-300 hover:text-white transition-colors no-underline flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">mail</span> hello@zorex.com</a>
<a href="tel:+18005550199" class="font-['Manrope'] text-sm tracking-wide text-slate-300 hover:text-white transition-colors no-underline flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">call</span> +1 (800) 555-0199</a>
<a href="https://calendly.com/zorex-strategy" target="_blank" class="font-['Manrope'] text-sm tracking-wide text-slate-300 hover:text-white transition-colors no-underline flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">event_available</span> Calendly</a>
<a href="https://linkedin.com/company/zorex-ai" target="_blank" class="font-['Manrope'] text-sm tracking-wide text-slate-300 hover:text-white transition-colors no-underline flex items-center gap-2"><span class="material-symbols-outlined text-[18px]">work</span> LinkedIn</a>
</div>
</div>
<div class="font-['Manrope'] text-sm tracking-wide text-[#E2C08D] text-left md:text-center max-w-xs">
<p class="mb-2">© 2024 Zorex AI Automation Agency.</p>
<p>Precision-engineered growth.</p>
</div>
<div class="flex flex-wrap justify-start md:justify-end gap-x-6 gap-y-4 max-w-md">"""

count = 0
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_footer in content:
        content = content.replace(old_footer, new_footer)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f'Updated {file}')
print(f'Total updated: {count}')
