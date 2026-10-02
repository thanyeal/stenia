# Stenia: Requirements

**Stenia** is a free, open-source, self-hosted file storage app that works like Google Drive. It runs on your own PC and uses Telegram as the cloud drive.
Expansion: Secured Telegram Enabled Network for Integrated Access.

## Scope for the first build

- Django web app, hosted on localhost (custom port)
- Storage backend: the Telegram API, used as the cloud drive
- Files live in a private Telegram channel (not Saved Messages)
- Free and open source
- Android app comes later, as a separate repo (React Native)
- Tailscale for phone access is for later testing, not a priority

## Design principles

- Stenia is a cloud drive, not a local mirror. It does not keep full local copies of files.
- Stenia never deletes the user's local original files on its own.
- Sync is one-way (local to Telegram) at first. Two-way sync comes later.
- The user logs in to Stenia first. Telegram and other provider credentials are entered only after login, in Settings, and stored encrypted on the local machine. They are never requested or shown before login and never committed to the repo.
- Keep a storage provider interface, so more providers can be added later without a rewrite. Telegram is the only provider for now.

## P1: Core (MVP)

- First-run setup: Telegram login (phone, code, optional 2FA), create or choose a private channel, add a backup admin account to the channel
- Login to the Stenia web app
- Create folders
- Upload files and folders (drag and drop, progress, resumable)
- Upload queue with staging: a file is marked done only after the upload is verified by size and hash and its message ID is saved
- "Incomplete" state for large files until every chunk is verified (never offered for download)
- Download files, and folders as ZIP
- Rename, move, copy, delete
- Trash with restore
- Search, sort, filter, group by file type
- Bulk select actions
- Storage usage display, calculated from the index (Telegram sets no quota)
- Settings page: Telegram connection status and target channel
- List and grid view, breadcrumb navigation
- Safe file handling: name collisions, path traversal protection, streaming large files
- "Telegram unavailable" paused state: the queue pauses, staged files stay on disk, and uploads resume when access returns
- "Reconnect" screen when the session expires or the user is logged out; the library stays browsable (read-only) from the index
- Export everything: download all files with the original folder structure (works while access exists)
- Metadata backup and export, plus rolling local backups of the index
- SQLite transactions: an index entry exists only after a verified upload
- Store a hash for every file at upload time (needed for duplicates and integrity checks)
- Storage provider interface (Telegram is the first provider)

## P2: Rich features

- **Sync folders:** the user selects which local folders sync to Telegram (one-way). A changed file is uploaded only after it has been stable for a few seconds. The local file stays untouched until the new upload is verified, and the last verified version stays in the index. If Telegram is unavailable, changes stay queued as "pending".
- **Projects:** named collections that point to existing files and folders (nothing is moved or copied), with a description, notes, and their own page in the sidebar
- **Client-side encryption:** files are encrypted before upload, since they sit on Telegram's servers
- **Recovery key flow:** show a recovery key or passphrase at setup and require the user to confirm it is saved
- **Reconnect with another account:** link a new Telegram account to the same channel
- **Index rebuild tool:** scans the channel and recreates the database
- Size-limited cache for thumbnails and recently opened files (for speed only)
- File preview (images, PDF, video, audio, text) and thumbnails
- Starred and recent files
- Tags and labels
- Duplicate detection by hash
- Auto-organize rules (example: all .jpg files go to Photos)
- Full-text search
- Activity log
- Integrity check that re-hashes files to catch corruption
- Bulk rename and saved searches
- Dark mode and keyboard shortcuts
- API tokens (needed for the phone app later)

## P3: Later

- Optional second storage provider (for example S3-compatible or local) to replicate chosen "critical" folders
- "Free up space": opt-in, removes a local copy only after the upload is verified, with a clear warning
- Two-way sync with conflict handling
- Dashboards and analytics
- Share links with expiry and password
- File versioning
- Multi-user accounts and permissions
- Optional "Ask about this project" chat using the user's own LLM API key
- Tailscale remote access
- Android app (React Native)

## Technical notes

- Telegram client: MTProto (Telethon or Pyrogram) with a user session. The Bot API has small file size limits.
- Telegram has no folders. Folders are virtual: SQLite maps the folder tree to Telegram message IDs.
- SQLite is required. It is the only record of where each file is.
- Files over Telegram's size limit (about 2GB, higher with Premium) are split into chunks and rejoined on download.
- Back up the SQLite index to Telegram on a schedule, so the library can be rebuilt if the local file is lost.
- Handle Telegram rate limits (FloodWait) with an upload queue and retries.
- Use a dedicated Telegram account for Stenia, not a personal one.
- Store `api_id`, `api_hash` and the session file locally only, encrypted. Add them to `.gitignore`, since the repo is open source.
- Windows packaging: PyInstaller or Nuitka, Inno Setup installer, tray icon
- Security: bind to `127.0.0.1` only, check the `Origin` header, use session tokens
- API address must be configurable (not hardcoded to localhost)
- API must be separate from the UI so the phone app can reuse it

## Risks

- Telegram policy changes or account restrictions could affect access
- Speed depends on Telegram's limits
- If the Telegram account is banned or deleted, files that exist only in Telegram cannot be recovered. Files still in the user's synced local folders are safe. State this plainly in the README and on the first-run screen.
