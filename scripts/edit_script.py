import os
import re

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
files = [os.path.join(project_root, "index.html")]

for file in files:
    with open(file, 'r') as f:
        content = f.read()

    # 1. Favicon
    if '<link rel="icon"' not in content:
        content = content.replace('<meta property="og:type" content="website">',
                                  '<meta property="og:type" content="website">\n  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>☕</text></svg>">')

    # 2. 15% discount for students, no mint tea
    content = content.replace('15% OFF', '10% OFF')
    content = content.replace('get 15% off your order + a free mint tea on your first visit.', 'get 10% off your order.')
    content = content.replace('<span class="text-2xl font-black">15%</span>', '<span class="text-2xl font-black">10%</span>')
    content = content.replace('for 15% off + free mint tea 🌿', 'for 10% off 🌿')
    content = content.replace('· 15% off + free mint tea 🌿', '· 10% off 🌿')
    content = content.replace('+ free mint tea', '')

    # 3. Instagram is zeezeniasofra
    content = content.replace('instagram.com/zeezeniafarm', 'instagram.com/zeezeniasofra')

    # 4. Mango lasi to $7
    content = content.replace('<p class="font-semibold text-sm text-charcoal-900">Fresh Mango Lassi</p><span class="font-bold text-sm text-olive-800 shrink-0">$6.00</span>',
                              '<p class="font-semibold text-sm text-charcoal-900">Fresh Mango Lassi</p><span class="font-bold text-sm text-olive-800 shrink-0">$7.00</span>')

    # 5. Quality You Can Taste section
    old_quality_header = """<span class="text-xs font-extrabold text-terracotta-300 tracking-[0.22em] uppercase">The Market</span>
        <h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-bold text-white mt-3 leading-tight">Quality You<br>Can Taste.</h2>
        <p class="text-white/50 mt-4 font-light">The trusted Gainesville source for Mediterranean delicacies for over 14 years.</p>"""
    
    new_quality_header = """<span class="text-xs font-extrabold text-terracotta-300 tracking-[0.22em] uppercase">The Farm</span>
        <h2 class="font-serif text-3xl md:text-4xl lg:text-5xl font-bold text-white mt-3 leading-tight">What We Grow &<br>What We Raise</h2>
        <p class="text-white/50 mt-4 font-light">Fresh produce and pasture-raised animals straight from our farm.</p>"""
    
    content = content.replace(old_quality_header, new_quality_header)

    old_grid = """<div class="pillar-card reveal bg-white/8 border border-white/12 rounded-3xl p-8 flex flex-col gap-6">
          <div class="w-14 h-14 rounded-2xl bg-terracotta-500/20 text-terracotta-300 flex items-center justify-center border border-terracotta-500/25">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
          </div>
          <div class="flex-1">
            <h3 class="text-xl font-extrabold text-white mb-3">Fresh Halal Meats</h3>
            <p class="text-sm text-white/60 font-light leading-relaxed">Professional butchery meets Zabiha standards. Pasture-raised and prepared fresh daily for your family meals.</p>
          </div>
          <span class="text-xs font-bold text-terracotta-300 uppercase tracking-widest border-t border-white/10 pt-4">Beef · Lamb · Chicken</span>
        </div>

        <div class="pillar-card reveal reveal-delay-1 bg-white/8 border border-white/12 rounded-3xl p-8 flex flex-col gap-6">
          <div class="w-14 h-14 rounded-2xl bg-terracotta-500/20 text-terracotta-300 flex items-center justify-center border border-terracotta-500/25">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1M4.22 4.22l.707.707m12.02 12.02l.707.707M1 12h2m18 0h2M4.22 19.78l.707-.707M18.95 5.05l.707-.707"/><circle cx="12" cy="12" r="4"/></svg>
          </div>
          <div class="flex-1">
            <h3 class="text-xl font-extrabold text-white mb-3">Bakery &amp; Sweets</h3>
            <p class="text-sm text-white/60 font-light leading-relaxed">Fresh pitas, traditional cookies, and our signature baklawa. Made with pure butter and premium nuts.</p>
          </div>
          <span class="text-xs font-bold text-terracotta-300 uppercase tracking-widest border-t border-white/10 pt-4">Baklawa · Pita · Pastries</span>
        </div>

        <div class="pillar-card reveal reveal-delay-2 bg-white/8 border border-white/12 rounded-3xl p-8 flex flex-col gap-6">
          <div class="w-14 h-14 rounded-2xl bg-terracotta-500/20 text-terracotta-300 flex items-center justify-center border border-terracotta-500/25">
            <svg class="w-7 h-7" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 002 2h2a2.5 2.5 0 002.5-2.5V8a2 2 0 00-2-2h-1.5a2 2 0 01-2-2V2.5"/></svg>
          </div>
          <div class="flex-1">
            <h3 class="text-xl font-extrabold text-white mb-3">Pantry Essentials</h3>
            <p class="text-sm text-white/60 font-light leading-relaxed">From sumac and za'atar to premium olive oils and grains. We source the authentic pantry items you need.</p>
          </div>
          <span class="text-xs font-bold text-terracotta-300 uppercase tracking-widest border-t border-white/10 pt-4">Spices · Oils · Pantry</span>
        </div>"""
    
    new_grid = """<div class="pillar-card reveal bg-white/8 border border-white/12 rounded-3xl p-8 flex flex-col gap-6">
          <div class="w-full h-48 rounded-2xl bg-white/5 flex items-center justify-center border border-white/10 border-dashed">
            <span class="text-white/30 text-sm font-medium">Image Placeholder</span>
          </div>
          <div class="flex-1">
            <h3 class="text-xl font-extrabold text-white mb-3">What We Grow</h3>
            <p class="text-sm text-white/60 font-light leading-relaxed">Fresh produce, organic vegetables, and our signature blueberries straight from the farm.</p>
          </div>
        </div>

        <div class="pillar-card reveal reveal-delay-1 bg-white/8 border border-white/12 rounded-3xl p-8 flex flex-col gap-6">
          <div class="w-full h-48 rounded-2xl bg-white/5 flex items-center justify-center border border-white/10 border-dashed">
            <span class="text-white/30 text-sm font-medium">Image Placeholder</span>
          </div>
          <div class="flex-1">
            <h3 class="text-xl font-extrabold text-white mb-3">What We Raise</h3>
            <p class="text-sm text-white/60 font-light leading-relaxed">Pasture-raised animals cared for with respect and traditional farming methods.</p>
          </div>
        </div>"""
    
    content = content.replace(old_grid, new_grid)

    with open(file, 'w') as f:
        f.write(content)

print("Done")
