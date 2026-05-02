import os, re
DIR = r"d:\agency website"
def read(n):
    with open(os.path.join(DIR,n),encoding="utf-8") as f: return f.read()
def write(n,c):
    with open(os.path.join(DIR,n),"w",encoding="utf-8") as f: f.write(c)
    print("OK",n)

idx = read("index.html")
head_nav = re.search(r"([\s\S]*?</nav>)", idx).group(1)
footer = re.search(r"(<footer[\s\S]*?</html>)", idx).group(1)

ECHO_IMG = "https://lh3.googleusercontent.com/aida-public/AB6AXuB5J4qZnVhqxg38Q1-SjkBhvn4nCaEwTfAVcDF1HiRt2ByggvUvSbCrxl4xa-I5fan8Toi8uJelaFMcIMpoMLJlJ4pESweGeKciv0csPg6VCChKtPNpWqZ9khiNx4l1fLOKpHgqCPoxyxZMueNwyXtU4c_y2XrZTICn2hTGKX56v9UpcNoq6CrexrzYwLtMT2uT2uBBeQdbdzHBERpRJ0FCNtf-ClYhry0OACeqNBVhm-sQLgGx588tXtx3jg80hJGdd1dUzHZbnQ"
ECHO_HEAD = "https://lh3.googleusercontent.com/aida-public/AB6AXuCS0_JIuCu1hk2stRtmTWamEtZVgURlgQl-iZZqLjDG-YFO63wwp0MxGzQUt7M1PH0mGN3q-SAMdTbSXeTlRZr4j5heVnyFgVIsgDf6otNUUkRCe91xWdRrBs212nBb9WC_PpaKdoaizdDvmgib8MRatrbpYVVii-5PNp51HNStm7rvhZiTrhZdcm0HoFZ9x5EtIKLn9Xrqcvi5RikyatJjV076uexEPntOHKNBBjo5_grZTJdiwSbvRHUykNfaTUNR0r53ecZgkw"

page = head_nav.replace("<title>Zelqar - AI Automation Agency</title>","<title>Case Study: How EchoCommerce Scaled Support with AI | Zelqar</title>")

page += r"""
<main class="pt-20">
<!-- Hero -->
<section class="py-24 lg:py-32 px-6 max-w-[1280px] mx-auto relative">
<div class="absolute top-20 right-20 w-64 h-64 bg-secondary-container/20 rounded-full blur-3xl z-[-1]"></div>
<div class="absolute bottom-10 left-10 w-96 h-96 bg-primary-container/5 rounded-full blur-3xl z-[-1]"></div>
<div class="max-w-4xl">
<div class="flex items-center gap-3 mb-4">
<span class="inline-flex items-center gap-1 bg-secondary-container text-on-secondary-container px-4 py-1.5 rounded-full font-label-sm text-xs border border-secondary/20">
<span class="material-symbols-outlined text-[14px]">analytics</span> Case Study
</span>
<span class="font-label-sm text-on-surface-variant uppercase tracking-widest text-xs">EchoCommerce</span>
</div>
<h1 class="font-headline-xl text-headline-xl text-primary-container mb-6 leading-tight">How EchoCommerce Scaled Support with AI</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl border-l-4 border-secondary pl-6">From 24-hour response times to 3 minutes. A strategic deployment of autonomous AI agents that transformed customer support into a competitive advantage while cutting costs by 60%.</p>
</div>
</section>

<!-- Challenge & Paradigm Shift -->
<section class="py-24 bg-surface-container-low border-y border-outline-variant/30 relative">
<div class="max-w-[1280px] mx-auto px-6 relative z-10">
<div class="text-center max-w-2xl mx-auto mb-16">
<h2 class="font-headline-md text-headline-md text-primary-container mb-4">The Challenge & Paradigm Shift</h2>
<p class="font-body-md text-on-surface-variant">Rapid growth meant ticket volumes scaled linearly with sales, creating an unsustainable operational bottleneck. EchoCommerce was at a crossroads: hire an army of support staff or find a technological lever.</p>
</div>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
<div class="bg-surface-container-lowest p-10 rounded-xl border border-outline-variant/30 shadow-sm relative overflow-hidden group hover:border-outline transition-colors">
<div class="absolute top-0 left-0 w-1 h-full bg-error/80"></div>
<div class="flex justify-between items-start mb-6">
<div class="w-12 h-12 bg-error-container text-on-error-container rounded-lg flex items-center justify-center">
<span class="material-symbols-outlined">warning</span>
</div>
<span class="font-label-sm text-error bg-error-container px-3 py-1 rounded-full text-xs">Manual Process</span>
</div>
<h3 class="font-headline-md text-2xl text-primary-container mb-4">Support Overload & Customer Churn</h3>
<ul class="space-y-4 font-body-md text-on-surface-variant">
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Average 24-hour response time driving customer dissatisfaction.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Linear scaling: every revenue jump required proportional staff hiring.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Human agents overwhelmed by repetitive Tier-1 and Tier-2 queries.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Siloed data forcing manual lookups across CRM, ERP, and order systems.</li>
</ul>
</div>
<div class="bg-surface-container-lowest p-10 rounded-xl border border-outline-variant/30 shadow-sm relative overflow-hidden group hover:border-outline transition-colors">
<div class="absolute top-0 left-0 w-1 h-full bg-primary/80"></div>
<div class="flex justify-between items-start mb-6">
<div class="w-12 h-12 bg-primary-container text-on-primary-container rounded-lg flex items-center justify-center">
<span class="material-symbols-outlined">memory</span>
</div>
<span class="font-label-sm text-primary-container bg-primary-fixed px-3 py-1 rounded-full text-xs">AI-Driven Process</span>
</div>
<h3 class="font-headline-md text-2xl text-primary-container mb-4">Autonomous Support Intelligence</h3>
<ul class="space-y-4 font-body-md text-on-surface-variant">
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Instant 3-minute average resolution via custom-trained LLM agents.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Non-linear scaling: handle 10x volume without proportional headcount.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> 60% of all tickets resolved autonomously with zero human intervention.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Parallel API-driven data retrieval across all connected systems.</li>
</ul>
</div>
</div>
</div>
</section>

<!-- Strategic Implementation -->
<section class="py-24 px-6 max-w-[1280px] mx-auto">
<div class="text-center max-w-2xl mx-auto mb-16">
<span class="text-secondary font-label-sm tracking-widest uppercase block mb-2 text-xs">Methodology</span>
<h2 class="font-headline-md text-headline-md text-primary-container mb-4">Strategic Implementation</h2>
<p class="font-body-md text-on-surface-variant">A phased deployment ensured zero disruption to live customer support operations while building the AI infrastructure underneath.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
<div class="hidden md:block absolute top-1/2 left-0 w-full h-[1px] bg-outline-variant/50 -z-10"></div>
<div class="bg-surface-container-lowest p-8 rounded-xl border border-outline-variant/30 shadow-sm text-center relative">
<div class="w-16 h-16 bg-background border-4 border-surface-container-lowest rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm absolute -top-8 left-1/2 -translate-x-1/2 text-primary-container font-headline-md">1</div>
<div class="w-12 h-12 bg-secondary-container/30 text-secondary rounded-full flex items-center justify-center mx-auto mb-4 mt-4">
<span class="material-symbols-outlined">support_agent</span>
</div>
<h3 class="font-headline-md text-xl text-primary-container mb-3">Ticket Analysis</h3>
<p class="font-body-md text-sm text-on-surface-variant">Comprehensive audit of 50,000+ historical support tickets to identify patterns, common queries, and edge-case scenarios for model training.</p>
</div>
<div class="bg-surface-container-lowest p-8 rounded-xl border border-outline-variant/30 shadow-sm text-center relative">
<div class="w-16 h-16 bg-background border-4 border-surface-container-lowest rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm absolute -top-8 left-1/2 -translate-x-1/2 text-primary-container font-headline-md">2</div>
<div class="w-12 h-12 bg-secondary-container/30 text-secondary rounded-full flex items-center justify-center mx-auto mb-4 mt-4">
<span class="material-symbols-outlined">model_training</span>
</div>
<h3 class="font-headline-md text-xl text-primary-container mb-3">LLM Fine-Tuning</h3>
<p class="font-body-md text-sm text-on-surface-variant">Custom training of domain-specific language models on EchoCommerce's product catalog, policies, and brand voice for accurate, on-brand responses.</p>
</div>
<div class="bg-surface-container-lowest p-8 rounded-xl border border-outline-variant/30 shadow-sm text-center relative">
<div class="w-16 h-16 bg-background border-4 border-surface-container-lowest rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm absolute -top-8 left-1/2 -translate-x-1/2 text-primary-container font-headline-md">3</div>
<div class="w-12 h-12 bg-secondary-container/30 text-secondary rounded-full flex items-center justify-center mx-auto mb-4 mt-4">
<span class="material-symbols-outlined">rocket_launch</span>
</div>
<h3 class="font-headline-md text-xl text-primary-container mb-3">Progressive Rollout</h3>
<p class="font-body-md text-sm text-on-surface-variant">Shadow mode testing followed by gradual traffic routing, from 10% to full autonomous resolution, with human-in-the-loop quality gates.</p>
</div>
</div>
</section>

<!-- The Solution Detail -->
<section class="py-24 px-6 max-w-[1280px] mx-auto bg-surface-container-low rounded-3xl mb-24 border border-outline-variant/20 shadow-inner">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
<div class="p-8 lg:p-12">
<h2 class="font-headline-md text-headline-md text-primary-container mb-6">The Autonomous Support Engine</h2>
<p class="font-body-md text-body-md text-on-surface-variant mb-8">We deployed a sophisticated architecture of custom-trained LLM agents designed specifically for e-commerce edge cases. This wasn't a chatbot; it was an autonomous resolution system with deep operational integration.</p>
<ul class="space-y-6">
<li class="flex items-start gap-4 bg-surface-container-lowest p-4 rounded-lg border border-outline-variant/20 shadow-sm">
<div class="w-10 h-10 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-sm">psychology</span>
</div>
<div>
<strong class="font-body-md text-primary-container block mb-1">Custom-Trained LLM Agents</strong>
<span class="text-sm text-on-surface-variant">Domain-specific models trained on product catalogs, return policies, and historical ticket resolutions for contextual accuracy.</span>
</div>
</li>
<li class="flex items-start gap-4 bg-surface-container-lowest p-4 rounded-lg border border-outline-variant/20 shadow-sm">
<div class="w-10 h-10 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-sm">route</span>
</div>
<div>
<strong class="font-body-md text-primary-container block mb-1">Intelligent Ticket Routing</strong>
<span class="text-sm text-on-surface-variant">Semantic classification engine that instantly categorizes tickets and routes complex edge cases to specialized human agents.</span>
</div>
</li>
<li class="flex items-start gap-4 bg-surface-container-lowest p-4 rounded-lg border border-outline-variant/20 shadow-sm">
<div class="w-10 h-10 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-sm">integration_instructions</span>
</div>
<div>
<strong class="font-body-md text-primary-container block mb-1">Seamless ERP Integration</strong>
<span class="text-sm text-on-surface-variant">Direct API connections to inventory, order management, and logistics systems for real-time data retrieval during ticket resolution.</span>
</div>
</li>
</ul>
</div>
<div class="relative h-full min-h-[500px] rounded-r-3xl overflow-hidden shadow-2xl border-l border-outline-variant/30">
"""
page += f'<img alt="EchoCommerce AI support dashboard" class="absolute inset-0 w-full h-full object-cover" src="{ECHO_IMG}"/>'
page += r"""
<div class="absolute inset-0 bg-gradient-to-t from-primary/80 to-transparent mix-blend-multiply pointer-events-none"></div>
</div>
</div>
</section>

<!-- Results -->
<section class="py-24 bg-primary text-on-primary relative overflow-hidden">
<div class="max-w-[1280px] mx-auto px-6 text-center relative z-10">
<h2 class="font-headline-md text-headline-md mb-4 text-white">Measurable Impact</h2>
<p class="font-body-md text-primary-fixed-dim max-w-2xl mx-auto mb-16">Operational efficiency achieved without compromising customer satisfaction. ROI realized within the first quarter.</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
<div class="bg-primary-container/80 backdrop-blur-sm p-10 rounded-xl border border-secondary-container/30 relative overflow-hidden group">
<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-6xl text-secondary-container">trending_down</span>
</div>
<div class="font-headline-xl text-headline-xl text-secondary-container mb-2">60%</div>
<div class="font-body-lg text-body-lg text-on-primary mb-4 font-semibold">Cost Reduction</div>
<div class="h-2 w-full bg-primary/50 rounded-full overflow-hidden"><div class="h-full bg-secondary-container w-[60%] rounded-full"></div></div>
<p class="text-sm text-primary-fixed-dim mt-4 text-left">Automating high-volume Tier-1 and Tier-2 queries drastically reduced operational expenditure.</p>
</div>
<div class="bg-primary-container/80 backdrop-blur-sm p-10 rounded-xl border border-secondary-container/30 relative overflow-hidden group">
<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-6xl text-secondary-container">star</span>
</div>
<div class="font-headline-xl text-headline-xl text-secondary-container mb-2">95%</div>
<div class="font-body-lg text-body-lg text-on-primary mb-4 font-semibold">CSAT Score</div>
<div class="h-2 w-full bg-primary/50 rounded-full overflow-hidden"><div class="h-full bg-secondary-container w-[95%] rounded-full"></div></div>
<p class="text-sm text-primary-fixed-dim mt-4 text-left">Instant resolutions and zero hold times resulted in friction-free customer experiences.</p>
</div>
<div class="bg-primary-container/80 backdrop-blur-sm p-10 rounded-xl border border-secondary-container/30 relative overflow-hidden group">
<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-6xl text-secondary-container">speed</span>
</div>
<div class="font-headline-xl text-headline-xl text-secondary-container mb-2">3 min</div>
<div class="font-body-lg text-body-lg text-on-primary mb-4 font-semibold">Avg Resolution</div>
<div class="h-2 w-full bg-primary/50 rounded-full overflow-hidden"><div class="h-full bg-secondary-container w-[88%] rounded-full"></div></div>
<p class="text-sm text-primary-fixed-dim mt-4 text-left">Down from 24 hours to 3 minutes average resolution time across all ticket types.</p>
</div>
</div>
</div>
</section>

<!-- Testimonial -->
<section class="py-24 px-6 max-w-4xl mx-auto text-center relative">
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-full h-full max-w-3xl border border-outline-variant/20 rounded-3xl -z-10"></div>
<div class="bg-surface-container-lowest p-12 rounded-3xl shadow-sm border border-outline-variant/10">
<span class="material-symbols-outlined text-5xl text-secondary/40 mb-6 block">format_quote</span>
<blockquote class="font-headline-md text-3xl text-primary-container leading-relaxed mb-10 italic">
"Implementing the Zelqar solution completely transformed our operational capability. We scaled our revenue without scaling our headcount, while actually improving the customer experience. It's like hiring a team of experts that never sleep."
</blockquote>
<div class="flex items-center justify-center gap-4">
"""
page += f'<div class="w-16 h-16 rounded-full overflow-hidden border-2 border-secondary-fixed"><img alt="David L." class="w-full h-full object-cover" src="{ECHO_HEAD}"/></div>'
page += r"""
<div class="text-left">
<div class="font-label-sm text-label-sm text-primary-container uppercase tracking-widest font-bold">David L.</div>
<div class="text-sm text-on-surface-variant">Founder, EchoCommerce</div>
</div>
</div>
</div>
</section>
</main>
"""

page += footer
write("case-study-echocommerce.html", page)
print("EchoCommerce rebuilt!")
