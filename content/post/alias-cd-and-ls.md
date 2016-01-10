+++
date = "2014-03-31T08:35:31+08:00"
draft = true
title = "alias cd and ls"

+++



## .zshrc

<pre>
# cd and ls                                                                                                                                                                                                         
function chpwd() {
  emulate -L zsh
  ls -a
}
</pre>

## Reference

* <http://stackoverflow.com/questions/3964068/zsh-automatically-run-ls-after-every-cd>