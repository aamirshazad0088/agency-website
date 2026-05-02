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

NOVUS_IMG = "https://lh3.googleusercontent.com/aida-public/AB6AXuDEvrG0vuOmEI9j6X7ucg-rYvKPChuVgZtZsFHWGD8CABiANXWAADEdjB2IHwKKFqCSDBiF6CjbyijiPPFjKEzbPPHjq6kZ-Qh0-A6TDNa0yDWPqxSLyxAJHANbpBpbaIi6oY0A9IT1Du6w-H1MFo50OmMqtZ4jYxOH5qjzgcYdhVNNRWgRu4jA-IIJQPjbKqKpc4qc7VrmvpwFR_RJeAIZA-j60uzSjU2q1Rt5RBoQKv7g0RbNQXbjE4vIOCLeDMDZ6p1lhvO7Cw"

page = head_nav.replace("<title>Zelqar - AI Automation Agency</title>","<title>Case Study: Eliminating Data Bottlenecks at Novus | Zelqar</title>")

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
<span class="font-label-sm text-on-surface-variant uppercase tracking-widest text-xs">Novus Operations</span>
</div>
<h1 class="font-headline-xl text-headline-xl text-primary-container mb-6 leading-tight">Eliminating Data Bottlenecks at Novus</h1>
<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl border-l-4 border-secondary pl-6">Turning 40 hours of weekly manual reporting into 5 minutes of automated insight. Discover how Zelqar engineered a custom data pipeline that transformed operational confidence across the entire organization.</p>
</div>
</section>

<!-- Challenge & Paradigm Shift -->
<section class="py-24 bg-surface-container-low border-y border-outline-variant/30 relative">
<div class="max-w-[1280px] mx-auto px-6 relative z-10">
<div class="text-center max-w-2xl mx-auto mb-16">
<h2 class="font-headline-md text-headline-md text-primary-container mb-4">The Challenge & Paradigm Shift</h2>
<p class="font-body-md text-on-surface-variant">Novus Operations was hemorrhaging productivity. Their operations team spent entire workweeks manually aggregating data from disconnected systems, resulting in delayed decisions and unreliable metrics.</p>
</div>
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
<div class="bg-surface-container-lowest p-10 rounded-xl border border-outline-variant/30 shadow-sm relative overflow-hidden group hover:border-outline transition-colors">
<div class="absolute top-0 left-0 w-1 h-full bg-error/80"></div>
<div class="flex justify-between items-start mb-6">
<div class="w-12 h-12 bg-error-container text-on-error-container rounded-lg flex items-center justify-center">
<span class="material-symbols-outlined">hourglass_bottom</span>
</div>
<span class="font-label-sm text-error bg-error-container px-3 py-1 rounded-full text-xs">Manual Process</span>
</div>
<h3 class="font-headline-md text-2xl text-primary-container mb-4">Data Chaos & Decision Lag</h3>
<ul class="space-y-4 font-body-md text-on-surface-variant">
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> 40+ hours per week spent manually aggregating spreadsheet data.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Siloed systems creating contradictory reports across departments.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Critical business decisions delayed by days due to data verification.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-error text-lg mt-0.5">close</span> Error-prone manual entry causing cascading inaccuracies in forecasting.</li>
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
<h3 class="font-headline-md text-2xl text-primary-container mb-4">Autonomous Data Intelligence</h3>
<ul class="space-y-4 font-body-md text-on-surface-variant">
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Real-time data aggregation from all connected platforms.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Unified dashboards providing single-source-of-truth reporting.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Instant anomaly detection flagging data inconsistencies automatically.</li>
<li class="flex items-start gap-3"><span class="material-symbols-outlined text-primary text-lg mt-0.5">check</span> Automated forecasting models with 98% verified accuracy.</li>
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
<p class="font-body-md text-on-surface-variant">A systematic three-phase approach ensured zero disruption to ongoing operations while fundamentally rebuilding the data infrastructure from the ground up.</p>
</div>
<div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
<div class="hidden md:block absolute top-1/2 left-0 w-full h-[1px] bg-outline-variant/50 -z-10"></div>
<div class="bg-surface-container-lowest p-8 rounded-xl border border-outline-variant/30 shadow-sm text-center relative">
<div class="w-16 h-16 bg-background border-4 border-surface-container-lowest rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm absolute -top-8 left-1/2 -translate-x-1/2 text-primary-container font-headline-md">1</div>
<div class="w-12 h-12 bg-secondary-container/30 text-secondary rounded-full flex items-center justify-center mx-auto mb-4 mt-4">
<span class="material-symbols-outlined">search</span>
</div>
<h3 class="font-headline-md text-xl text-primary-container mb-3">Systems Audit</h3>
<p class="font-body-md text-sm text-on-surface-variant">Deep-dive analysis of all existing data sources, spreadsheet workflows, and system integrations to map the complete data topology.</p>
</div>
<div class="bg-surface-container-lowest p-8 rounded-xl border border-outline-variant/30 shadow-sm text-center relative">
<div class="w-16 h-16 bg-background border-4 border-surface-container-lowest rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm absolute -top-8 left-1/2 -translate-x-1/2 text-primary-container font-headline-md">2</div>
<div class="w-12 h-12 bg-secondary-container/30 text-secondary rounded-full flex items-center justify-center mx-auto mb-4 mt-4">
<span class="material-symbols-outlined">api</span>
</div>
<h3 class="font-headline-md text-xl text-primary-container mb-3">Pipeline Engineering</h3>
<p class="font-body-md text-sm text-on-surface-variant">Custom API connectors built to bridge disparate platforms, creating a unified data lake with automated ETL pipelines running 24/7.</p>
</div>
<div class="bg-surface-container-lowest p-8 rounded-xl border border-outline-variant/30 shadow-sm text-center relative">
<div class="w-16 h-16 bg-background border-4 border-surface-container-lowest rounded-full flex items-center justify-center mx-auto mb-6 shadow-sm absolute -top-8 left-1/2 -translate-x-1/2 text-primary-container font-headline-md">3</div>
<div class="w-12 h-12 bg-secondary-container/30 text-secondary rounded-full flex items-center justify-center mx-auto mb-4 mt-4">
<span class="material-symbols-outlined">dashboard</span>
</div>
<h3 class="font-headline-md text-xl text-primary-container mb-3">Dashboard Deployment</h3>
<p class="font-body-md text-sm text-on-surface-variant">Interactive real-time dashboards replacing static spreadsheets, with automated alerts and scheduled executive summary reports.</p>
</div>
</div>
</section>

<!-- The Solution Detail -->
<section class="py-24 px-6 max-w-[1280px] mx-auto bg-surface-container-low rounded-3xl mb-24 border border-outline-variant/20 shadow-inner">
<div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
<div class="p-8 lg:p-12">
<h2 class="font-headline-md text-headline-md text-primary-container mb-6">The Automated Reporting Engine</h2>
<p class="font-body-md text-body-md text-on-surface-variant mb-8">We engineered a custom API-driven reporting infrastructure that seamlessly integrates Novus's core platforms. This wasn't a simple dashboard overlay; it was a complete reconstruction of their data architecture.</p>
<ul class="space-y-6">
<li class="flex items-start gap-4 bg-surface-container-lowest p-4 rounded-lg border border-outline-variant/20 shadow-sm">
<div class="w-10 h-10 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-sm">hub</span>
</div>
<div>
<strong class="font-body-md text-primary-container block mb-1">Unified API Integration Layer</strong>
<span class="text-sm text-on-surface-variant">Custom connectors bridging CRM, ERP, and financial systems into a single coherent data stream.</span>
</div>
</li>
<li class="flex items-start gap-4 bg-surface-container-lowest p-4 rounded-lg border border-outline-variant/20 shadow-sm">
<div class="w-10 h-10 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-sm">monitoring</span>
</div>
<div>
<strong class="font-body-md text-primary-container block mb-1">Real-Time KPI Dashboards</strong>
<span class="text-sm text-on-surface-variant">Interactive visualizations replacing static spreadsheets with instant, drill-down metric exploration.</span>
</div>
</li>
<li class="flex items-start gap-4 bg-surface-container-lowest p-4 rounded-lg border border-outline-variant/20 shadow-sm">
<div class="w-10 h-10 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center shrink-0">
<span class="material-symbols-outlined text-sm">notifications_active</span>
</div>
<div>
<strong class="font-body-md text-primary-container block mb-1">Automated Anomaly Alerts</strong>
<span class="text-sm text-on-surface-variant">Intelligent threshold monitoring that flags data discrepancies before they cascade into reporting errors.</span>
</div>
</li>
</ul>
</div>
<div class="relative h-full min-h-[500px] rounded-r-3xl overflow-hidden shadow-2xl border-l border-outline-variant/30">
"""
page += f'<img alt="Novus data dashboard" class="absolute inset-0 w-full h-full object-cover" src="{NOVUS_IMG}"/>'
page += r"""
<div class="absolute inset-0 bg-gradient-to-t from-primary/80 to-transparent mix-blend-multiply pointer-events-none"></div>
</div>
</div>
</section>

<!-- Results -->
<section class="py-24 bg-primary text-on-primary relative overflow-hidden">
<div class="max-w-[1280px] mx-auto px-6 text-center relative z-10">
<h2 class="font-headline-md text-headline-md mb-4 text-white">Measurable Impact</h2>
<p class="font-body-md text-primary-fixed-dim max-w-2xl mx-auto mb-16">Enterprise-grade data automation delivering concrete ROI within the first month of deployment.</p>
<div class="grid grid-cols-1 md:grid-cols-3 gap-8">
<div class="bg-primary-container/80 backdrop-blur-sm p-10 rounded-xl border border-secondary-container/30 relative overflow-hidden group">
<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-6xl text-secondary-container">verified</span>
</div>
<div class="font-headline-xl text-headline-xl text-secondary-container mb-2">98%</div>
<div class="font-body-lg text-body-lg text-on-primary mb-4 font-semibold">Data Accuracy</div>
<div class="h-2 w-full bg-primary/50 rounded-full overflow-hidden"><div class="h-full bg-secondary-container w-[98%] rounded-full"></div></div>
<p class="text-sm text-primary-fixed-dim mt-4 text-left">From error-prone manual entry to verified, automated data pipelines with built-in validation.</p>
</div>
<div class="bg-primary-container/80 backdrop-blur-sm p-10 rounded-xl border border-secondary-container/30 relative overflow-hidden group">
<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-6xl text-secondary-container">schedule</span>
</div>
<div class="font-headline-xl text-headline-xl text-secondary-container mb-2">40 hrs</div>
<div class="font-body-lg text-body-lg text-on-primary mb-4 font-semibold">Saved Per Week</div>
<div class="h-2 w-full bg-primary/50 rounded-full overflow-hidden"><div class="h-full bg-secondary-container w-[90%] rounded-full"></div></div>
<p class="text-sm text-primary-fixed-dim mt-4 text-left">Entire workweeks reclaimed from manual data aggregation and cross-referencing tasks.</p>
</div>
<div class="bg-primary-container/80 backdrop-blur-sm p-10 rounded-xl border border-secondary-container/30 relative overflow-hidden group">
<div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
<span class="material-symbols-outlined text-6xl text-secondary-container">speed</span>
</div>
<div class="font-headline-xl text-headline-xl text-secondary-container mb-2">5 min</div>
<div class="font-body-lg text-body-lg text-on-primary mb-4 font-semibold">Report Generation</div>
<div class="h-2 w-full bg-primary/50 rounded-full overflow-hidden"><div class="h-full bg-secondary-container w-[95%] rounded-full"></div></div>
<p class="text-sm text-primary-fixed-dim mt-4 text-left">From 40 hours of manual compilation to 5-minute automated executive summaries.</p>
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
"Zelqar didn't just speed up our reporting; they entirely rebuilt our operational confidence. We now trust our numbers instantly. The team went from drowning in spreadsheets to making strategic decisions in real time."
</blockquote>
<div class="flex items-center justify-center gap-4">
<div class="w-12 h-12 bg-primary-container text-on-primary-container rounded-full flex items-center justify-center font-bold">AM</div>
<div class="text-left">
<div class="font-label-sm text-label-sm text-primary-container uppercase tracking-widest font-bold">Aisha M.</div>
<div class="text-sm text-on-surface-variant">Operations Director, Novus Operations</div>
</div>
</div>
</div>
</section>
</main>
"""

page += footer
write("case-study-novus.html", page)
print("Novus rebuilt!")
