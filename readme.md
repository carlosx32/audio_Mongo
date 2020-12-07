load enviroment variables with
    source env.sh

start python env with pyenv

    https://github.com/pyenv/pyenv-virtualenv
    
    pyenv install 3.8.2
    
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

    pyenv virtualenv 3.8.2 mongo3.8
    pyenv activate mongo3.8