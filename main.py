import re

def generate_clean_id(title):
    clean_title = title.replace('[', '').replace(']', '').strip()
    safe_id = re.sub(r'[^a-z0-9]+', '-', clean_title.lower()).strip('-')
    return clean_title, safe_id

def define_env(env):
    
    @env.macro
    def move_card(type, title, body, die=None, pwr=None, dmg=None, ep=None, cost=None, h=4):
        # 1. Map Types to Abbreviations and Icons
        type_map = {
            "offensive": ("OFFENSE", ":material-sword:"),
            "defensive": ("DEFENSE", ":material-shield:"),
            "utility": ("UTILITY", ":material-wrench:"),
            "passive": ("PASSIVE", ":material-puzzle:"),
            "trait": ("TRAIT", ":material-sd:"),
            "feature": ("FEATURE", ":material-cog:")
        }
        
        badge_text, badge_icon = type_map.get(type, ("", ""))
        
        # 2. Generate the Enlarged Type Badge with Icon Included
        badge_html = f'<span class="type-badge {type}" markdown="1">{badge_icon} {badge_text}</span>' if badge_text else ""
        
        # 3. Generate the Cost Pill (Only for moves with actual costs)
        corner_badge_html = ""
        if ep is not None:
            corner_badge_html = f'<span class="corner-cost ep-cost" title="EP Cost" markdown="1">:material-poker-chip: **{ep}**</span>'
        elif cost is not None:
            corner_badge_html = f'<span class="corner-cost fp-cost" title="FP Cost" markdown="1">**{cost}**</span>'
            
        clean_title, base_id = generate_clean_id(title)
        final_id = f"move-{base_id}"
        
        # 4. Generate the Secondary Stats Banner (Flush under header)
        stats_html = ""
        if die is not None:
            stats_html = (
                f'<div class="stats-banner" markdown="1">\n'
                f'<span class="stat-item">**:material-dice-6: DIE:** {die}</span>\n'
                f'<span class="stat-item">**:material-lightning-bolt: PWR:** {pwr}</span>\n'
                f'<span class="stat-item">**:fontawesome-solid-burst: DMG:** {dmg}</span>\n'
                f'</div>'
            )
            
        heading_hashes = '#' * h
            
        # 5. Output: Notice the { .card-header } injected into the Markdown heading
        return f"""<div class="move-card {type}" markdown="1">
{heading_hashes} {badge_html} {title} {corner_badge_html} {{ #{final_id} data-toc-label="{clean_title}" .card-header }}
{stats_html}
<div class="card-body" markdown="1">
{body}
</div>
</div>"""