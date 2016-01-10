+++
date = "2016-01-10T08:35:29+08:00"
draft = true
title = "android share button"

+++



<pre>     
Intent intent = new Intent(Intent.ACTION_SEND);
intent.setType(“text/plain”);
intent.putExtra(Intent.EXTRA_SUBJECT, “Share A SongStory”);
intent.putExtra(Intent.EXTRA_TEXT, “The status update text”);
startActivity(Intent.createChooser(intent, “Share A SongStory”));
</pre>