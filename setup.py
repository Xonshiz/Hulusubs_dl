from cx_Freeze import setup, Executable

copyDependentFiles=True
silent = True
#includes = ["re",  "gzip", "encodings.cp949", "encodings.utf_8", "encodings.ascii","glob","os","sys","subprocess","selenium"]
buildOptions = dict(
        compressed = True,
        includes = ["re",  "gzip", "encodings.cp949", "encodings.utf_8", "encodings.ascii","glob","os","sys","selenium","requests","bs4","time","lxml", "lxml._elementpath", "lxml.etree"],
        include_files = ["phantomjs.exe"],
        bin_includes = ["phantomjs.exe"]
        )
setup(name='Hulu Subs Downloader - Xonshiz',
     version='3.0',
      description='Little Python Script To Download Susb from HULU.',
      author='Xonshiz',
      author_email='Xonshiz@psychoticelites.com',
      options = dict(build_exe = buildOptions),
      executables=[Executable('Hulu_Subs_Downloader-Xonshiz.py')],
 ) 
