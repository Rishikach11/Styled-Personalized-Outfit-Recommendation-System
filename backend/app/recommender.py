
def extract_color(title):
    title = title.lower()
    colors = ['red', 'blue', 'black', 'white', 'green', 'pink', 'yellow']
    for c in colors:
        if c in title:
            return c
    return 'unknown'

def extract_style(title):
    title = title.lower()
    if any(word in title for word in ['formal', 'office', 'oxford', 'derby']):
        return 'formal'
    elif any(word in title for word in ['ethnic', 'traditional', 'jutti', 'mojri']):
        return 'ethnic'
    elif any(word in title for word in ['heels', 'party']):
        return 'party'
    else:
        return 'casual'

def extract_occasion(title):
    title = title.lower()
    if any(word in title for word in ['wedding', 'bridal', 'ethnic']):
        return 'wedding'
    elif any(word in title for word in ['party', 'heels']):
        return 'party'
    elif any(word in title for word in ['formal', 'office']):
        return 'interview'
    else:
        return 'daily'

def recommend_products(df, color, style, occasion, top_n=10):
    filtered = df[
        (df['color'] == color) &
        (df['style'] == style) &
        (df['occasion'] == occasion)
    ]

    if filtered.empty:
        filtered = df[df['style'] == style]

    filtered = filtered.sort_values(by='score', ascending=False)
    return filtered.head(top_n)
