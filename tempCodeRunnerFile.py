# Create labels for the title, copyright, explanation, and url
title_label = tk.Label(info_frame, text=info['title'])
copyright_label = tk.Label(info_frame, text=info['copyright'])
explanation_label = tk.Label(info_frame, text=info['explanation'])
url_label = tk.Label(info_frame, text=info['url'], fg="blue", cursor="hand2")