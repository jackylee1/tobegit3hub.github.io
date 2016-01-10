+++
date = "2016-01-10T08:35:33+08:00"
draft = true
title = "java 7 closeable"

+++



## Usage

Now you can write code with "try-with-resource" like this.

```
static String readFirstLineFromFile(String path) throws IOException {
    try (BufferedReader br = new BufferedReader(new FileReader(path))) {
        return br.readLine();
    }
}
```

And your resource should implement closeable interface.

