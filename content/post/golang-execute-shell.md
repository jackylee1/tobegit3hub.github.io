+++
date = "2015-07-24T08:35:33+08:00"
draft = true
title = "golang execute shell"

+++



## Code

```
import "syscall"
```

```
// Execute the command to replace current process. TODO: not used yet
func Exec(args []string) {
     path, err := exec.LookPath(args[0])
     if err != nil {
      	  os.Exit(1)
     }
     err = syscall.Exec(path, args, os.Environ())
     if err != nil {
       	   os.Exit(1)
     }
}
```


