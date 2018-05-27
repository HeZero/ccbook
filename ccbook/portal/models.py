import uuid
import time
from django.db import models


class Classify(models.Model):

    id = models.AutoField(primary_key=True, max_length=11)
    uni_uuid = models.CharField(unique=True, max_length=40)
    create_time = models.CharField(max_length=40)
    update_time = models.CharField(max_length=40)

    parent_uuid = models.CharField(db_index=True, max_length=40)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=225)
    index = models.IntegerField(default=0, help_text="分类排序")
    use = models.BooleanField(default=True, help_text="是否使用")

    def save(self, *args, **kwargs):
        self.uni_uuid = str(uuid.uuid1())
        self.create_time = str(time.time() * 1000)
        self.update_time = "0"
        super(Classify, self).save(*args, **kwargs)

    class Meta:
        ordering = ['index']


class Book(models.Model):

    id = models.AutoField(primary_key=True, max_length=11)
    uni_uuid = models.CharField(unique=True, max_length=40)
    create_time = models.CharField(max_length=40)
    update_time = models.CharField(max_length=40)

    name = models.CharField(db_index=True, max_length=100)
    personal_title = models.CharField(max_length=225, default='', help_text="个性化标题")
    author = models.CharField(db_index=True, max_length=100)
    introduction = models.CharField(max_length=400, default='', help_text="简介")
    detail_url = models.CharField(max_length=225, default='', help_text="详情链接")
    image_url = models.CharField(max_length=225, default='http://images.zhulang.com/b'
                                                         'ook_cover/image/38/58/385884_x160.jpg', help_text="封面图片")
    click_num = models.BigIntegerField(default=0, help_text="点击数")
    recommed_num = models.BigIntegerField(default=0, help_text="推荐数")
    use = models.BooleanField(default=True, help_text="是否上架")

    def save(self, *args, **kwargs):
        self.uni_uuid = str(uuid.uuid1())
        self.create_time = str(time.time() * 1000)
        self.update_time = "0"
        super(Book, self).save(*args, **kwargs)
        rank = Rank(book_uuid=self.uni_uuid, rank_type="RECOMMEND", rank_num=0,)
        rank.save()
        rank = Rank(book_uuid=self.uni_uuid, rank_type="CLICK", rank_num=0)
        rank.save()


class Chapter(models.Model):

    id = models.AutoField(primary_key=True, max_length=11)
    uni_uuid = models.CharField(unique=True, max_length=40)
    create_time = models.CharField(max_length=40)
    update_time = models.CharField(max_length=40)
    name = models.CharField(max_length=225)
    url = models.CharField(max_length=225)
    content = models.TextField
    aync_status = models.BooleanField(help_text="是否同步章节内容到数据库")

    def save(self, *args, **kwargs):
        self.uni_uuid = str(uuid.uuid1())
        self.create_time = str(time.time() * 1000)
        self.update_time = "0"
        super(Chapter, self).save(*args, **kwargs)


class Rank(models.Model):

    id = models.AutoField(primary_key=True, max_length=11)
    uni_uuid = models.CharField(unique=True, max_length=40)
    create_time = models.CharField(max_length=40)
    update_time = models.CharField(max_length=40)

    rank_type = models.CharField(db_index=True, max_length=20, help_text="排名类型")
    rank_num = models.BigIntegerField(db_index=True, help_text="排名位置")
    book_uuid = models.CharField(db_index=True, max_length=40, help_text="关联书的uuid")

    def save(self, *args, **kwargs):
        self.uni_uuid = str(uuid.uuid1())
        self.create_time = str(time.time() * 1000)
        self.update_time = "0"
        super(Rank, self).save(*args, **kwargs)


class Navigation(models.Model):

    id = models.AutoField(primary_key=True, max_length=11)
    uni_uuid = models.CharField(unique=True, max_length=40)
    create_time = models.CharField(max_length=40)
    update_time = models.CharField(max_length=40)

    name = models.CharField(db_index=True, max_length=40)
    url = models.CharField(max_length=225)
    use = models.BooleanField(help_text="是否使用")
    index = models.IntegerField(default=0, help_text="菜单排序")

    def save(self, *args, **kwargs):
        self.uni_uuid = str(uuid.uuid1())
        self.create_time = str(time.time()*1000)
        self.update_time = "0"
        super(Navigation, self).save(*args, **kwargs)

    class Meta:
        ordering = ['index']
