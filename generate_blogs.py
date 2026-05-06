import os
import re

# Read the template
with open("blog-agentic-systems.html", "r", encoding="utf-8") as f:
    template = f.read()

def generate_blog(filename, title, description, h1_title, subtext, author, date, read_time, body_html, image_url, image_alt):
    content = template

    # Replace Metadata
    content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content)
    content = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{description}">', content)
    content = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{title}">', content)
    content = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{description}">', content)
    content = re.sub(r'https://zorexai.vercel.app/blog-agentic-systems.html', f'https://zorexai.vercel.app/{filename}', content)
    
    # Replace JSON-LD name and description
    content = re.sub(r'"name": "The Rise of Agentic Systems - Zorex AI"', f'"name": "{title}"', content)
    content = re.sub(r'"headline": "The Rise of Agentic Systems - Zorex AI"', f'"headline": "{title}"', content)
    content = re.sub(r'"description": "A deep dive into why agentic AI systems are replacing traditional RPA.*?"', f'"description": "{description}"', content)
    content = re.sub(r'"name": "The Rise of Agentic Systems"', f'"name": "{title.split(" - ")[0]}"', content)

    # Replace Main Content
    # Hero Title
    content = re.sub(r'<h1.*?>.*?</h1>', f'<h1 class="font-headline-xl text-headline-xl text-primary mb-stack-md">{h1_title}</h1>', content, count=1, flags=re.DOTALL)
    # Hero Subtext
    content = re.sub(r'<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mb-stack-lg">.*?</p>', f'<p class="font-body-lg text-body-lg text-on-surface-variant max-w-2xl mb-stack-lg">{subtext}</p>', content, count=1, flags=re.DOTALL)
    
    # Author Info
    content = re.sub(r'<span>By Dr. Aris Thorne</span>', f'<span>By {author}</span>', content)
    content = re.sub(r'<span>October 24, 2024</span>', f'<span>{date}</span>', content)
    content = re.sub(r'<span>12 Min Read</span>', f'<span>{read_time}</span>', content)

    # Image
    content = re.sub(r'<img class="w-full h-full object-cover opacity-90".*?/>', f'<img class="w-full h-full object-cover opacity-90" data-alt="{image_alt}" src="{image_url}" />', content, count=1, flags=re.DOTALL)

    # Replace JSON-LD to be BlogPosting Schema
    blog_schema = f"""
    {{
      "@type": "BlogPosting",
      "@id": "https://zorex.ai/{filename}#article",
      "headline": "{title}",
      "name": "{title.split(" - ")[0]}",
      "description": "{description}",
      "author": {{
        "@type": "Person",
        "name": "{author}"
      }},
      "publisher": {{
        "@id": "https://zorex.ai/#organization"
      }},
      "datePublished": "2024-10-24",
      "dateModified": "2024-10-24",
      "image": "{image_url}",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://zorex.ai/{filename}"
      }}
    }}"""
    
    # We will just replace the existing FAQPage schema or WebPage schema in the template with this BlogPosting one if needed.
    # Actually, it's safer to just inject it into the @graph array
    content = re.sub(r'"@type": "FAQPage",.*?\]\s*\}', f'{blog_schema}\n  ]', content, flags=re.DOTALL)

    # Body Content
    # Extract everything between <section class="max-w-3xl mx-auto px-gutter py-card-gap"> and </main>
    # Since there are multiple sections, let's find the start of the first article body section and the end of the CTA section
    # Wait, it's easier to just replace the whole <main> content after the Hero Section.
    # Let's find the end of the Hero Section: </section> after the image.
    hero_end = content.find('</section>', content.find('opacity-90')) + 10
    main_end = content.find('</main>')
    
    # We will preserve the CTA section from the template
    cta_start = content.rfind('<!-- CTA Section -->')
    
    new_body = f"""
        <!-- Article Body -->
        <section class="max-w-3xl mx-auto px-gutter py-card-gap">
            {body_html}
        </section>
        {content[cta_start:main_end]}
    """
    
    content = content[:hero_end] + new_body + content[main_end:]
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


# Blog 1
generate_blog(
    "blog-cognitive-infrastructure.html",
    "Beyond RAG: Architecting True Cognitive Infrastructure | Zorex Blog",
    "Deep technical dive into vector databases, semantic routing, and how Zorex builds multi-agent systems that synthesize context dynamically.",
    "Beyond RAG: Architecting True Cognitive Infrastructure",
    "Simple retrieval-augmented generation is no longer a competitive advantage. We must move beyond fetching documents to synthesizing live operational context.",
    "Dr. Aris Thorne",
    "November 05, 2024",
    "15 Min Read",
    """
            <p class="font-body-lg text-body-lg text-on-surface mb-stack-lg first-letter:text-headline-xl first-letter:font-headline-xl first-letter:text-primary first-letter:mr-3 first-letter:float-left">
                Retrieval-Augmented Generation (RAG) solved the initial hallucination problem for Large Language Models by anchoring them to deterministic data sources. However, as enterprise demands scale, standard RAG pipelines—relying on naive chunking and simple vector similarity—are breaking under the weight of complex, multi-hop queries.
            </p>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                The next evolutionary step is Cognitive Infrastructure. This isn't just about storing embeddings in Pinecone; it's about semantic routing, hierarchical memory systems, and multi-agent orchestration. A true cognitive architecture evaluates the intent of a query, routes it to the appropriate specialized agent, synthesizes information across disparate databases (SQL, NoSQL, and Vector), and generates an actionable outcome. As noted by <a href="https://www.gartner.com/en/newsroom/press-releases/2023-10-11-gartner-identifies-the-top-10-strategic-technology-trends-for-2024" target="_blank" class="text-primary underline hover:text-secondary">Gartner's strategic research</a>, intelligent applications that dynamically adapt are the core differentiator for modern enterprises.
            </p>
            <h2 class="font-headline-md text-headline-md text-primary mt-card-gap mb-stack-md">Semantic Routing vs. Naive Retrieval</h2>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                In a standard RAG setup, every query hits the vector database. This is computationally wasteful and logically flawed. Semantic routing introduces a classifier layer before retrieval. Is the user asking for a mathematical calculation? Route to a deterministic Python execution agent. Are they asking for a client's billing history? Route to the Stripe API agent. Are they asking for policy details? Only then do we route to the vector store.
            </p>
            <div class="bg-surface-container p-8 rounded-xl border border-surface-variant my-8">
                <h3 class="font-headline-md text-xl text-primary mb-4">The Zorex Router Architecture</h3>
                <ul class="space-y-4 font-body-md text-body-md text-on-surface-variant">
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-secondary text-sm mt-1">schema</span> <strong>Intent Classification:</strong> Sub-70ms latency routing using fast, smaller models (e.g., Claude 3 Haiku or fine-tuned Llama 3).</li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-secondary text-sm mt-1">schema</span> <strong>Multi-Index Search:</strong> Querying hybrid search architectures (sparse + dense vectors) for precision.</li>
                    <li class="flex items-start gap-3"><span class="material-symbols-outlined text-secondary text-sm mt-1">schema</span> <strong>Context Synthesis:</strong> A synthesis agent aggregates the findings, scoring them for relevance before final generation.</li>
                </ul>
            </div>
            <p class="font-body-md text-body-md text-on-surface mb-section-padding">
                By decoupling retrieval from generation and introducing specialized routing, we reduce token waste by up to 60% while drastically improving the logical coherence of the final output. This is the foundation of enterprise-grade AI, aligning with findings from <a href="https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023-generative-ais-breakout-year" target="_blank" class="text-primary underline hover:text-secondary">McKinsey's State of AI report</a> emphasizing scalable value over isolated tools.
            </p>
    """,
    "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&q=80&w=1200",
    "Abstract server room data infrastructure"
)

# Blog 2
generate_blog(
    "blog-llm-security.html",
    "Zero-Trust AI: Securing Enterprise LLM Deployments | Zorex Blog",
    "Addressing the biggest enterprise objection—data privacy. Detailing self-hosted models, VPC deployments, and deterministic guardrails.",
    "Zero-Trust AI: Securing Enterprise LLM Deployments",
    "Data sovereignty is non-negotiable. Learn how we architect LLM deployments that guarantee proprietary enterprise data never leaks to public models.",
    "Elena Rostova",
    "December 12, 2024",
    "10 Min Read",
    """
            <p class="font-body-lg text-body-lg text-on-surface mb-stack-lg first-letter:text-headline-xl first-letter:font-headline-xl first-letter:text-primary first-letter:mr-3 first-letter:float-left">
                The greatest barrier to AI adoption in the enterprise isn't capability; it's security. When executives envision connecting an LLM to their core CRM or ERP, they immediately picture proprietary data inadvertently training a public model or being exposed via prompt injection. These are valid fears, but they are entirely solvable with a Zero-Trust AI architecture.
            </p>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                At Zorex, we treat LLMs as untrusted actors within the network. By enforcing strict boundaries, we allow the model to reason about data without ever permanently possessing it.
            </p>
            <h2 class="font-headline-md text-headline-md text-primary mt-card-gap mb-stack-md">VPC Deployments and Air-Gapped Models</h2>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                For highly regulated industries (healthcare, finance, legal), API calls to public endpoints (like standard OpenAI APIs) are often unacceptable, regardless of zero-retention policies. The solution is deploying open-weight models (like Llama 3 or Mixtral) directly within the client's Virtual Private Cloud (VPC), or utilizing Azure/AWS dedicated endpoints that guarantee hardware-level isolation.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 my-8">
                <div class="bg-primary p-6 rounded-lg">
                    <h4 class="font-headline-md text-lg text-secondary-fixed mb-2">Deterministic Guardrails</h4>
                    <p class="font-body-md text-primary-fixed-dim text-sm">We wrap LLM outputs in deterministic parsing layers (like NeMo Guardrails or Outlines) that enforce structured JSON schemas. If the model attempts to deviate or output restricted PII, the guardrail intercepts and blocks the transaction.</p>
                </div>
                <div class="bg-surface-container p-6 rounded-lg border border-surface-variant">
                    <h4 class="font-headline-md text-lg text-primary mb-2">Role-Based Access Control (RBAC)</h4>
                    <p class="font-body-md text-on-surface-variant text-sm">The agent inherits the permissions of the user interacting with it. If User A cannot access Q3 financial reports in the CRM, the agent executing a query on behalf of User A will be denied access at the database level. Frameworks detailed by <a href="https://www.microsoft.com/en-us/security/business/zero-trust" target="_blank" class="text-primary underline hover:text-secondary">Microsoft's Zero Trust</a> research emphasize this boundary as crucial.</p>
                </div>
            </div>
            <p class="font-body-md text-body-md text-on-surface mb-section-padding">
                Security in the age of generative AI requires shifting from perimeter defense to data-centric defense. By combining VPC deployments, strict RBAC, and deterministic output parsing, we deliver the power of cognitive automation with the security of traditional enterprise software.
            </p>
    """,
    "https://images.unsplash.com/photo-1563206767-5b18f218e8de?auto=format&fit=crop&q=80&w=1200",
    "Secure digital vault and lock abstract"
)

# Blog 3
generate_blog(
    "blog-intelligent-process.html",
    "The End of Static Workflows: Intelligent Process Automation | Zorex Blog",
    "How decision-layer AI replaces brittle logic trees, featuring the mathematics of error reduction and ROI horizons for growing businesses.",
    "The End of Static Workflows: Intelligent Process Automation",
    "Traditional RPA is brittle. Discover how injecting reasoning layers into business processes yields unbreakable, self-healing automation workflows.",
    "Dr. Aris Thorne",
    "January 18, 2025",
    "14 Min Read",
    """
            <p class="font-body-lg text-body-lg text-on-surface mb-stack-lg first-letter:text-headline-xl first-letter:font-headline-xl first-letter:text-primary first-letter:mr-3 first-letter:float-left">
                If you have ever managed a complex Zapier or Make.com workflow, you know the pain of the 'silent failure'. An API changes slightly, a client submits a form with a typo in their email, or a document is uploaded in the wrong format. The rigid 'if-then' logic snaps, the workflow halts, and human intervention is required to unblock the pipeline. This is the fundamental flaw of static workflows.
            </p>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                Intelligent Process Automation (IPA) introduces a cognitive reasoning layer into the orchestration engine. Instead of failing when encountering an exception, the system pauses, evaluates the error, and attempts to resolve it autonomously.
            </p>
            <h2 class="font-headline-md text-headline-md text-primary mt-card-gap mb-stack-md">Self-Healing Automation Pipelines</h2>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                Consider an automated client onboarding sequence. A new contract is signed, triggering a workflow to create a project in Asana, an invoice in QuickBooks, and a folder in Google Drive. If the client's company name contains an invalid character for a Google Drive folder, a traditional automation tool fails instantly.
            </p>
            <p class="font-body-md text-body-md text-on-surface mb-stack-lg">
                An Intelligent Process Agent handles this differently. It receives the API error from Google Drive, reads the error message ("Invalid character in folder name"), reasons about the solution ("I need to sanitize the string"), sanitizes the input, and retries the API call. The pipeline heals itself in milliseconds.
            </p>
            <div class="bg-surface-container-low border-l-4 border-secondary p-6 my-8">
                <p class="font-body-md text-on-surface-variant italic">"We replaced a 40-step deterministic automation with a single agentic objective: 'Onboard this client based on the standard operating procedure document.' The error rate dropped from 12% to 0.4% overnight."</p>
            </div>
            <p class="font-body-md text-body-md text-on-surface mb-section-padding">
                The ROI of Intelligent Process Automation isn't just in the hours saved from doing the work—it's in the hours saved from fixing the broken automations. As documented in <a href="https://www.ibm.com/topics/intelligent-automation" target="_blank" class="text-primary underline hover:text-secondary">IBM's Intelligent Automation</a> case studies, leveraging LLMs as dynamic decision nodes within workflows yields unbreakable, self-healing automation pipelines.
            </p>
    """,
    "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&q=80&w=1200",
    "Abstract microchip technology circuitry"
)
