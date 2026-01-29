#!/usr/bin/env python3
"""
Generate combined Google Ads CSV for all roofing services.
18 services × 19 rows = 342 total rows
"""

import csv
from typing import List, Dict

DOMAIN = "roofing-service-experts.com"
CAMPAIGN = f"{DOMAIN} | [DATE]"

# Service definitions
SERVICES = [
    # Emergency (3)
    {
        "slug": "emergency-roof-repair",
        "name": "Emergency Roof Repair",
        "short_name": "Emergency Repair",
        "headlines": [
            "24/7 Emergency Roof Repair",
            "Storm Damage? Call Now",
            "Same Day Emergency Service",
            "Fast Emergency Repairs"
        ],
        "descriptions": [
            "Emergency Roof Repairs 24/7. Storm Damage, Leaks, Tarps. Licensed & Insured. Call Now!",
            "Roof Emergency? We're Available Now. Fast Response. Professional Roofers. Same Day Service!",
            "Don't Wait - Call Now For Emergency Roof Repair. 24/7 Service. Licensed Professionals!",
            "Storm Damage? Leaking Roof? We're Here 24/7. Fast Emergency Repairs. Call Today!"
        ],
        "snippet_values": ["Emergency Repairs", "Storm Damage", "Leak Repair", "Tarp Installation", "24/7 Service", "Insurance Claims"]
    },
    {
        "slug": "roof-leak-repair",
        "name": "Roof Leak Repair",
        "short_name": "Leak Repair",
        "headlines": [
            "Roof Leak Repair Near You",
            "Stop Roof Leaks Today",
            "Same Day Leak Repair",
            "Fix Leaking Roof Fast"
        ],
        "descriptions": [
            "Stop Roof Leaks Today. Fast Leak Detection & Repair. Licensed & Insured. Free Inspections!",
            "Leaking Roof? We'll Fix It Today. Same Day Service. Professional Roofers. Call Now!",
            "Roof Leak Repair Experts. Fast Response. Quality Materials. Get Your Roof Fixed Today!",
            "Don't Let Leaks Cause Damage. Professional Leak Repair. Same Day Service. Call Now!"
        ],
        "snippet_values": ["Leak Detection", "Leak Repair", "Water Damage Prevention", "Same Day Service", "Free Inspections", "All Roof Types"]
    },
    {
        "slug": "storm-damage-repair",
        "name": "Storm Damage Repair",
        "short_name": "Storm Damage",
        "headlines": [
            "Storm Damage Roof Repair",
            "Post-Storm Roof Repairs",
            "Insurance Claims Help",
            "Fast Storm Damage Repairs"
        ],
        "descriptions": [
            "Storm Damage Roof Repair. Insurance Claims Assistance. Fast Response. Licensed Roofers!",
            "Roof Damaged By Storm? We'll Help With Your Insurance Claim. Fast Repairs. Call Now!",
            "Post-Storm Roof Repairs. We Document Everything For Your Insurance. Call Today!",
            "Storm Damage? We Work With Your Insurance. Fast Repairs. Professional Service!"
        ],
        "snippet_values": ["Storm Damage", "Insurance Claims", "Emergency Repairs", "Tarp Installation", "Documentation", "All Repairs"]
    },
    # Inspection (2)
    {
        "slug": "roof-inspection",
        "name": "Roof Inspection",
        "short_name": "Roof Inspection",
        "headlines": [
            "Professional Roof Inspection",
            "Free Roof Inspection",
            "Thorough Roof Assessment",
            "Expert Roof Inspection"
        ],
        "descriptions": [
            "Professional Roof Inspection. Free Assessment. Licensed Inspectors. Know Your Roof's Condition!",
            "Free Roof Inspection & Assessment. We Check Everything. Detailed Report. Call Today!",
            "Get A Thorough Roof Inspection. Identify Problems Early. Free Inspection. Call Now!",
            "Expert Roof Inspections. Complete Assessment. Licensed Professionals. Schedule Today!"
        ],
        "snippet_values": ["Roof Inspection", "Free Assessment", "Detailed Report", "All Roof Types", "Licensed Inspectors", "Photo Documentation"]
    },
    {
        "slug": "insurance-roof-inspection",
        "name": "Insurance Roof Inspection",
        "short_name": "Insurance Inspection",
        "headlines": [
            "Insurance Roof Inspection",
            "Claim Inspection Services",
            "Pre-Claim Roof Assessment",
            "Insurance Documentation"
        ],
        "descriptions": [
            "Insurance Roof Inspection. We Document Everything For Your Claim. Professional Service!",
            "Need A Roof Inspection For Insurance? We'll Document All Damage. Call Today!",
            "Pre-Claim Roof Inspection. Thorough Documentation. Work With All Insurers. Call Now!",
            "Insurance Roof Assessment. Complete Documentation. Help With Claims Process!"
        ],
        "snippet_values": ["Insurance Inspections", "Claim Documentation", "Photo Evidence", "Detailed Reports", "All Insurers", "Professional Service"]
    },
    # Maintenance (1)
    {
        "slug": "roof-maintenance",
        "name": "Roof Maintenance",
        "short_name": "Maintenance",
        "headlines": [
            "Roof Maintenance Services",
            "Extend Your Roof's Life",
            "Preventive Roof Care",
            "Annual Roof Maintenance"
        ],
        "descriptions": [
            "Roof Maintenance Services. Extend Your Roof's Life. Prevent Costly Repairs. Call Today!",
            "Regular Roof Maintenance Saves Money. Professional Service. Licensed Roofers. Schedule Now!",
            "Keep Your Roof In Top Shape. Maintenance Plans Available. Prevent Problems. Call Today!",
            "Professional Roof Maintenance. Inspections, Cleaning, Minor Repairs. Protect Your Investment!"
        ],
        "snippet_values": ["Roof Maintenance", "Inspections", "Cleaning", "Minor Repairs", "Preventive Care", "Maintenance Plans"]
    },
    # Repair - General (8)
    {
        "slug": "roof-repair",
        "name": "Roof Repair",
        "short_name": "Roof Repair",
        "headlines": [
            "Professional Roof Repair",
            "Same Day Roof Repair",
            "Fix Your Roof Today",
            "Expert Roof Repairs"
        ],
        "descriptions": [
            "Professional Roof Repair. Same Day Service. All Roof Types. Licensed & Insured. Call Now!",
            "Need Roof Repair? We'll Fix It Today. Quality Materials. Experienced Roofers. Call Now!",
            "Fast Roof Repairs. All Materials. Licensed Professionals. Free Inspections. Call Today!",
            "Expert Roof Repairs. Same Day Service. Quality Workmanship. Get Your Roof Fixed Today!"
        ],
        "snippet_values": ["Roof Repair", "Leak Repair", "Shingle Replacement", "Flashing Repair", "All Materials", "Same Day Service"]
    },
    {
        "slug": "shingle-repair",
        "name": "Shingle Repair",
        "short_name": "Shingle Repair",
        "headlines": [
            "Shingle Roof Repair",
            "Replace Missing Shingles",
            "Asphalt Shingle Repair",
            "Fast Shingle Replacement"
        ],
        "descriptions": [
            "Shingle Roof Repair. Missing Or Damaged Shingles? We'll Fix It Today. Call Now!",
            "Asphalt Shingle Repair & Replacement. Same Day Service. Licensed Roofers. Call Today!",
            "Missing Shingles? Don't Wait. Professional Repairs. Quality Materials. Call Now!",
            "Fast Shingle Repair. 3-Tab & Architectural. Same Day Service. Get It Fixed Today!"
        ],
        "snippet_values": ["Shingle Repair", "Shingle Replacement", "3-Tab Shingles", "Architectural Shingles", "Wind Damage", "Storm Damage"]
    },
    {
        "slug": "flat-roof-repair",
        "name": "Flat Roof Repair",
        "short_name": "Flat Roof",
        "headlines": [
            "Flat Roof Repair Experts",
            "Commercial Flat Roof Repair",
            "TPO & EPDM Roof Repair",
            "Flat Roof Leak Repair"
        ],
        "descriptions": [
            "Flat Roof Repair Specialists. TPO, EPDM, Modified Bitumen. Licensed Roofers. Call Now!",
            "Commercial Flat Roof Repair. Stop Leaks. Membrane Repairs. Professional Service!",
            "Flat Roof Leaking? We'll Fix It Today. All Flat Roof Systems. Call Now!",
            "Expert Flat Roof Repairs. Ponding Water, Leaks, Membrane Damage. Call Today!"
        ],
        "snippet_values": ["Flat Roof Repair", "TPO Repair", "EPDM Repair", "Membrane Repair", "Commercial Roofs", "Leak Repair"]
    },
    {
        "slug": "metal-roof-repair",
        "name": "Metal Roof Repair",
        "short_name": "Metal Roof",
        "headlines": [
            "Metal Roof Repair Experts",
            "Standing Seam Repair",
            "Metal Roof Leak Repair",
            "Rust & Panel Repair"
        ],
        "descriptions": [
            "Metal Roof Repair Specialists. Leaks, Rust, Panels, Fasteners. Licensed Roofers!",
            "Metal Roof Leaking? We'll Fix It. Standing Seam, Corrugated, All Types. Call Now!",
            "Expert Metal Roof Repairs. Panel Replacement, Rust Treatment, Leak Repair. Call Today!",
            "Professional Metal Roof Repair. Fasteners, Seams, Panels. Quality Work. Call Now!"
        ],
        "snippet_values": ["Metal Roof Repair", "Panel Replacement", "Rust Repair", "Leak Repair", "Standing Seam", "Fastener Repair"]
    },
    {
        "slug": "tile-roof-repair",
        "name": "Tile Roof Repair",
        "short_name": "Tile Roof",
        "headlines": [
            "Tile Roof Repair Experts",
            "Clay & Concrete Tile Repair",
            "Cracked Tile Replacement",
            "Tile Roof Restoration"
        ],
        "descriptions": [
            "Tile Roof Repair Specialists. Clay, Concrete, Spanish Tile. Licensed Roofers. Call Now!",
            "Cracked Or Broken Tiles? We'll Replace Them. Professional Service. Call Today!",
            "Expert Tile Roof Repairs. Matching Tiles. Quality Installation. Call Now!",
            "Tile Roof Leaking? Cracked Tiles? We'll Fix It. All Tile Types. Call Today!"
        ],
        "snippet_values": ["Tile Roof Repair", "Clay Tile", "Concrete Tile", "Spanish Tile", "Tile Replacement", "Leak Repair"]
    },
    {
        "slug": "slate-roof-repair",
        "name": "Slate Roof Repair",
        "short_name": "Slate Roof",
        "headlines": [
            "Slate Roof Repair Experts",
            "Natural Slate Restoration",
            "Cracked Slate Replacement",
            "Historic Slate Roof Repair"
        ],
        "descriptions": [
            "Slate Roof Repair Specialists. Natural Slate. Matching Replacement. Licensed Roofers!",
            "Cracked Or Missing Slate? We'll Replace It. Quality Matching. Call Today!",
            "Expert Slate Roof Repairs. Historic Homes. Proper Techniques. Call Now!",
            "Professional Slate Roof Repair. Natural Stone. Quality Workmanship. Call Today!"
        ],
        "snippet_values": ["Slate Roof Repair", "Natural Slate", "Historic Roofs", "Slate Replacement", "Leak Repair", "Restoration"]
    },
    {
        "slug": "hail-damage-repair",
        "name": "Hail Damage Repair",
        "short_name": "Hail Damage",
        "headlines": [
            "Hail Damage Roof Repair",
            "Insurance Claim Help",
            "Post-Hail Roof Repair",
            "Hail Damage Assessment"
        ],
        "descriptions": [
            "Hail Damage Roof Repair. Insurance Claims Assistance. Free Inspection. Call Now!",
            "Roof Damaged By Hail? We'll Help With Your Insurance Claim. Fast Repairs!",
            "Hail Damage Assessment & Repair. Work With All Insurers. Licensed Roofers!",
            "Post-Hail Roof Repairs. Complete Documentation. Insurance Help. Call Today!"
        ],
        "snippet_values": ["Hail Damage", "Insurance Claims", "Free Inspection", "Documentation", "All Roof Types", "Fast Repairs"]
    },
    {
        "slug": "wind-damage-repair",
        "name": "Wind Damage Repair",
        "short_name": "Wind Damage",
        "headlines": [
            "Wind Damage Roof Repair",
            "Storm Wind Damage Repair",
            "Missing Shingles? Call Us",
            "Fast Wind Damage Repairs"
        ],
        "descriptions": [
            "Wind Damage Roof Repair. Missing Shingles, Lifted Materials. Fast Service. Call Now!",
            "Roof Damaged By Wind? We'll Fix It Today. Insurance Claims Help. Call Now!",
            "Wind Damage Repairs. Shingles, Flashing, All Materials. Same Day Service!",
            "Storm Wind Damage? We'll Repair Your Roof Fast. Insurance Help. Call Today!"
        ],
        "snippet_values": ["Wind Damage", "Shingle Replacement", "Insurance Claims", "Emergency Repairs", "All Roof Types", "Fast Service"]
    },
    # Replacement (4)
    {
        "slug": "roof-replacement",
        "name": "Roof Replacement",
        "short_name": "Replacement",
        "headlines": [
            "New Roof Replacement",
            "Full Roof Replacement",
            "Replace Your Old Roof",
            "Professional Roof Install"
        ],
        "descriptions": [
            "New Roof Replacement. All Materials Available. Licensed & Insured. Free Estimates!",
            "Time For A New Roof? Quality Materials. Expert Installation. Call For Free Estimate!",
            "Professional Roof Replacement. Asphalt, Metal, Tile, All Types. Call Today!",
            "Full Roof Replacement. Quality Work. Licensed Roofers. Get Your Free Estimate!"
        ],
        "snippet_values": ["Roof Replacement", "New Roofs", "All Materials", "Asphalt Shingles", "Metal Roofs", "Free Estimates"]
    },
    {
        "slug": "shingle-roof-replacement",
        "name": "Shingle Roof Replacement",
        "short_name": "Shingle Replacement",
        "headlines": [
            "New Shingle Roof Install",
            "Asphalt Shingle Replacement",
            "3-Tab & Architectural",
            "Shingle Roof Installation"
        ],
        "descriptions": [
            "New Shingle Roof Installation. 3-Tab & Architectural. Licensed Roofers. Free Estimates!",
            "Asphalt Shingle Roof Replacement. Quality Materials. Expert Install. Call Today!",
            "New Shingle Roof. All Colors & Styles Available. Professional Install. Call Now!",
            "Shingle Roof Replacement. GAF, Owens Corning, CertainTeed. Free Estimates!"
        ],
        "snippet_values": ["Shingle Replacement", "Asphalt Shingles", "3-Tab", "Architectural", "All Colors", "Free Estimates"]
    },
    {
        "slug": "metal-roof-replacement",
        "name": "Metal Roof Replacement",
        "short_name": "Metal Replacement",
        "headlines": [
            "New Metal Roof Install",
            "Standing Seam Metal Roof",
            "Metal Roof Replacement",
            "Durable Metal Roofing"
        ],
        "descriptions": [
            "Metal Roof Replacement. Standing Seam, Corrugated, All Types. Free Estimates!",
            "New Metal Roof Installation. Long-Lasting, Energy Efficient. Licensed Roofers!",
            "Install A Durable Metal Roof. 30+ Year Lifespan. All Colors. Call For Estimate!",
            "Metal Roofing Experts. Standing Seam, R-Panel, All Styles. Free Estimates!"
        ],
        "snippet_values": ["Metal Roofs", "Standing Seam", "Corrugated", "Energy Efficient", "Long-Lasting", "Free Estimates"]
    },
    {
        "slug": "tile-roof-replacement",
        "name": "Tile Roof Replacement",
        "short_name": "Tile Replacement",
        "headlines": [
            "New Tile Roof Install",
            "Clay & Concrete Tile Roofs",
            "Spanish Tile Roofing",
            "Tile Roof Replacement"
        ],
        "descriptions": [
            "Tile Roof Replacement. Clay, Concrete, Spanish Tile. Licensed Roofers. Free Estimates!",
            "New Tile Roof Installation. Beautiful & Long-Lasting. All Styles. Call Today!",
            "Install A Clay Or Concrete Tile Roof. Expert Installation. Free Estimates!",
            "Tile Roofing Experts. Spanish, Mission, All Styles. Quality Install. Call Now!"
        ],
        "snippet_values": ["Tile Roofs", "Clay Tile", "Concrete Tile", "Spanish Tile", "Long-Lasting", "Free Estimates"]
    }
]

# Standard sitelinks (same for all)
SITELINKS = [
    {
        "url_suffix": "&sl=1",
        "text": "Same Day Service",
        "desc1": "Fast Response Times",
        "desc2": "We Come To You Today"
    },
    {
        "url_suffix": "&sl=2",
        "text": "Insurance Billing",
        "desc1": "We Work With Insurance",
        "desc2": "Claims Help Included"
    },
    {
        "url_suffix": "&sl=3",
        "text": "Free Inspections",
        "desc1": "No-Cost Roof Inspection",
        "desc2": "Get Expert Assessment"
    },
    {
        "url_suffix": "&sl=4",
        "text": "Licensed & Insured",
        "desc1": "Professional Roofers",
        "desc2": "Quality Workmanship"
    },
    {
        "url_suffix": "&sl=5",
        "text": "Why Choose Us",
        "desc1": "25+ Years Experience",
        "desc2": "Local Roofing Experts"
    },
    {
        "url_suffix": "&sl=6",
        "text": "Emergency Repairs",
        "desc1": "24/7 Emergency Service",
        "desc2": "Storm Damage Response"
    },
    {
        "url_suffix": "&sl=7",
        "text": "Roof Replacement",
        "desc1": "New Roof Installation",
        "desc2": "All Materials Available"
    }
]

# Standard callouts
CALLOUTS = [
    "24/7 Emergency",
    "Same Day Service",
    "Insurance Billing",
    "Licensed & Insured",
    "Free Inspections",
    "25+ Years Experience",
    "Local Experts",
    "Professional Service"
]


def generate_csv():
    """Generate the combined CSV for all services."""

    rows = []

    # Add header
    header = [
        "Campaign", "Ad Group", "Ad type", "Labels",
        "Headline 1", "Headline 1 position",
        "Headline 2", "Headline 2 position",
        "Headline 3", "Headline 3 position",
        "Headline 4", "Headline 4 position",
        "Description 1", "Description 1 position",
        "Description 2", "Description 2 position",
        "Description 3", "Description 3 position",
        "Description 4", "Description 4 position",
        "Path 1", "Path 2", "Final URL",
        "Link Text", "Description Line 1", "Description Line 2",
        "Callout text", "Header", "Snippet Values", "Keyword"
    ]
    rows.append(header)

    for service in SERVICES:
        ad_group = service["name"]
        slug = service["slug"]
        base_url = f"http://{DOMAIN}/?service={slug}"

        # Row 1: RSA Ad 1 (no label)
        rows.append([
            CAMPAIGN, ad_group, "Responsive search ad", "",
            service["headlines"][0], "-",
            service["headlines"][1], "-",
            service["headlines"][2], "-",
            service["headlines"][3], "-",
            service["descriptions"][0], "-",
            service["descriptions"][1], "-",
            service["descriptions"][2], "-",
            service["descriptions"][3], "-",
            "", "", base_url,
            "", "", "", "", "", "", ""
        ])

        # Row 2: RSA Ad 2 (with location insertion and pinned headlines)
        rows.append([
            CAMPAIGN, ad_group, "Responsive search ad", "Ad 2",
            f"{{LOCATION(City):Local}} {service['short_name']}", "1",
            "Call Now - Same Day Service", "2",
            service["headlines"][2], "-",
            service["headlines"][3], "-",
            service["descriptions"][0], "-",
            service["descriptions"][1], "-",
            service["descriptions"][2], "-",
            service["descriptions"][3], "-",
            "", "", base_url,
            "", "", "", "", "", "", ""
        ])

        # Rows 3-9: Sitelinks
        for sitelink in SITELINKS:
            rows.append([
                CAMPAIGN, ad_group, "", "",
                "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "",
                "", "", base_url + sitelink["url_suffix"],
                sitelink["text"], sitelink["desc1"], sitelink["desc2"],
                "", "", "", ""
            ])

        # Rows 10-17: Callouts
        for callout in CALLOUTS:
            rows.append([
                CAMPAIGN, ad_group, "", "",
                "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "", "",
                "", "", "", "", "", "",
                callout, "", "", ""
            ])

        # Row 18: Structured snippet
        snippet_str = "\n".join(service["snippet_values"])
        rows.append([
            CAMPAIGN, ad_group, "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "Services", snippet_str, ""
        ])

        # Row 19: Keyword
        keyword = service["name"].lower()
        rows.append([
            CAMPAIGN, ad_group, "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "",
            "", "", "", "", "", "", "", "", "", keyword
        ])

    return rows


def main():
    """Write the CSV file."""
    rows = generate_csv()

    output_file = "/Users/justingacina/CLAUDE CODE/Projects/Landing Page Designer/roofing-today/ad-exports/combined_upload.csv"

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"✅ Generated {len(rows)} rows (including header)")
    print(f"   18 services × 19 rows = {len(rows) - 1} data rows")
    print(f"   Saved to: combined_upload.csv")


if __name__ == "__main__":
    main()
