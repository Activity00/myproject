
**pipeline 设计**
 1.数据的去重过滤
 3.mongo存储
 5.新增日志
 总结：pipeline设计要围绕item取判断然后多层去重过滤，因为无论spider里面url、逻辑是什么
      最终要实现的是返回指的item，持续爬取的设计的关键还在数据表的设计啊。