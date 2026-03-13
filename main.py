def define_env(env):
    
    @env.macro
    def move_card(type, title, body, die=None, pwr=None, dmg=None, ep=None, cost=None):
        stats_html = ""
        
        # Build standard combat stats if 'die' is provided
        if die is not None:
            stats_html = f'<div class="move-stats" markdown="1">**:material-dice-6: DIE:** {die} // **:material-lightning-bolt: PWR:** {pwr} // **:fontawesome-solid-burst: DMG:** {dmg} // **:material-poker-chip: EP:** {ep}</div>\n'
        
        # Build utility stats if 'cost' is provided
        elif cost is not None:
            stats_html = f'<div class="move-stats" markdown="1">**Cost:** {cost}</div>\n'
            
        return f"""
<div class="move-card {type}" markdown="1">
#### {title}
{stats_html}
{body}
</div>
"""

    @env.macro
    def feature_card(title, body):
        return f"""
<div class="move-card feature" markdown="1">
#### {title}

{body}
</div>
"""