import re

def define_env(env):
    @env.macro
    def move_card(type, title, body, die=None, pwr=None, dmg=None, ep=None, cost=None):
        # Map types to 3-letter badges
        type_map = {
            "offensive": "OFF",
            "defensive": "DEF",
            "utility": "UTL",
            "passive": "PAS"
        }
        badge_text = type_map.get(type, "")
        badge_html = f'<span class="type-badge {type}">{badge_text}</span>' if badge_text else ""
        
        # Create a unique, URL-safe ID for the Move
        clean_title = title.replace('[', '').replace(']', '')
        safe_id = re.sub(r'[^a-z0-9]+', '-', clean_title.lower()).strip('-')
        
        stats_html = ""
        if die is not None:
            stats_html = f'<div class="move-stats" markdown="1">**:material-dice-6: DIE:** {die} // **:material-lightning-bolt: PWR:** {pwr} // **:fontawesome-solid-burst: DMG:** {dmg} // **:material-poker-chip: EP:** {ep}</div>'
        elif cost is not None:
            stats_html = f'<div class="move-stats" markdown="1">**Cost:** {cost}</div>'
            
        return f"""<div class="move-card {type}" markdown="1">

#### {badge_html} {title} {{ #{safe_id} data-toc-label="{clean_title}" }}

{stats_html}

{body}

</div>"""

    @env.macro
    def feature_card(title, body):
        clean_title = title.replace('[', '').replace(']', '')
        safe_id = re.sub(r'[^a-z0-9]+', '-', clean_title.lower()).strip('-')
        
        return f"""<div class="move-card feature" markdown="1">

### <span class="type-badge feature">FEA</span> {title} {{ #{safe_id} data-toc-label="{clean_title}" }}

{body}

</div>"""