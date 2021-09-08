# Created by newuser for 5.1.1
#antigen bundle zsh-users/zsh-autosuggestions
export ZSH=/home/guangrui/.oh-my-zsh
export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin
export PATH=/home/guangrui/bin:$PATH
export PYTHONSTARTUP="$(python -m jedi repl)"
#export NEPTUNE_API_TOKEN=eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vdWkubmVwdHVuZS5tbCIsImFwaV9rZXkiOiJjMTE0NTAxOS0yYTUxLTQzYzItYWUyOC1mNjRjZDRmOGI3ODMifQ==
export NEPTUNE_API_TOKEN="eyJhcGlfYWRkcmVzcyI6Imh0dHBzOi8vYXBwLm5lcHR1bmUuYWkiLCJhcGlfdXJsIjoiaHR0cHM6Ly9hcHAubmVwdHVuZS5haSIsImFwaV9rZXkiOiJjMTE0NTAxOS0yYTUxLTQzYzItYWUyOC1mNjRjZDRmOGI3ODMifQ=="
alias ls='ls --color=auto'
alias ll='ls -lh'
alias gg='nvidia-smi'
alias ck='pytype'
alias v='vim'
alias g0='CUDA_VISIBLE_DEVICES=0'
alias g1='CUDA_VISIBLE_DEVICES=1'
alias g2='CUDA_VISIBLE_DEVICES=2'
alias g01='CUDA_VISIBLE_DEVICES=0,1'
alias g12='CUDA_VISIBLE_DEVICES=1,2'
alias gall='CUDA_VISIBLE_DEVICES=0,1,2'
alias ggpu='watch -n 0.5 nvidia-smi'
alias to='tmux a -t'
alias ss='du -h --max-depth=1 .'



ZSH_THEME="robbyrussell"
plugins=(git
         extract
         python
         sublime
         osx
         zsh-autosuggestions)
source $ZSH/oh-my-zsh.sh
source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
export PATH=/home/guangrui/byobu/bin:/home/guangrui/.autojump/bin:/home/guangrui/anaconda3/bin:/home/guangrui/bin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/cuda/bin:/home/guangrui/data/SynLiDAR/wget/BaiduPCS-Go
alias bdy='BaiduPCS-Go'
alias gg='nvidia-smi'
alias gpu='CUDA_VISIBLE_DEVICES'
