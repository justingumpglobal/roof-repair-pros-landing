# Roofing Landing Page

Pay-per-call landing page for roofing services.

---

## Project Status: LIVE - READY FOR ELOCAL SUBMISSION

**Brand Name:** Roofing Service Experts
**Domain:** roofing-service-experts.com (LIVE)
**GitHub:** https://github.com/justingumpglobal/roof-repair-pros-landing
**Supabase Project:** rpcoelumfrzvbwnhvmnp
**Phone:** (888) ROOF-PRO → (888) 766-3776 (placeholder in HTML)
**Ringba Campaign ID:** TBD (placeholder `CAMPAIGN_ID_TBD` in HTML line 1228)

**Completed:**
- ✅ Landing page HTML/CSS/JS (index.html, privacy.html, terms.html)
- ✅ Database deployed to Supabase (5 tables, 97 rows, RPC function)
- ✅ Logo generated with "Roofing Service Experts" branding
- ✅ All 17 images generated and optimized
- ✅ Combined Google Ads CSV generated (342 rows, 18 services)
- ✅ Documentation complete
- ✅ GitHub repo created and code pushed
- ✅ Site LIVE at roofing-service-experts.com
- ✅ eLocal compliance changes applied (no insurance, no testimonials, no guarantees)

**Next:**
- ⏳ Submit to eLocal for compliance review
- ⏳ Receive phone number from eLocal
- ⏳ Set up Ringba campaign (route to eLocal number)
- ⏳ Update site with Ringba number and campaign ID
- ⏳ Set up Google Ads account

**Optional (can do after launch):**
- Insurance logos not downloaded (7 providers) - site works without them

---

## Next Steps

### 1. ✅ Deploy Database (COMPLETE)
Database successfully deployed to Supabase (rpcoelumfrzvbwnhvmnp):
- 5 tables created
- 97 rows inserted
- RPC function `get_roofing_content()` verified working

### 2. ✅ Site Live (COMPLETE)
Site deployed and live at roofing-service-experts.com

### 3. Submit to eLocal
- Site is LIVE and COMPLIANT → submit for compliance review now
- Wait for eLocal approval
- eLocal will provide phone number after approval
- Example from Dentist site: (484) 666-3244

### 4. After eLocal Approval
1. **Set up Ringba campaign** - Route calls to eLocal number
2. **Get Ringba tracking number** - Display on site
3. **Update index.html**:
   - Line 1228: Replace `CAMPAIGN_ID_TBD` with real Ringba campaign ID
   - Lines 924, 975, 1189, 1203, 1224, 1240: Replace `(888) ROOF-PRO` with Ringba number
4. **Push changes** - GitHub auto-deploys to Cloudflare Pages

### 5. Google Ads Setup
1. Create Google Ads account under Bryan
2. Upload `ad-exports/combined_upload.csv` (342 rows ready)
3. Before uploading: Replace `[DATE]` with campaign date (e.g., `01/29/26`)
4. Manually add image assets (17 images in `assets/images/`)
5. Set up conversion tracking for phone calls

---

## Quick Reference

**Supabase Project:** rpcoelumfrzvbwnhvmnp

### Run Commands
```bash
# Test locally
python -m http.server 8000

# Push changes (auto-deploys via GitHub after setup)
git add . && git commit -m "message" && git push
```

---

## Database Tables

| Table | Rows | Description |
|-------|------|-------------|
| `roofing_services` | 18 | All service types with slugs, categories, custom content fields |
| `roofing_service_content` | 18 | Short names, common problems (JSONB) per service |
| `roofing_testimonials` | 54 | 3 per service, problem → solution focused |
| `roofing_insurance_providers` | 7 | State Farm, Allstate, USAA, Liberty Mutual, Farmers, Nationwide, Travelers |
| `roofing_value_props` | 4 | Service type → value prop mapping (Fast, Fair, FIXED/INSTALLED/THOROUGH/PROTECTED) |

### RPC Function
- `get_roofing_content(p_service_slug)` - Returns all dynamic content for a service (27+ fields)

---

## Services (18 total)

### Emergency Services (3)
| Slug | Name |
|------|------|
| emergency-roof-repair | Emergency Roof Repair |
| roof-leak-repair | Roof Leak Repair |
| storm-damage-repair | Storm Damage Repair |

### General Repair (4)
| Slug | Name |
|------|------|
| roof-repair | Roof Repair |
| shingle-repair | Shingle Repair |
| flat-roof-repair | Flat Roof Repair |
| metal-roof-repair | Metal Roof Repair |

### Material-Specific Repair (4)
| Slug | Name |
|------|------|
| tile-roof-repair | Tile Roof Repair |
| slate-roof-repair | Slate Roof Repair |
| hail-damage-repair | Hail Damage Repair |
| wind-damage-repair | Wind Damage Repair |

### Replacement Services (4)
| Slug | Name |
|------|------|
| roof-replacement | Roof Replacement |
| shingle-roof-replacement | Shingle Roof Replacement |
| metal-roof-replacement | Metal Roof Replacement |
| tile-roof-replacement | Tile Roof Replacement |

### Inspection & Maintenance (3)
| Slug | Name |
|------|------|
| roof-inspection | Roof Inspection |
| roof-maintenance | Roof Maintenance |
| insurance-roof-inspection | Insurance Roof Inspection |

---

## URL Parameters

| Parameter | Example | Description |
|-----------|---------|-------------|
| `service` | `?service=emergency-roof-repair` | Loads service-specific content |
| `loc_physical_ms` | `?loc_physical_ms=9003499` | Google Ads geo-targeting code |

**Full URL Example:**
```
https://roofrepairpros.com/?service=emergency-roof-repair&loc_physical_ms=9003499
```

---

## Service Type System

Service types map to dynamic value props in "Fast, Fair, [X]" section:

| Service Type | Third Word | Use Cases |
|--------------|------------|-----------|
| repair | FIXED | All repair services (leak, shingle, emergency, etc.) |
| replacement | INSTALLED | New roof installations |
| inspection | THOROUGH | Inspections, assessments |
| maintenance | PROTECTED | Ongoing maintenance plans |

---

## File Structure

```
roofing-today/
├── CLAUDE.md                  # This file
├── index.html                 # Main landing page (HTML/CSS/JS)
├── privacy.html               # Privacy policy
├── terms.html                 # Terms of service
├── current_ad_groups.txt      # Tracking created ad groups
├── ad-exports/
│   └── templates/
│       └── ad-group-template.csv
└── assets/
    └── images/
        ├── logo.png           # Roof Repair Pros logo (TBD)
        ├── final_cta_background.jpg
        ├── hero/              # 6 hero images needed
        ├── process/           # 3 process step images
        ├── services/          # 6 service card images
        └── insurance/         # 7 insurance logos
```

---

## Images Status

### ✅ Logo (Complete)
- `logo.png` - 90KB, navy blue & red, trimmed transparent background
- Location: `assets/images/logo.png`

### ✅ Hero Images (6 - Complete)
All generated and optimized (800x1000px, 147-198KB):
- `hero_emergency.jpg` - 198KB
- `hero_repair.jpg` - 156KB (currently used as default on page)
- `hero_replacement.jpg` - 169KB
- `hero_inspection.jpg` - 148KB
- `hero_shingle.jpg` - 167KB
- `hero_metal.jpg` - 147KB

Location: `assets/images/hero/`

**Note:** Only `hero_repair.jpg` is currently displayed. Other 5 hero images are generated but not dynamically loaded. To enable dynamic hero images per service, would need to:
1. Add `hero_image_filename` field to database
2. Add JavaScript to swap hero image based on service
3. Map each service to appropriate hero image

### ✅ Process Step Images (3 - Complete)
All generated and optimized (600x600px, 57-87KB):
- `call.jpg` - 57KB
- `assess.jpg` - 87KB
- `protected.jpg` - 75KB

Location: `assets/images/process/`

### ✅ Service Card Images (6 - Complete)
All generated and optimized (600x450px, 53-87KB):
- `service_emergency.jpg` - 53KB
- `service_leak.jpg` - 72KB
- `service_shingle.jpg` - 87KB
- `service_replacement.jpg` - 74KB
- `service_inspection.jpg` - 64KB
- `service_maintenance.jpg` - 76KB

Location: `assets/images/services/`

### ✅ Background Image (1 - Complete)
- `final_cta_background.jpg` - 262KB (slightly over 150KB target but acceptable)
- Location: `assets/images/final_cta_background.jpg`

### ❌ Insurance Logos (7 - Not Complete)
Still need to manually download:
- `state-farm.png`, `allstate.png`, `usaa.png`, `liberty-mutual.png`, `farmers.png`, `nationwide.png`, `travelers.png`

Source: [Brandfetch](https://brandfetch.com/) or [WorldVectorLogo](https://worldvectorlogo.com/)
Specs: PNG transparent, 120px height, under 50KB
Note: USAA and Travelers logos are light (set `is_light: true` in database)
Location: `assets/images/insurance/`

**Can launch without insurance logos** - section will simply not display until logos are added.

---

## Roofing-Specific Features

### Insurance Prominence
- Insurance logos grid in hero section (7 providers)
- "We Work With All Major Insurance" messaging
- Insurance-specific sitelinks in Google Ads

### Material Versatility
- Separate services for each roof type (shingle, metal, tile, slate, flat)
- Material-specific common problems and testimonials

### Storm/Seasonal Messaging
- Dynamic badge: "24/7 Emergency Service" for storm services
- Storm damage documentation for insurance claims
- Hail and wind damage specialists

### Inspection Lead Gen
- Free inspections as primary offer
- Insurance inspection services (second opinions)
- Pre-purchase and pre-sale inspections

### Compliance Considerations
- **NEVER say:** "We guarantee insurance approval" or "100% covered by insurance"
- **OK to say:** "We work with all major insurance", "We help with claims documentation", "Free inspections for insurance claims"
- Testimonials can mention insurance help, NOT full coverage claims

---

## Dynamic Content Flow

1. **User lands on page** with `?service=roof-leak-repair&loc_physical_ms=9003499`
2. **JavaScript fetches** location data (Boston) and zip code (for Ringba)
3. **JavaScript calls** `get_roofing_content('roof-leak-repair')`
4. **RPC function returns** 27+ fields including:
   - Hero headline/accent, subheadline, testimonial
   - CTA button text, final CTA headline/subtext
   - Common problems (5 JSONB objects with title/description)
   - 3 service-specific testimonials
   - 7 insurance providers
   - Value prop (FIXED) based on service type (repair)
   - Meta title/description for SEO
5. **JavaScript updates** all `[data-dynamic]` and `[data-location]` elements
6. **Ringba tags** zip code for IVR auto-fill
7. **Page displays** fully customized content for roof leak repair in Boston

---

## Ad Group Creation

**Template:** `ad-exports/templates/ad-group-template.csv`

**CSV Structure (30 columns, 19 rows per service):**
1. Ad 1 - RSA with 4 unpinned headlines/descriptions
2. Ad 2 - RSA with location insertion + pinned headlines
3-9. Sitelinks (7 rows) - Same Day, Insurance, Free Inspections, Licensed, Why Choose Us, Emergency, Replacement
10-17. Callouts (8 rows) - 24/7 Emergency, Same Day, Insurance, Licensed, Free Inspections, 25+ Years, Local, Guaranteed
18. Structured Snippet - Services (6 values)
19. Keyword - Broad match [service name]

**Combined CSV File:**
- ONE CSV file (`combined_upload.csv`) for entire Google Ads account setup
- Contains all 18 services × 19 rows = 342 total rows
- Upload once to set up entire campaign

**Google Ads Character Limits:**
- Headlines: 30 chars max
- Descriptions: 90 chars max
- Sitelinks: 25 chars (text), 35 chars (descriptions)
- Callouts: 25 chars

---

## Deployment Checklist

**Pre-Launch:**
- [x] Landing page HTML/CSS/JS created
- [x] Privacy and terms pages created
- [x] Database schema designed (5 tables, 97 rows)
- [x] Google Ads CSV template created
- [x] Generate/add brand logo (logo.png) - 90KB
- [x] Generate all hero, process, service, background images - 17 images total
- [ ] Download insurance logos (7 providers) - Optional, can launch without
- [ ] Purchase domain (roofrepairpros.com recommended)
- [ ] Acquire phone number (toll-free: 833 or 844 prefix)
- [ ] Create Ringba campaign (get campaign ID)
- [ ] Update index.html line 1228 with real Ringba campaign ID
- [ ] Update index.html lines 924, 975, 1189, 1203, 1224, 1240 with real phone
- [ ] Execute database setup SQL in Supabase
- [ ] Update CLAUDE.md with real domain, phone, Ringba ID
- [ ] Create GitHub repo
- [ ] Connect Cloudflare Pages to GitHub
- [ ] Point DNS records to Cloudflare Pages

**Post-Launch:**
- [ ] Verify Ringba phone swap works on live domain
- [ ] Test all 18 service URLs (e.g., `?service=emergency-roof-repair`)
- [ ] Test location targeting (e.g., `?loc_physical_ms=9003499`)
- [ ] Verify RPC function `get_roofing_content()` returns correct data
- [ ] Mobile test on real devices (iOS Safari, Android Chrome)
- [ ] PageSpeed Insights (target 90+ mobile, 95+ desktop)
- [ ] Generate combined Google Ads CSV (18 services × 19 rows = 342 total rows)
- [ ] Set up Google Ads campaigns (under Bryan per user notes)
- [ ] Upload combined_upload.csv to Google Ads
- [ ] Add image assets in Google Ads (manual step)
- [ ] Monitor first 100 calls for quality
- [ ] eLocal/Inquirly compliance check (if needed)

---

## Known Considerations

### Logo Protocol
When adding insurance logos:
1. Download PNG (not SVG) for auto-trimming
2. Auto-trim whitespace: `magick input.png -trim +repage output.png`
3. Check if logo is white/light - set `is_light = true` in database
4. JavaScript adds `.is-light` class, CSS applies `filter: invert(1)` to flip to dark

### Ringba Deployment
Before deploying:
1. Verify "Number to Replace" in Ringba campaign matches hardcoded phone in HTML
2. Add domain to Ringba whitelist
3. Confirm campaign is active

### Google Ads CSV Exports
If editing existing campaigns:
1. Only read 'Ad Group' and 'Final URL' columns to save context
2. Check if ads have Labels - add if missing for unique identification
3. Change `Labels` header to `Labels#Original` for unique identifier on re-import

---

## Copy Rules (MUST FOLLOW)

### Never Say
- **No warranty claims** - Never mention specific warranty durations unless backed by written contract

### Always Do
- **Insurance language accuracy** - Never guarantee coverage, only say we "work with" or "help with claims"
- **Subheadlines must convey urgency** - Use "today" language where appropriate
- **Testimonials stay natural** - Problem → solution format, emotional, avoid technical jargon

---

## Recent Changes

### 2026-01-29 (Evening)
- **Images generated:** All 17 images created using Gemini API
  - Logo: 90KB (trimmed, transparent background)
  - Hero images (6): 147-198KB each (under 200KB target)
  - Process images (3): 57-87KB each (under 100KB target)
  - Service images (6): 53-87KB each (under 80KB target)
  - Background: 262KB (slightly over 150KB target but acceptable)
- **CSV documentation updated:** Clarified that projects use ONE combined CSV (not separate CSVs per ad group)
- **Status:** Images complete, ready for domain/Ringba/database setup

### 2026-01-29 (Afternoon)
- **Project created:** Complete roofing landing page implementation
- Database schema (5 tables, 97 rows) created in `.claude/plans/roofing-database-setup.sql`
- Landing page HTML/CSS/JS complete in `index.html`
- Privacy and terms pages created
- CSV template created for Google Ads
- Project documentation (this file) complete
