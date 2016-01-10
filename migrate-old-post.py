#!/usr/bin/env python

from os import listdir
from os.path import isfile, join

from subprocess import call

def main():
    print("Start to migrate old posts")

    path = "/Users/tobe/code/tobegit3hub.github.io.old/_posts"
    old_post_files = [f for f in listdir(path) if isfile(join(path, f))]

    for old_post_name in old_post_files:
        # Example: 2015-10-19-simple-japenese.md
        if old_post_name.startswith("20"):
            # Example: simple-japenese.md
            new_post_name = old_post_name[11:]
            #print(new_post_name)

            # 1. Gernerate new post files
            # call(["hugo", "new", "post/" + new_post_name])

            # 2. Write content to new post
            old_post = open('/Users/tobe/code/tobegit3hub.github.io.old/_posts/' + old_post_name, 'r')
            # Example: "---header--- just content"
            post_content = old_post.read()
            # Example: "just content"
            post_content_no_header = post_content.split("---")[2]
            old_post.close()
            
            # Append content to new file
            #new_post = open("/Users/tobe/code/tobegit3hub.github.io/content/post/" + new_post_name, "a")
            #new_post.write(post_content_no_header)
            #new_post.close()

            # 3. Modify the time of post
            # Example: 2012-12-31
            year = old_post_name[0:4]
            month = old_post_name[5:7]
            day = old_post_name[8:10]
            #print(year + "-" + month + "-" + day)

            new_post = open("/Users/tobe/code/tobegit3hub.github.io/content/post/" + new_post_name, "r")
            origin_post_content = new_post.read()

            # Example: "2016-01-10T08:35:27+08:00" to " "2015-10-19T08:35:27+08:00"
            new_post_content = origin_post_content.replace('-10', "-" + day, 1)
            new_post_content = new_post_content.replace('-01', "-" + month, 1)
            new_post_content = new_post_content.replace('2016', year, 1)
            new_post.close()

            new_post_to_write = open("/Users/tobe/code/tobegit3hub.github.io/content/post/" + new_post_name, "w")
            new_post_to_write.write(new_post_content)
            new_post_to_write.close()

    print("End of migrating")

if __name__ == "__main__":
    main()


