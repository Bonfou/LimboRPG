import re

def generate_clean_id(title):
    clean_title = title.replace('[', '').replace(']', '').strip()
    safe_id = re.sub(r'[^a-z0-9]+', '-', clean_title.lower()).strip('-')
    return clean_title, safe_id

def define_env(env):
    
    @env.macro
    def move_card(type, title, body, die=None, pwr=None, dmg=None, ep=None, cost=None, h=4):
        type_map = {
            "offensive": "OFF",
            "defensive": "DEF",
            "utility": "UTL",
            "passive": "PAS",
            "trait": "TRT"
        }
        badge_text = type_map.get(type, "")
        badge_html = f'<span class="type-badge {type}">{badge_text}</span>' if badge_text else ""
        
        clean_title, base_id = generate_clean_id(title)
        final_id = f"move-{base_id}"
        
        stats_html = ""
        if die is not None:
            stats_html = f'<div class="move-stats" markdown="1">**:material-dice-6: DIE:** {die} // **:material-lightning-bolt: PWR:** {pwr} // **:fontawesome-solid-burst: DMG:** {dmg} // **:material-poker-chip: EP:** {ep}</div>'
        elif cost is not None:
            stats_html = f'<div class="move-stats" markdown="1">**Cost:** {cost}</div>'
            
        # Dynamically generate the correct number of hashes based on the 'h' parameter
        heading_hashes = '#' * h
            
        return f"""<div class="move-card {type}" markdown="1">

{heading_hashes} {badge_html} {title} {{ #{final_id} data-toc-label="{clean_title}" }}

{stats_html}

{body}

</div>"""

    @env.macro
    def feature_card(title, body):
        clean_title, base_id = generate_clean_id(title)
        final_id = f"feat-{base_id}"
        
        return f"""<div class="move-card feature" markdown="1">

### <span class="type-badge feature">FEA</span> {title} {{ #{final_id} data-toc-label="{clean_title}" }}

{body}

</div>"""