syntax enable
filetype off  " required!
filetype plugin indent on  " required!

set nu
set ruler
set showcmd
set t_Co=256
set background=dark
set laststatus=2
set cursorcolumn
set hlsearch
set tags=tags;
set autochdir
set colorcolumn=120

" PEP8 au BufNewFile,BufRead *.py
set tabstop=4
set softtabstop=4
set shiftwidth=4
set textwidth=79
set expandtab
set autoindent
set fileformat=unix

set rtp+=/root/.vim/bundle/Vundle.vim/
call vundle#begin('/root/.vim/bundle/')

Bundle 'VundleVim/Vundle.vim'
Bundle 'ervandew/supertab'
Bundle 'scrooloose/nerdtree'
Bundle 'scrooloose/nerdcommenter'
Bundle 'majutsushi/tagbar'
Bundle 'kien/ctrlp.vim'
Bundle 'flazz/vim-colorschemes'
Bundle 'bling/vim-airline'
Bundle 'vim-airline/vim-airline-themes'
Bundle 'junegunn/vim-easy-align'
Bundle 'jiangmiao/auto-pairs'
Bundle 'mattn/emmet-vim'
Bundle 'easymotion/vim-easymotion'
Bundle 'fholgado/minibufexpl.vim'
Bundle 'nathanaelkane/vim-indent-guides.git'
Bundle 'chemzqm/vim-run'
Bundle 'davidhalter/jedi-vim'

call vundle#end()


let mapleader=','

" jedi-vim 代码补全
let g:jedi#auto_initialization = 1
let g:jedi#auto_vim_configuration = 1
let g:jedi#goto_definitions_command = '<leader>g'
let g:jedi#documentation_command = '<leader>k'
let g:jedi#usages_command = '<leader>u'
let g:jedi#completions_command = '<Tab>'
let g:jedi#rename_command = '<leader>r'
let g:jedi#completions_enabled = 1
let g:SuperTabDefaultCompletionType = "context"  
let g:jedi#popup_on_dot = 0 
autocmd FileType python setlocal completeopt-=preview
" <C-o> <C-i> 光标跳到上/下一个位置

" easymotion/vim-easymotion 搜索跳转
map ff <Plug>(easymotion-sn)
let g:EasyMotion_smartcase = 1      " 忽略大小写

" scrooloose/nerdtree 树形目录结构
map <F1> :NERDTreeToggle<CR>
let g:NERDTreeDirArrowExpandable = '+'
let g:NERDTreeDirArrowCollapsible = '-'

" majutsushi/tagbar 代码结构
map <F2> :TagbarToggle<CR>
let g:tagbar_right = 1

" scrooloose/nerdcommenter 代码注释
let g:NERDSpaceDelims=1
",cc ,cu, cA, c<Space>, n,cc n,cu

" kien/ctrlp.vim 文件超级搜
let g:ctrlp_map = '<C-S-n>' 
let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn|pyc)$'   " 设置过滤不进行查找的后缀名
"let g:ctrlp_cmd = 'CtrlN'

" fholgado/minibufexpl.vim 多文档编辑
map <C-Right> :MBEbn<cr>     " buffer 切换快捷键
map <C-Left> :MBEbp<cr>
" Ctrl+w s/Ctrl+w v/Ctrl+w q   	上下/左右/关闭分屏
" :vs filename/:vs filename"

" nathanaelkane/vim-indent-guides.git 代码缩进
"let g:indent_guides_enable_on_vim_startup = 1     " 随vim自启动
map <F3> :IndentGuidesToggle<CR>
let g:indent_guides_start_level = 2       " 从第二层开始可视化显示缩进
let g:indent_guides_guide_size = 1      " 色块宽度

" chemzqm/vim-run 运行代码
let g:vim_run_command_map = {'python': 'python'}
map <C-r> :Run<cr>


" 宏录制
" 书签
" 多寄存器

" <k0> - <k9> 小键盘 0 到 9
" <S-...> Shift＋键
" <C-...> Control＋键
" <M-...> Alt＋键 或 meta＋键
" <A-...> 同 <M-...>
" <Esc> Escape 键
" <Up> 光标上移键
" <Space> 插入空格
" <Tab> 插入Tab
" <CR> 等于<Enter>

