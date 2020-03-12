#!/usr/bin/env python 
# coding: utf-8 
from twython import Twython,TwythonError 
import datetime
import time

def twitter_reply(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    CK = "4i9S3b2rinTZEUT3ND1y4elSW"
    CS = "64uSrKYEHA18t9eVPxq0osp0jkFN4wKLbu8rEgWdjg5nGP8nH7"
    AT = "1015043866871779328-RqKl6E3040z7m162OlYPEvQc4zZkN0"
    AS = "RUzVr6fNsAhegCqDjfh7qMGVqvaZ6SxooM3cEtHzn4BOk"

    api = Twython(CK,CS,AT,AS) 
    print('Auth Done!')

    #日時取得
    now = datetime.datetime.now()
    print(now)
    tw_text = ('First value')
    print(tw_text)
    count = 0

    try:
        user_timeline = api.get_mentions_timeline(screen_name='nkkuma_service', count=1)
    except TwythonError as e:
        print('error')
        print (e)
        
    while True:
        #重複処理
        print(tw_text)
        for tweet in user_timeline:
            print(tweet['text'])
            print("From now on, checking duplication")
            #TL取得更新
            try:
                user_timeline = api.get_mentions_timeline(screen_name='nkkuma_service', count=1)
                print("GET TL")
            except TwythonError as error:
                print('error')
                print (error)
            if tw_text != tweet['text'] :
                print(tw_text)
                print(tweet['text'])
                print('This is new tweet')
                #TL取得更新
                try:
                    user_timeline = api.get_mentions_timeline(screen_name='nkkuma_service', count=1)
                    print("GET TL")
                except TwythonError as error:
                    print('error')
                    print (error)
                for tweet in user_timeline:
                    print("tw_textに代入")
                    target = 'nkkuma_service'
                    fb = 0
                    fd = tweet['text'].find("@" + target)
                    print('find' + str(fd))
                    if fd == -1:
                        print('This tweet is not order')
                    if fd != -1:
                        print('This tweet is order')
                        try:
                            now = datetime.datetime.now()
                            api.update_status(status="@" + 'tweet test' + str(now))
                            print('Have tweeted')
                        except TwythonError as e:
                            print('ERROR')
                            print (e)
                    tw_text = tweet['text']
            else :
                print("I have seen")
        print('4')
        print(tw_text)
        print(tweet['text'])
        print("==========================================================")
        time.sleep(10)
        count = count + 1

        if count == 5:
            break
    
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Reply Completed'
