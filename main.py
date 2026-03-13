def define_env(env):
    
    # Standard Move Card (For Offensive, Defensive, Utility, Passive)
    @env.macro
    def move_card(type, title, stats, body):
        return f"""
<div class="move-card {type}" markdown="1">
#### {title}
{stats}

{body}
</div>
"""

    # Dedicated Feature Card (For Core Class Features & Weapon Shell Features)
    @env.macro
    def feature_card(title, body):
        return f"""
<div class="move-card feature" markdown="1">
### {title}

{body}
</div>
"""