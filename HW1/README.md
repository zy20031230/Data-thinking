## 数据处理
### date:9.16
1. 年龄118表示大量重复错误数据
2. profile残缺数据删除
3. 同时由于聚合,导致部分消费数据丢失
4. 按照用户id聚合数据,其中用户行为已经转化为字典,可以通过event-time-value,在value的位置上索引data['event-time-value'][2],对照transcipt表,同时把部分错误标签修正
5. 查找表为transcipt

### date:9.17

1. 计算出amount总和
2. TODO 进一步提取出每一种推销策略数据的分类