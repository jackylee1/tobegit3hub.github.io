+++
date = "2015-07-17T08:35:33+08:00"
draft = true
title = "the project seagull"

+++



## Foreword

[Seagull](https://github.com/tobegit3hub/seagull) is the open-source friendly Web UI to manage and monitor docker.

It was open sourced on Oct 12, 2014 and is still ative development. Now it has 1053+ star in [GitHub](https://github.com/tobegit3hub/seagull) and 2362+ downloads in [DockerHub](https://registry.hub.docker.com/u/tobegit3hub/seagull/). Thanks to our contributors, seagull supports English, Chinese, German and French. Currently, we have added some exciting features like monitoring metrics of containers with the latest docker 1.7 APIs.

![](/images/seagull_home_page.png)

More and more users are using seagull to improve the usage of docker. With Web UI, we can manage our docker images and containers much easilier instead of command line. We're so glad to see the Japanese developers have post the [tutorial](http://knowledge.sakura.ad.jp/tech/2962/) about how to use seagull.

![](/images/seagull_japanese_tutorial.jpg)

Someone helps to recommand seagull in [hacker news](https://news.ycombinator.com/item?id=8713129). The most inspiring thing is that Solomon Hykes, the CTO of docker, has appreciated our project and hope we can continue to develop.

![](/images/seagull_hackernews.png)

## Introduction

If you're not familiar with seagull, you can watch the [three-minute video](https://www.youtube.com/watch?v=0BAiSx7l7Y4). You can also try seagull in your machine with just one command.

```
docker run -d -p 10086:10086 -v /var/run/docker.sock:/var/run/docker.sock tobegit3hub/seagull
```

![](/images/seagull_containers_page.png)

Seagull would be the best Web tool with full features.

* Easy to install and uninstall within docker container
* One click to start/stop/delete containers and images
* Super fast(<10ms) for searching and filtering
* Support multi-host management and monitoring
* I18n includes English, Chinese, German and French

It's wriiten in golang. For more information, please go to https://github.com/tobegit3hub/seagull .

## The future

Since we kicked of the project seagull, we're trying to build the best and most friendly tool for docker. We did it and seagull is one of the most popular docker projects which is super easy to deploy and use. But we're not satisfied. We're improving seagull almost every week and the latest release is 1.6 which is compatible with docker 1.7 APIs.

We're adding more and more features for developers if they need it. It's easy to add support for new languages. Please let us know if you has any trouble or any creative suggestion.

At last, I will show you my experience about "How I manage docker with seagull" in <http://slides.com/tobychan/how-i-manage> .

![](/images/how_i_manage_docker_with_seagull.jpg)