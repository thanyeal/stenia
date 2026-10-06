def sidebar(request):
    return {
        "sidebar_starred": [
            {"name": "job-contract-2026.pdf", "icon_class": "size-4 text-red-500"},
            {"name": "update-resume.pdf", "icon_class": "size-4 text-red-500"},
            {"name": "photoshoot-25.png", "icon_class": "size-4 text-green-500"},
        ],
        "sidebar_types": [
            {"label": "Images", "key": "images", "color": "bg-blue-500"},
            {"label": "Documents", "key": "documents", "color": "bg-red-500"},
            {"label": "Videos", "key": "videos", "color": "bg-amber-500"},
            {"label": "Audio", "key": "audio", "color": "bg-green-500"},
        ],
    }