
# Changelog
- Re-did the entire codebase and implemented hulu API to scrap data.
- Proxy support added.
- Fix for #22
- Added Verbose Logging.
- `#22` was still happening. Verified and fixed it.
- Updated TravisCI Configs to do a Github Release.
- Fixed #27
- Added support to download subtitles of "movies".
- Fix for #29 and #28
- Fix for #25
- Fix for #31
- Subtitles will now show proper language names instead of 'en', 'es', etc.
- Fix for path naming issues #31
- Change config file location to ~/.config and add check to utils.createFile() to see if directory exists. Creates directoy if not exists
