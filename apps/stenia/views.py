from django.shortcuts import render

_TYPE_ICON = {
    "pdf": "size-4 text-red-500",
    "image": "size-4 text-green-500",
    "video": "size-4 text-amber-500",
    "doc": "size-4 text-blue-500",
    "audio": "size-4 text-slate-500",
}


def _file(name, kind, folder, size, modified, starred=False):
    return {
        "name": name,
        "icon_class": _TYPE_ICON[kind],
        "folder": folder,
        "size": size,
        "modified": modified,
        "starred": starred,
    }


_FOLDERS = [
    {"name": "Images", "count": 189},
    {"name": "Documents", "count": 100},
    {"name": "Videos", "count": 11},
]

_STORAGE = {
    "used": "13.1GB",
    "total": "25GB",
    "used_percent": 52,
    "segments": [
        {"label": "Images", "size": "10.3GB", "percent": 41.2, "color": "bg-blue-500"},
        {"label": "Documents", "size": "2.1GB", "percent": 8.4, "color": "bg-red-500"},
        {"label": "Videos", "size": "600MB", "percent": 2.4, "color": "bg-amber-500"},
        {"label": "Audio", "size": "100MB", "percent": 0.4, "color": "bg-green-500"},
    ],
}

_RECENT_FILES = [
    _file("job-contract-2026.pdf", "pdf", "Documents", "1.2 MB", "Today, 10:42", True),
    _file("photoshoot-25.png", "image", "Images", "4.8 MB", "Today, 09:15", True),
    _file("update-resume.pdf", "pdf", "Documents", "340 KB", "Today, 08:50", True),
    _file("vacation-clips-2025.mp4", "video", "Videos", "212 MB", "Yesterday, 21:30"),
    _file("project-brief-q2.docx", "doc", "Documents", "88 KB", "Yesterday, 18:05"),
    _file("bella-headshot-final.jpg", "image", "Images", "2.1 MB", "Yesterday, 14:22"),
    _file("podcast-ep12.mp3", "audio", "Audio", "34 MB", "Mar 29, 11:00"),
    _file("brand-kit-v3.png", "image", "Images", "780 KB", "Mar 29, 09:45"),
    _file("invoice-march-2026.pdf", "pdf", "Documents", "210 KB", "Mar 28, 17:33"),
    _file("screen-recording-demo.mp4", "video", "Videos", "95 MB", "Mar 28, 15:10"),
    _file("logo-dark-mode.svg", "image", "Images", "18 KB", "Mar 28, 12:00"),
]


def _page(template, title):
    def view(request):
        return render(request, template, {"page_title": title})
    return view


def dashboard(request):
    return render(request, "pages/dashboard.django", {
        "page_title": "Dashboard",
        "folders": _FOLDERS,
        "storage": _STORAGE,
        "recent_files": _RECENT_FILES,
        "total_files": "1,290",
        "total_size": "13.1 GB",
    })


files_browser       = _page("pages/files_browser.django", "File Browser")
my_files            = _page("pages/my_files.django", "My files")
shared_with_me      = _page("pages/shared_with_me.django", "Shared with me")
recent              = _page("pages/recent.django", "Recent")
recently_deleted    = _page("pages/recently_deleted.django", "Recently deleted")
settings            = _page("pages/settings.django", "Settings")
integrations        = _page("pages/integrations.django", "Integrations")
profile             = _page("pages/profile.django", "Profile")
telegram_setup      = _page("pages/telegram_setup.django", "Telegram Setup")
