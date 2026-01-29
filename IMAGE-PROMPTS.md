# AI Image Generation Prompts for Roofing Landing Page

Use these prompts with AI image generators (Midjourney, DALL-E, Stable Diffusion, Gemini).

---

## Hero Images (6 needed)

### hero_emergency.jpg
**Prompt:** "Professional roofer in safety gear on residential roof with blue tarp covering storm damage, emergency repair equipment visible, urgent but controlled atmosphere, professional photography, natural lighting, 4:5 portrait aspect ratio"

**Key Elements:** Emergency tarp, storm damage visible, professional roofer, ladder, safety equipment

---

### hero_repair.jpg
**Prompt:** "Professional roofer fixing asphalt shingles on residential roof, wearing safety harness and hard hat, close-up detailed work with roofing tools, professional photography, sunny day, 4:5 portrait aspect ratio"

**Key Elements:** Roofer working, visible shingles, professional tools, safety gear, quality craftsmanship

---

### hero_replacement.jpg
**Prompt:** "Professional roofing crew installing new shingle roof on suburban house, team of 3-4 workers, organized workspace with materials stacked neatly, modern residential home, professional photography, clear blue sky, 4:5 portrait aspect ratio"

**Key Elements:** Multiple workers, new shingles, organized job site, professional installation

---

### hero_inspection.jpg
**Prompt:** "Professional roof inspector on residential roof with digital tablet or clipboard documenting roof condition, professional attire, measuring tools visible, detailed inspection process, professional photography, 4:5 portrait aspect ratio"

**Key Elements:** Inspector with tablet/clipboard, measurement tools, professional documentation, thorough assessment

---

### hero_shingle.jpg
**Prompt:** "Close-up of professional roofer's hands installing architectural asphalt shingles, nail gun or hammer visible, detailed craftsmanship, new shingles in sharp focus, professional photography, natural lighting, 4:5 portrait aspect ratio"

**Key Elements:** Hands working, shingles in detail, roofing tools, precision work

---

### hero_metal.jpg
**Prompt:** "Professional roofer installing standing seam metal roofing panels, modern metal roof system, professional tools and fasteners visible, clean lines, professional photography, 4:5 portrait aspect ratio"

**Key Elements:** Metal panels, specialized tools, modern roofing system, professional installation

---

## Process Step Images (3 needed)

### call.jpg
**Prompt:** "Professional roofer or office staff member answering phone call with friendly smile, customer service setting or job site, professional and welcoming atmosphere, professional photography, 1:1 square aspect ratio"

**Key Elements:** Phone communication, friendly professional, trust and reliability

---

### assess.jpg
**Prompt:** "Professional roofer on residential roof taking measurements and notes, inspection tools visible, thorough assessment in progress, professional photography, clear day, 1:1 square aspect ratio"

**Key Elements:** Roof inspection, measuring tape, clipboard/tablet, detailed assessment

---

### protected.jpg
**Prompt:** "Beautiful completed residential roof with professional roofer and happy homeowner shaking hands in foreground, perfect finished roof visible, satisfaction and pride evident, professional photography, sunny day, 1:1 square aspect ratio"

**Key Elements:** Completed work, handshake, satisfied customer, quality result

---

## Service Card Images (6 needed)

### service_emergency.jpg
**Prompt:** "Emergency roof repair in progress, roofer securing blue tarp on damaged roof, storm damage visible, urgent professional response, professional photography, 16:10 landscape aspect ratio"

---

### service_leak.jpg
**Prompt:** "Roof leak detection and repair, roofer examining shingles around potential leak point, diagnostic tools visible, professional problem-solving, professional photography, 16:10 landscape aspect ratio"

---

### service_shingle.jpg
**Prompt:** "Close-up of damaged and new shingles side by side, roofer replacing worn shingles, color matching visible, professional repair work, professional photography, 16:10 landscape aspect ratio"

---

### service_replacement.jpg
**Prompt:** "New roof installation in progress, half old roof half new showing transformation, professional crew working, dramatic before/after visible, professional photography, 16:10 landscape aspect ratio"

---

### service_inspection.jpg
**Prompt:** "Roof inspector with drone or inspection equipment examining residential roof, thorough professional assessment, modern inspection technology, professional photography, 16:10 landscape aspect ratio"

---

### service_maintenance.jpg
**Prompt:** "Roofer performing routine maintenance, cleaning gutters or removing debris from roof, preventive care visible, professional upkeep, professional photography, 16:10 landscape aspect ratio"

---

## Background Image (1 needed)

### final_cta_background.jpg
**Prompt:** "Wide shot of professional roofing crew installing beautiful new residential roof, suburban neighborhood, blue sky with few clouds, organized professional operation, inspirational quality work, professional photography, 1920x1080 landscape aspect ratio"

**Key Elements:** Wide establishing shot, professional operation, quality work, aspirational feel

---

## Logo Generation (1 needed)

### logo.png
**Prompt:** "Professional roofing company logo for 'Roof Repair Pros', modern and trustworthy design, incorporating roof/shingle/house silhouette, clean professional font, suitable for web and print, navy blue and red color scheme, transparent background, vector style"

**Alternative Approach:** Use Gemini Nano Banana (see `.claude/logo-generation.md`):
```bash
python generate_logo.py "Roof Repair Pros logo, professional roofing company, roof icon with house silhouette, navy blue and red colors, modern clean design, trustworthy"
```

---

## Image Optimization

After generating images:

1. **Resize to spec:**
```bash
# Hero images to 800x1000
magick input.jpg -resize 800x1000^ -gravity center -extent 800x1000 output.jpg

# Process images to 600x600
magick input.jpg -resize 600x600^ -gravity center -extent 600x600 output.jpg

# Service images to 600x450
magick input.jpg -resize 600x450^ -gravity center -extent 600x450 output.jpg

# Background to 1920x1080
magick input.jpg -resize 1920x1080^ -gravity center -extent 1920x1080 output.jpg
```

2. **Compress for web:**
```bash
# JPG quality 85
magick input.jpg -quality 85 output.jpg

# Or use WebP for better compression
magick input.jpg -quality 85 output.webp
```

3. **Verify file sizes:**
- Hero: under 200KB each
- Process: under 100KB each
- Services: under 80KB each
- Background: under 150KB

---

## Alternative: Stock Photo Sources

If AI generation doesn't work well:
- Unsplash (unsplash.com) - free high-quality photos
- Pexels (pexels.com) - free stock photos
- Shutterstock - paid, high quality, model releases

Search terms:
- "roofer working on roof"
- "roof repair professional"
- "roofing contractor"
- "roof inspection"
- "new roof installation"
