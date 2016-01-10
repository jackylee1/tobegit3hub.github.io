+++
date = "2014-09-19T08:35:32+08:00"
draft = true
title = "insert shuihuzhuan into mycomputerxyz"

+++



Here is the database schema.

<pre>
CREATE TABLE IF NOT EXISTS item (
   id int PRIMARY KEY AUTO_INCREMENT,
   username varchar(255) REFERENCES user(name),
   number int,
   image varchar(255),
   description varchar(255)
);
</pre>

And I insert data like this.

<pre>
insert into item values(null, "水浒传", 29, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-29.jpg", "29. 短命二郎 阮小五");
insert into item values(null, "水浒传", 30, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-30.jpg", "30. 浪里白条 张顺");
insert into item values(null, "水浒传", 31, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-31.jpg", "31. 活阎罗 阮小七");
insert into item values(null, "水浒传", 32, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-32.jpg", "32. 病关索 杨雄");
insert into item values(null, "水浒传", 33, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-33.jpg", "33. 拼命三郎 石秀");
insert into item values(null, "水浒传", 34, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-34.jpg", "34. 两头蛇 解珍");
insert into item values(null, "水浒传", 35, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-35.jpg", "35. 双尾蝎 解宝");
insert into item values(null, "水浒传", 36, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-36.jpg", "36. 浪子 燕青");
insert into item values(null, "水浒传", 37, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-37.jpg", "37. 神机军师 朱武");
insert into item values(null, "水浒传", 38, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-38.jpg", "38. 镇三山 黄信");
insert into item values(null, "水浒传", 39, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-39.jpg", "39. 病尉迟 孙立");
insert into item values(null, "水浒传", 40, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-40.jpg", "40. 丑郡马 宣赞");
insert into item values(null, "水浒传", 41, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-41.jpg", "41. 井木犴 郝思文");
insert into item values(null, "水浒传", 42, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-42.jpg", "42. 百胜将 韩滔");
insert into item values(null, "水浒传", 43, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-43.jpg", "43. 天目将 彭玘");
insert into item values(null, "水浒传", 44, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-44.jpg", "44. 圣水将 单廷圭");
insert into item values(null, "水浒传", 45, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-45.jpg", "45. 神火将 魏定国");
insert into item values(null, "水浒传", 46, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-46.jpg", "46. 圣手书生 萧让");
insert into item values(null, "水浒传", 47, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-47.jpg", "47. 铁面孔目 裴宣");
insert into item values(null, "水浒传", 48, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-48.jpg", "48. 摩云金翅 欧鹏");
insert into item values(null, "水浒传", 49, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-49.jpg", "49. 火眼狻猊 邓飞");
insert into item values(null, "水浒传", 50, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-50.jpg", "50. 锦毛虎 燕顺");
insert into item values(null, "水浒传", 51, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-51.jpg", "51. 锦豹子 杨林");
insert into item values(null, "水浒传", 52, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-52.jpg", "52. 轰天雷 凌振");
insert into item values(null, "水浒传", 53, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-53.jpg", "53. 神算子 蒋敬");
insert into item values(null, "水浒传", 54, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-54.jpg", "54. 小温侯 吕方");
insert into item values(null, "水浒传", 55, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-55.jpg", "55. 赛仁贵 郭盛");
insert into item values(null, "水浒传", 56, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-56.jpg", "56. 神医 安道全");
insert into item values(null, "水浒传", 57, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-57.jpg", "57. 紫髯伯 皇甫端");
insert into item values(null, "水浒传", 58, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-58.jpg", "58. 矮脚虎 王英");
insert into item values(null, "水浒传", 59, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-59.jpg", "59. 一丈青 扈三娘");
insert into item values(null, "水浒传", 60, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-60.jpg", "60. 丧门神 鲍旭");
insert into item values(null, "水浒传", 61, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-61.jpg", "61. 混世魔王 樊瑞");
insert into item values(null, "水浒传", 62, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-62.jpg", "62. 毛头星 孔明");
insert into item values(null, "水浒传", 63, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-63.jpg", "63. 独火星 孔亮");
insert into item values(null, "水浒传", 64, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-64.jpg", "64. 八臂哪吒 项充");
insert into item values(null, "水浒传", 65, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-65.jpg", "65. 飞天大圣 李衮");
insert into item values(null, "水浒传", 66, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-66.jpg", "66. 玉臂匠 金大坚");
insert into item values(null, "水浒传", 67, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-67.jpg", "67. 铁笛仙 马麟");
insert into item values(null, "水浒传", 68, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-68.jpg", "68. 出洞蛟 童威");
insert into item values(null, "水浒传", 69, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-69.jpg", "69. 翻江蜃 童猛");
insert into item values(null, "水浒传", 70, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-70.jpg", "70. 玉幡竿 孟康");
insert into item values(null, "水浒传", 71, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-71.jpg", "71. 通臂猿 侯健");
insert into item values(null, "水浒传", 72, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-72.jpg", "72. 跳涧虎 陈达");
insert into item values(null, "水浒传", 73, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-73.jpg", "73. 白花蛇 杨春");
insert into item values(null, "水浒传", 74, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-74.jpg", "74. 白面郎君 郑天寿");
insert into item values(null, "水浒传", 75, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-75.jpg", "75. 九尾亀 陶宗旺");
insert into item values(null, "水浒传", 76, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-76.jpg", "76. 铁扇子 宋清");
insert into item values(null, "水浒传", 77, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-77.jpg", "77. 铁叫子 乐和");
insert into item values(null, "水浒传", 78, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-78.jpg", "78. 花项虎 龚旺");
insert into item values(null, "水浒传", 79, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-79.jpg", "79. 中箭虎 丁得孙");
insert into item values(null, "水浒传", 80, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-80.jpg", "80. 小遮拦 穆春");
insert into item values(null, "水浒传", 81, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-81.jpg", "81. 操刀鬼 曹正");
insert into item values(null, "水浒传", 82, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-82.jpg", "82. 云里金刚 宋万");
insert into item values(null, "水浒传", 83, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-83.jpg", "83. 摸着天 杜迁");
insert into item values(null, "水浒传", 84, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-84.jpg", "84. 病大虫 薛永");
insert into item values(null, "水浒传", 85, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-85.jpg", "85. 打虎将 李忠");
insert into item values(null, "水浒传", 86, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-86.jpg", "86. 小霸王 周通");
insert into item values(null, "水浒传", 87, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-87.jpg", "87. 金钱豹子 汤隆");
insert into item values(null, "水浒传", 88, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-88.jpg", "88. 鬼脸儿 杜兴");
insert into item values(null, "水浒传", 89, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-89.jpg", "89. 出林龙 邹渊");
insert into item values(null, "水浒传", 90, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-90.jpg", "90. 独角龙 邹润");
insert into item values(null, "水浒传", 91, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-91.jpg", "91. 旱地忽律 朱贵");
insert into item values(null, "水浒传", 92, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-92.jpg", "92. 笑面虎 朱富");
insert into item values(null, "水浒传", 93, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-93.jpg", "93. 金眼彪 施恩");
insert into item values(null, "水浒传", 94, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-94.jpg", "94. 铁臂膊 蔡福");
insert into item values(null, "水浒传", 95, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-95.jpg", "95. 一枝花 蔡庆");
insert into item values(null, "水浒传", 96, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-96.jpg", "96. 催命判官 李立");
insert into item values(null, "水浒传", 97, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-97.jpg", "97. 青眼虎 李云");
insert into item values(null, "水浒传", 98, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-98.jpg", "98. 没面目 焦挺");
insert into item values(null, "水浒传", 99, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-99.jpg", "99. 石将军 石勇");
insert into item values(null, "水浒传", 100, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-100.jpg", "100. 小尉迟 孙新");
insert into item values(null, "水浒传", 101, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-101.jpg", "101. 母大虫 顾大嫂");
insert into item values(null, "水浒传", 102, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-102.jpg", "102. 菜园子 张青");
insert into item values(null, "水浒传", 103, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-103.jpg", "103. 母夜叉 孙二娘");
insert into item values(null, "水浒传", 104, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-104.jpg", "104. 活闪婆 王定六");
insert into item values(null, "水浒传", 105, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-105.jpg", "105. 险道神 郁保四");
insert into item values(null, "水浒传", 106, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-106.jpg", "106. 白日鼠 白胜");
insert into item values(null, "水浒传", 107, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-107.jpg", "107. 鼓上蚤 时迁");
insert into item values(null, "水浒传", 108, "http://mycomputerxyz.qiniudn.com/shuihuzhuan-108.jpg", "108. 金毛犬 段景住");
</pre>