from flask import jsonify
# from flask_sqlalchemy import and_
from app import helpers
from app import models
from app.extensions import db

def post_comments(userid,picid,content,time,reply_to):
    result = models.Comment(
            userId=userid,
            content=content,
            time=time,
            reply_to=reply_to,
            picId=picid
            )
    db.session.add(result)
    db.session.commit()
    return {'created': 'Post the comment .'}

def get_comments(picId):
    comments = models.Comment.query.filter(models.Comment.picId==picId, models.Comment.reply_to==0).all() # 获取所有原评论
    replys = models.Comment.query.filter(models.Comment.picId==picId, models.Comment.reply_to!=0).all() # 获取所有评论评论的评论
    lastcomment_id = models.Comment.query.order_by(models.Comment.id.desc()).first().id
    commentslist = [] # 用来存放最终结果
    index = 0
    for comment in comments:
        parentids = [] # 存放改评论及其下所有评论的commentid
        parentids.append(comment.id)
        username = get_username(comment.userId),
        commentslist.append({
            'id': comment.id,
            'name': username[0],  
            'time': comment.time,
            'content': comment.content,
            'reply': []
        })
        for reply in replys:
            responder_name = get_username(reply.userId) # 获取回复者姓名
            if reply.reply_to in parentids:
                parentids.append(reply.id)
                commentslist[index]['reply'].append({
                    'id': reply.id,
                    'responder': responder_name,
                    'reviewers': username[0],
                    'time': reply.time,
                    'content': reply.content
                })
        index = index + 1
    
    return jsonify({
        'lastcomment_id': lastcomment_id,
        'comments': commentslist
    })
    # return jsonify({
    #     'lastcomment_id': 1,
    #     'comments': 2
    # })

def get_username(userid):  # 经测试，返回的是数组。。。。
    name = models.User.query.filter_by(id=userid).first().username
    print(name)
    return name