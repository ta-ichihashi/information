# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_nameko_theme
sys.path.insert(0, os.path.abspath('.'))
from enum import Enum

class Author(Enum):
    organization: str = '滋賀県オリエンテーリング協会'
    author_native: str = '市橋 卓'
    author_en: str = 'Takashi Ichihashi'

    @classmethod
    def get_strings(cls, delimiter = ' '):
        return delimiter.join([e.value for e in cls])


# -- Project information -----------------------------------------------------

titles = ['滋賀県オリエンテーリング協会']

project = '滋賀県オリエンテーリング協会'
copyright = '2024, 滋賀県オリエンテーリング協会事務局 <orienteering.shiga.contact@gmail.com>'
author = Author.author_native.value

# The full version, including alpha/beta/rc tags
release = '第1版'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'japanesesupport',
    'sphinx.ext.githubpages',
    'sphinxnotes.strike',
    'docxbuilder'
    ]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

suppress_warnings = ["myst.header"]

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

#### Config for plugins

numfig = True

# Fontpath for blockdiag (truetype font)
#blockdiag_fontpath = 'C:/Windows/fonts/YuGothM.ttc'
# Fontpath for blockdiag (truetype font)
blockdiag_fontpath = './source/assets/ipaexg.ttf'
actdiag_fontpath = './source/assets/ipaexg.ttf'
seqdiag_fontpath = './source/assets/ipaexg.ttf'
nwdiag_fontpath = './source/assets/ipaexg.ttf'

# -- Options for revealjs output -------------------------------------------------
revealjs_style_theme = 'sky'
# 普通のHTMLと同じものを使えるので、簡単な設定として指定
#revealjs_static_path = html_static_path
# Reveal.jsプレゼンテーションで使うCSSファイルを指定
# revealjs_static_pathで指定したフォルダからのパス
revealjs_css_files = [
    "slides.css",
]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
"""
# For book theme
html_theme = 'sphinx_book_theme'
# html_static_path = ['_static']
html_sidebars = {
    "**": ["sbt-sidebar-nav.html"]
}

html_theme_options = {
    "repository_url": "https://github.com/ta-ichihashi/orienteering-shiga",
    "use_repository_button": True,
    "home_page_in_toc": True,
}

# For Mozilla sphinx theme
html_theme = 'mozilla'
html_theme_path = [os.path.dirname(mozilla_sphinx_theme.__file__)]

"""

html_theme = 'nameko'
html_theme_path = [sphinx_nameko_theme.get_html_theme_path()]


# These folders are copied to the documentation's HTML output.
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...).
html_css_files = ["custom.css"]

html_theme_options = dict(
    project_name = "滋賀県オリエンテーリング協会",
    logo = "img/shiga-o-flag.svg",
    logo_alt = "Orienteering-Shiga",
    logo_height = 59,
    logo_url = "/information/",
    logo_width = 105,
    github_url = "https://github.com/orienteering-shiga/information/blob/main/source/",
    header_links = "イベント開催届提出|/terrain/event_application.html, 後援依頼|/sponsorship/index.html, 滋賀県協会開催イベント|/events/"
)

html_sidebars = {"**": [
    "searchbox.html",
    "contact.html",
    "globaltoc.html",
]}

# Docx builder extensions

docx_documents = [
    ('index', 'Shiga-pref_orienteering_assosiation_info.docx', {'title': '滋賀県オリエンテーリング協会ご案内',
     'creator': '滋賀県オリエンテーリング協会事務局', 'subject': '滋賀県オリエンテーリング協会ご案内', }, True),
]

docx_style = '_templates/template.docx'

docx_coverpage = True
docx_pagebreak_before_section = 1
docx_pagebreak_after_table_of_contents = 0
docx_table_options = {
    'landscape_columns': 6,      #
    'in_single_page': True,      #
    'row_splittable': True,      #
    'header_in_all_page': True,  #
}



# Myst extensions
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "amsmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]


#latex_docclass = {'manual': 'jsbook'}

latex_elements = {
    # Latex figure (float) alignment
    #
    'figure_align': 'H',
    'sphinxsetup': "verbatimforcewraps, verbatimmaxunderfull=0"
}


latex_engine = 'lualatex'

latex_docclass = {'manual': 'ltjsbook'}

# 改行コマンド `\\` を挟んで連結する(A)
my_latex_title_lines = '\\\\'.join(titles)

latex_elements = {
    # (C) Polyglossiaパッケージを読み込まないようにする
    'polyglossia': '',
    'fontpkg': r'''
        \setmainfont{DejaVu Serif}
        \setsansfont{DejaVu Sans}
        \setmonofont{DejaVu Sans Mono}
        ''',
    'preamble': r'''

        % my_latex_title_linesをLaTeXの世界に持ち込む
        \newcommand{\mylatextitlelines}{''' + my_latex_title_lines + r'''}
        \newcommand{\mylatexauthorlines}{''' + Author.get_strings('\\\\') + r'''}

        % 表紙テンプレート内でアットマークが使われているため、アットマークを通常の文字として扱う
        \makeatletter

        % 表紙テンプレートを再定義(B)
        \renewcommand{\sphinxmaketitle}{%
            \let\sphinxrestorepageanchorsetting\relax
            \ifHy@pageanchor\def\sphinxrestorepageanchorsetting{\Hy@pageanchortrue}\fi
            \hypersetup{pageanchor=false}% avoid duplicate destination warnings
            \begin{titlepage}%
                \let\footnotesize\small
                \let\footnoterule\relax
                \noindent\rule{\textwidth}{1pt}\par
                \begingroup % for PDF information dictionary
                \def\endgraf{ }\def\and{\& }%
                \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
                \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
                \endgroup
                \begin{flushright}%
                \sphinxlogo
                \py@HeaderFamily
                {\Huge \mylatextitlelines \par} % <--- ここで\mylatextitlelinesを使用(C)
                {\itshape\LARGE \py@release\releaseinfo \par}
                \vfill
                {\LARGE
                    \begin{tabular}[t]{l}
                    \mylatexauthorlines
                    %\@author
                    \end{tabular}\kern-\tabcolsep
                    \par}
                \vfill\vfill
                {\large
                \@date \par
                \vfill
                \py@authoraddress \par
                }%
                \end{flushright}%\par
                \@thanks
            \end{titlepage}%
            \setcounter{footnote}{0}%
            \let\thanks\relax\let\maketitle\relax
            %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
            \clearpage
            \ifdefined\sphinxbackoftitlepage\sphinxbackoftitlepage\fi
            \if@openright\cleardoublepage\else\clearpage\fi
            \sphinxrestorepageanchorsetting
        } % 表紙スタイル終わり
        % アットマークを特殊文字に戻す
        \makeatother

        \setcounter{tocdepth}{1}
        \usepackage[titles]{tocloft}
        %\usepackage[OT1]{fontenc}
        \cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
        \setlength{\cftchapnumwidth}{1.5cm}
        \setlength{\cftsecindent}{\cftchapnumwidth}
        \setlength{\cftsecnumwidth}{1.25cm}
        \addtolength{\footskip}{0mm}
        ''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex'
}


latex_show_urls = 'footnote'


# for epub


epub_title = project
epub_author = author
epub_basename = 'orienteering_shiga'
epub_language = 'ja'
epub_publisher = author
#epub_identifier = u'http://ascii.asciimw.jp/books/books/detail/978-4-04-868629-7.shtml'
epub_scheme = 'URL'
epub_tocdepth = 3
