from cx_Freeze import setup, Executable

copyDependentFiles=True
silent = True
#includes = ["re",  "gzip", "encodings.cp949", "encodings.utf_8", "encodings.ascii","glob","os","sys","subprocess","selenium"]
buildOptions = dict(
        compressed = True,
        includes = ["re",  "gzip", "encodings.cp949", "encodings.utf_8", "encodings.ascii","cfscrape","re","sys","selenium","urllib.request"],
        include_files = ["ReadMe.md"],
        bin_includes = ["ReadMe.md"]
        )
setup(name='Hulu Subs Downloader - Xonshiz',
     version='4.1',
      description='Little Python Script To Download Susb from HULU.',
      author='Xonshiz',
      author_email='Xonshiz@psychoticelites.com',
      options = dict(build_exe = buildOptions),
      executables=[Executable('HuluSubsDownloader.py')],
 ) 
