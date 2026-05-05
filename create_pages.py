import os

blog_path = r'd:\agency website\blog.html'
with open(blog_path, 'r', encoding='utf-8') as f:
    content = f.read()

head_nav = content.split('<!-- Main Content -->')[0]
footer = content.split('</main>')[1]

privacy_main = """<!-- Main Content -->
<main class="pt-32 pb-24 px-8 max-w-4xl mx-auto flex-grow">
  <div class="bg-surface-container-lowest border border-outline-variant/30 rounded-2xl p-10 md:p-16 shadow-sm">
      <h1 class="font-headline-lg text-primary-container mb-6">Privacy Policy</h1>
      <p class="font-body-md text-on-surface-variant mb-8">Last updated: May 2026</p>
      
      <div class="space-y-8 text-on-surface-variant">
          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">1. Introduction</h2>
              <p>Welcome to Zorex. We respect your privacy and are committed to protecting your personal data. This privacy policy will inform you as to how we look after your personal data when you visit our website and tell you about your privacy rights and how the law protects you.</p>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">2. The Data We Collect About You</h2>
              <p>Personal data, or personal information, means any information about an individual from which that person can be identified. We may collect, use, store and transfer different kinds of personal data about you which we have grouped together follows:</p>
              <ul class="list-disc pl-6 mt-4 space-y-2">
                  <li><strong>Identity Data</strong> includes first name, last name, username or similar identifier.</li>
                  <li><strong>Contact Data</strong> includes billing address, delivery address, email address and telephone numbers.</li>
                  <li><strong>Technical Data</strong> includes internet protocol (IP) address, your login data, browser type and version, time zone setting and location, browser plug-in types and versions, operating system and platform and other technology on the devices you use to access this website.</li>
                  <li><strong>Usage Data</strong> includes information about how you use our website, products and services.</li>
              </ul>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">3. How We Use Your Personal Data</h2>
              <p>We will only use your personal data when the law allows us to. Most commonly, we will use your personal data in the following circumstances:</p>
              <ul class="list-disc pl-6 mt-4 space-y-2">
                  <li>Where we need to perform the contract we are about to enter into or have entered into with you.</li>
                  <li>Where it is necessary for our legitimate interests (or those of a third party) and your interests and fundamental rights do not override those interests.</li>
                  <li>Where we need to comply with a legal or regulatory obligation.</li>
              </ul>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">4. Data Security</h2>
              <p>We have put in place appropriate security measures to prevent your personal data from being accidentally lost, used or accessed in an unauthorised way, altered or disclosed. In addition, we limit access to your personal data to those employees, agents, contractors and other third parties who have a business need to know.</p>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">5. Contact Us</h2>
              <p>If you have any questions about this privacy policy or our privacy practices, please contact us at:</p>
              <p class="mt-4">Email: hello@zorex.com</p>
          </section>
      </div>
  </div>
</main>
"""

terms_main = """<!-- Main Content -->
<main class="pt-32 pb-24 px-8 max-w-4xl mx-auto flex-grow">
  <div class="bg-surface-container-lowest border border-outline-variant/30 rounded-2xl p-10 md:p-16 shadow-sm">
      <h1 class="font-headline-lg text-primary-container mb-6">Terms of Service</h1>
      <p class="font-body-md text-on-surface-variant mb-8">Last updated: May 2026</p>
      
      <div class="space-y-8 text-on-surface-variant">
          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">1. Agreement to Terms</h2>
              <p>By accessing our website and using our services, you agree to be bound by these Terms of Service and all applicable laws and regulations. If you do not agree with any of these terms, you are prohibited from using or accessing this site.</p>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">2. Use License</h2>
              <p>Permission is granted to temporarily download one copy of the materials (information or software) on Zorex's website for personal, non-commercial transitory viewing only. This is the grant of a license, not a transfer of title, and under this license you may not:</p>
              <ul class="list-disc pl-6 mt-4 space-y-2">
                  <li>modify or copy the materials;</li>
                  <li>use the materials for any commercial purpose, or for any public display (commercial or non-commercial);</li>
                  <li>attempt to decompile or reverse engineer any software contained on Zorex's website;</li>
                  <li>remove any copyright or other proprietary notations from the materials; or</li>
                  <li>transfer the materials to another person or "mirror" the materials on any other server.</li>
              </ul>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">3. Disclaimer</h2>
              <p>The materials on Zorex's website are provided on an 'as is' basis. Zorex makes no warranties, expressed or implied, and hereby disclaims and negates all other warranties including, without limitation, implied warranties or conditions of merchantability, fitness for a particular purpose, or non-infringement of intellectual property or other violation of rights.</p>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">4. Limitations</h2>
              <p>In no event shall Zorex or its suppliers be liable for any damages (including, without limitation, damages for loss of data or profit, or due to business interruption) arising out of the use or inability to use the materials on Zorex's website, even if Zorex or a Zorex authorized representative has been notified orally or in writing of the possibility of such damage.</p>
          </section>

          <section>
              <h2 class="font-headline-md text-primary-container mb-4 text-2xl">5. Governing Law</h2>
              <p>These terms and conditions are governed by and construed in accordance with the laws and you irrevocably submit to the exclusive jurisdiction of the courts in that State or location.</p>
          </section>
      </div>
  </div>
</main>
"""

with open(r'd:\agency website\privacy.html', 'w', encoding='utf-8') as f:
    f.write(head_nav.replace('<title>Blog — AI Automation Insights | Zorex</title>', '<title>Privacy Policy | Zorex</title>') + privacy_main + footer)

with open(r'd:\agency website\terms.html', 'w', encoding='utf-8') as f:
    f.write(head_nav.replace('<title>Blog — AI Automation Insights | Zorex</title>', '<title>Terms of Service | Zorex</title>') + terms_main + footer)

print('Successfully created privacy.html and terms.html')
