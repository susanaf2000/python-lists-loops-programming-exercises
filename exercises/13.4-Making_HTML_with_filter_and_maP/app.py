all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

def generate_li(color):
    return f'<li>{color["label"]}</li>'

def filter_colors(colors):
    sexy_colors = filter(lambda color: color["sexy"], colors)
    return list(map(generate_li, sexy_colors))

sexy_colors_list = filter_colors(all_colors)
print(sexy_colors_list)


