import os, re

DIR = r"d:\agency website"

def read(name):
    with open(os.path.join(DIR, name), encoding="utf-8") as f:
        return f.read()

def write(name, content):
    with open(os.path.join(DIR, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("OK wrote", name)

# ── shared nav/footer from index.html ───────────────────────────────────────
index_html = read("index.html")

def get_head_nav(html):
    m = re.search(r"([\s\S]*?</nav>)", html, re.IGNORECASE)
    return m.group(1)

def get_footer_script(html):
    m = re.search(r"(<footer[\s\S]*?</html>)", html, re.IGNORECASE)
    return m.group(1)

HEAD_NAV = get_head_nav(index_html)
FOOTER   = get_footer_script(index_html)

# ── 1. Build case-studies.html ───────────────────────────────────────────────
CASE_STUDIES_PAGE = (
    HEAD_NAV.replace(
        "<title>Zelqar - AI Automation Agency</title>",
        "<title>Case Studies — Real Results | Zelqar AI Automation</title>"
    )
    + """
<main class="pt-20">

  <!-- Hero -->
  <section class="relative py-24 px-8 bg-surface-bright border-b border-outline-variant/30 overflow-hidden">
    <div class="max-w-[1280px] mx-auto relative z-10 text-center">
      <span class="inline-flex items-center gap-2 px-4 py-2 bg-secondary-fixed text-on-secondary-fixed-variant rounded-full font-label-sm uppercase tracking-widest mb-6 shadow-sm text-xs">
        <span class="material-symbols-outlined text-sm icon-fill">verified</span>
        Client Success Stories
      </span>
      <h1 class="font-headline-xl text-headline-xl text-primary-container max-w-4xl mx-auto mb-6">
        Real Businesses.<br/>
        <span class="text-secondary">Measurable Results.</span>
      </h1>
      <p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mx-auto">
        Every engagement starts with a bottleneck and ends with a system that scales. Explore how we've transformed operations for leading enterprises.
      </p>
    </div>
    <div class="absolute top-1/2 left-0 -translate-y-1/2 -translate-x-1/3 w-[500px] h-[500px] bg-secondary-container/20 rounded-full blur-3xl -z-10"></div>
    <div class="absolute top-0 right-0 -translate-y-1/4 translate-x-1/4 w-[600px] h-[600px] bg-primary-fixed/20 rounded-full blur-3xl -z-10"></div>
  </section>

  <!-- Stats Bar -->
  <section class="py-10 px-8 bg-primary-container border-b border-white/10">
    <div class="max-w-[1280px] mx-auto grid grid-cols-3 gap-8 text-center">
      <div>
        <div class="font-headline-md text-headline-md text-accent-gold">3+</div>
        <div class="font-label-sm text-xs text-on-primary uppercase tracking-widest mt-1">Enterprises Transformed</div>
      </div>
      <div>
        <div class="font-headline-md text-headline-md text-accent-gold">60-98%</div>
        <div class="font-label-sm text-xs text-on-primary uppercase tracking-widest mt-1">Efficiency Gains</div>
      </div>
      <div>
        <div class="font-headline-md text-headline-md text-accent-gold">&lt;30 Days</div>
        <div class="font-label-sm text-xs text-on-primary uppercase tracking-widest mt-1">Average Deployment</div>
      </div>
    </div>
  </section>

  <!-- Case Study Cards -->
  <section class="py-24 px-8 bg-background">
    <div class="max-w-[1280px] mx-auto space-y-12">

      <!-- Card 1: Novus -->
      <a href="case-study-novus.html"
         class="group block no-underline bg-surface-container-lowest border border-outline-variant/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1 md:flex">
        <div class="md:w-2/5 h-64 md:h-auto overflow-hidden relative flex-shrink-0 bg-surface-container">
          <img
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuDEvrG0vuOmEI9j6X7ucg-rYvKPChuVgZtZsFHWGD8CABiANXWAADEdjB2IHwKKFqCSDBiF6CjbyijiPPFjKEzbPPHjq6kZ-Qh0-A6TDNa0yDWPqxSLyxAJHANbpBpbaIi6oY0A9IT1Du6w-H1MFo50OmMqtZ4jYxOH5qjzgcYdhVNNRWgRu4jA-IIJQPjbKqKpc4qc7VrmvpwFR_RJeAIZA-j60uzSjU2q1Rt5RBoQKv7g0RbNQXbjE4vIOCLeDMDZ6p1lhvO7Cw"
            alt="Novus Operations dashboard"
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          <div class="absolute inset-0 bg-gradient-to-r from-transparent to-primary/10"></div>
        </div>
        <div class="p-10 md:p-14 flex flex-col justify-center md:w-3/5">
          <div class="flex flex-wrap items-center gap-3 mb-5">
            <span class="bg-secondary-container text-on-secondary-container font-label-sm text-xs px-3 py-1 rounded-full uppercase tracking-widest">Operations</span>
            <span class="bg-primary-fixed text-primary-container font-label-sm text-xs px-3 py-1 rounded-full uppercase tracking-widest">Data Automation</span>
          </div>
          <h2 class="font-headline-md text-headline-md text-primary-container mb-3 leading-tight group-hover:text-secondary transition-colors duration-300">
            Eliminating Data Bottlenecks at Novus
          </h2>
          <p class="font-body-md text-body-md text-on-surface-variant mb-6">
            Turning 40 hours of manual reporting into 5 minutes of automated insight. We engineered a custom API-driven reporting engine that delivered a 98% improvement in data accuracy.
          </p>
          <div class="flex flex-wrap gap-6 mb-6">
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">98%</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Data Accuracy</div>
            </div>
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">40hrs</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Saved Weekly</div>
            </div>
          </div>
          <div class="flex items-center justify-between border-t border-outline-variant/30 pt-4">
            <div class="flex items-center gap-3 text-xs font-label-sm text-outline uppercase tracking-widest">
              <span>Aisha M., Operations Director</span>
              <span class="w-1 h-1 bg-secondary rounded-full"></span>
              <span>Novus Operations</span>
            </div>
            <span class="inline-flex items-center gap-1 text-secondary font-label-sm text-xs uppercase tracking-wider group-hover:gap-2 transition-all">
              Read Case Study <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </span>
          </div>
        </div>
      </a>

      <!-- Card 2: EchoCommerce -->
      <a href="case-study-echocommerce.html"
         class="group block no-underline bg-surface-container-lowest border border-outline-variant/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1 md:flex md:flex-row-reverse">
        <div class="md:w-2/5 h-64 md:h-auto overflow-hidden relative flex-shrink-0 bg-surface-container">
          <img
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuB5J4qZnVhqxg38Q1-SjkBhvn4nCaEwTfAVcDF1HiRt2ByggvUvSbCrxl4xa-I5fan8Toi8uJelaFMcIMpoMLJlJ4pESweGeKciv0csPg6VCChKtPNpWqZ9khiNx4l1fLOKpHgqCPoxyxZMueNwyXtU4c_y2XrZTICn2hTGKX56v9UpcNoq6CrexrzYwLtMT2uT2uBBeQdbdzHBERpRJ0FCNtf-ClYhry0OACeqNBVhm-sQLgGx588tXtx3jg80hJGdd1dUzHZbnQ"
            alt="EchoCommerce support dashboard"
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          <div class="absolute inset-0 bg-gradient-to-l from-transparent to-primary/10"></div>
        </div>
        <div class="p-10 md:p-14 flex flex-col justify-center md:w-3/5">
          <div class="flex flex-wrap items-center gap-3 mb-5">
            <span class="bg-secondary-container text-on-secondary-container font-label-sm text-xs px-3 py-1 rounded-full uppercase tracking-widest">E-Commerce</span>
            <span class="bg-primary-fixed text-primary-container font-label-sm text-xs px-3 py-1 rounded-full uppercase tracking-widest">AI Support</span>
          </div>
          <h2 class="font-headline-md text-headline-md text-primary-container mb-3 leading-tight group-hover:text-secondary transition-colors duration-300">
            How EchoCommerce Scaled Support with AI
          </h2>
          <p class="font-body-md text-body-md text-on-surface-variant mb-6">
            From 24-hour response times to 3 minutes. Custom-trained LLM agents handle 60% of all tickets flawlessly, reducing support costs by 60% while maintaining a 95% CSAT score.
          </p>
          <div class="flex flex-wrap gap-6 mb-6">
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">60%</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Cost Reduction</div>
            </div>
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">95%</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">CSAT Score</div>
            </div>
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">3 min</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Avg Resolution</div>
            </div>
          </div>
          <div class="flex items-center justify-between border-t border-outline-variant/30 pt-4">
            <div class="flex items-center gap-3 text-xs font-label-sm text-outline uppercase tracking-widest">
              <span>David L., Founder</span>
              <span class="w-1 h-1 bg-secondary rounded-full"></span>
              <span>EchoCommerce</span>
            </div>
            <span class="inline-flex items-center gap-1 text-secondary font-label-sm text-xs uppercase tracking-wider group-hover:gap-2 transition-all">
              Read Case Study <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </span>
          </div>
        </div>
      </a>

      <!-- Card 3: ViralGrowth -->
      <a href="case-study-viralgrowth.html"
         class="group block no-underline bg-surface-container-lowest border border-outline-variant/30 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300 hover:-translate-y-1 md:flex">
        <div class="md:w-2/5 h-64 md:h-auto overflow-hidden relative flex-shrink-0 bg-surface-container">
          <img
            src="https://lh3.googleusercontent.com/aida-public/AB6AXuB97FEcECi24Eg6Hz83mnBNHWGe4Ymi-pBPjY2ljZ1iN3c5TBgU9-7JYDU6lHScmDCozZJ2Dg7M9QhSSxE2QW-aJOxzSS5EYiDrRUEpZyTFAkHtBshWTBtDKuAfhT0ZTb55sTh5LphjfPEAFplr3JjldFoE4u_Hx8zZXSPwRAOEMyZFsw0eTPUa2WAz5OXJtSYiWQyBj9NPpxMtrQJd3LmM2OOp0p-TZltf-urWIxqopP9WOBTdquccO7izymbXRBC1R8wVmNvQUg"
            alt="ViralGrowth AI dashboard"
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"/>
          <div class="absolute inset-0 bg-gradient-to-r from-transparent to-primary/10"></div>
        </div>
        <div class="p-10 md:p-14 flex flex-col justify-center md:w-3/5">
          <div class="flex flex-wrap items-center gap-3 mb-5">
            <span class="bg-secondary-container text-on-secondary-container font-label-sm text-xs px-3 py-1 rounded-full uppercase tracking-widest">Social Media</span>
            <span class="bg-primary-fixed text-primary-container font-label-sm text-xs px-3 py-1 rounded-full uppercase tracking-widest">Content AI</span>
          </div>
          <h2 class="font-headline-md text-headline-md text-primary-container mb-3 leading-tight group-hover:text-secondary transition-colors duration-300">
            How ViralGrowth Automated 90% of Social Content Creation
          </h2>
          <p class="font-body-md text-body-md text-on-surface-variant mb-6">
            From manual posting to a 24/7 autonomous engagement engine. Fine-tuned LLMs and predictive trend analysis drove a 400% increase in monthly reach and an 85% reduction in production costs.
          </p>
          <div class="flex flex-wrap gap-6 mb-6">
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">+400%</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Monthly Reach</div>
            </div>
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">-85%</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Production Cost</div>
            </div>
            <div class="text-center">
              <div class="font-headline-md text-2xl text-primary-container font-bold">2.4M</div>
              <div class="font-label-sm text-xs text-on-surface-variant uppercase tracking-wider">Engagements</div>
            </div>
          </div>
          <div class="flex items-center justify-between border-t border-outline-variant/30 pt-4">
            <div class="flex items-center gap-3 text-xs font-label-sm text-outline uppercase tracking-widest">
              <span>Sarah J., CMO</span>
              <span class="w-1 h-1 bg-secondary rounded-full"></span>
              <span>ViralGrowth</span>
            </div>
            <span class="inline-flex items-center gap-1 text-secondary font-label-sm text-xs uppercase tracking-wider group-hover:gap-2 transition-all">
              Read Case Study <span class="material-symbols-outlined text-sm">arrow_forward</span>
            </span>
          </div>
        </div>
      </a>

    </div>
  </section>

  <!-- CTA -->
  <section class="py-20 px-8 bg-primary-container relative overflow-hidden">
    <div class="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-primary/50 via-primary-container to-primary-container"></div>
    <div class="max-w-[1280px] mx-auto text-center relative z-10">
      <h2 class="font-headline-lg text-headline-lg text-on-primary mb-4">Want results like these?</h2>
      <p class="font-body-lg text-on-primary-container mb-8 max-w-xl mx-auto">Schedule a zero-commitment strategy audit and discover where automation can transform your operations.</p>
      <a href="index.html#book"
         class="inline-flex items-center justify-center px-10 py-4 bg-accent-gold text-primary-container rounded-full font-label-sm uppercase tracking-wider font-bold hover:bg-white transition-colors shadow-lg no-underline">
        Book Strategy Call
        <span class="material-symbols-outlined ml-2 text-sm">arrow_forward</span>
      </a>
    </div>
  </section>

</main>
"""
    + FOOTER
)

write("case-studies.html", CASE_STUDIES_PAGE)

# ── 2. Update ALL html files: nav link + active-tab logic ───────────────────
ALL_FILES = [f for f in os.listdir(DIR) if f.endswith(".html") and f not in ["build_blog.py", "update_blogs.py"]]

OLD_DESKTOP_CS = 'href="index.html#case-studies" data-page="case-studies"'
NEW_DESKTOP_CS = 'href="case-studies.html" data-page="case-studies"'

OLD_MOBILE_CS  = 'href="index.html#case-studies" class="block font'
NEW_MOBILE_CS  = 'href="case-studies.html" class="block font'

OLD_FOOTER_CS  = 'href="index.html#case-studies">Case Studies</a>'
NEW_FOOTER_CS  = 'href="case-studies.html">Case Studies</a>'

OLD_SCRIPT_CS  = "if(d==='case-studies'&&(page.startsWith('case-study')||page==='index.html'))a=true;"
NEW_SCRIPT_CS  = "if(d==='case-studies'&&(page.startsWith('case-study')||page==='case-studies.html'))a=true;"

for fname in ALL_FILES:
    path = os.path.join(DIR, fname)
    with open(path, encoding="utf-8") as f:
        content = f.read()

    changed = False
    for old, new in [
        (OLD_DESKTOP_CS, NEW_DESKTOP_CS),
        (OLD_MOBILE_CS,  NEW_MOBILE_CS),
        (OLD_FOOTER_CS,  NEW_FOOTER_CS),
        (OLD_SCRIPT_CS,  NEW_SCRIPT_CS),
    ]:
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print("  updated nav in", fname)

print("\nDone.")
