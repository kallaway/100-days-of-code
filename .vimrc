" vimrc file

set enc=utf-8
set fenc=utf-8
set termencoding=utf-8

set nocompatible	"use vim defaults
set ls=2	" always show status line
set tabstop=4	" number of spaces of tab character
set shiftwidth=4	" number of spaces to (auto) indent
set hlsearch		" highlight searches
set ignorecase		" ignore case when searching
"set noignorecase	" don't ignore case when searching
set title		" show title in the console title bar

set noautoindent	" don't autoindent
set nosmartindent	" don't smartindent
set nocindent		" don't indent syntax
set number		" show line numbers

" set new filetype for opencl and flow/conf files
au BufRead,BufNewFile *.cl set filetype=c
au BufRead,BufNewFile *.flow set filetype=c
au BufRead,BufNewFile *.conf set filetype=c

" enable doxygen
let mysyntaxfile='~/.vim/doxygen_load.vim'

syntax on		" highlight syntax
filetype indent plugin on

colorscheme torte 	" use this color scheme

autocmd! BufNewFile * silent! 0r ~/.vim/skel/tmpl.%:e

au FileType matlab,cpp,c,java,sh,pl,php,asp,python set autoindent
au FileType matlab,cpp,c,java,sh,pl,php,asp set smartindent
"au FileType matlab,cpp,c,java,sh,pl,php,asp,python set tabstop=4
"au FileType matlab,cpp,c,java,sh,pl,php,asp,python set shiftwidth=4
au FileType matlab,cpp,c,java,sh,pl,php,asp,python set expandtab
au FileType python set nosmartindent

au FileType cpp,c set textwidth=120
au FileType cpp,c set t_Co=256

"for omnicomplete stuff
set nocp
filetype plugin on

map <C-F12> :!ctags -R --c++-kinds=+p --fields=+iaS --extra=+q .<CR>

set tags+=/vobs/iungo/tags
set tags+=/vobs/iungo_steps/tags

" set guifont=Courier\ 10\ Pitch\ 8
set guifont=Monospace\ 8
if has('gui_running')
	set columns=120
endif
