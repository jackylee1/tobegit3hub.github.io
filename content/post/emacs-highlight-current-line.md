+++
date = "2013-12-30T08:35:31+08:00"
draft = true
title = "emacs highlight current line"

+++



## Configuration

<pre>
; show line number                                                                                                                                                                                                  
(global-linum-mode 1)
(setq linum-format "%d ")

; highlight current line                                                                                                                                                                                            
(global-hl-line-mode 1)

; highlight-tail-mode                                                                                                                                                                                               
;(global-highlight-tail-mode 1)                                                                                                                                                                                     
(add-hook 'text-mode-hook 'highlight-tail-mode)
</pre

## Reference

* <http://homepages.inf.ed.ac.uk/s0243221/emacs/>