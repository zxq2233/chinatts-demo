# ！/usr/bin/env python
# -*- coding: utf-8 -*-
from base64 import b64decode
from uuid import uuid4
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.aai.v20180522.models import TextToVoiceRequest
from tencentcloud.aai.v20180522.aai_client import AaiClient

list1 = ['本草纲目上类似的千奇百怪的药方子确实不少，但我们并不认为《本草纲目》全是精华、没有糟粕，但是大部分内容还是有效的、也是经得起实践检验的本草纲目上类似的千奇百怪的药方子确实不少','但我们并不认为《本草纲目》全是精华、没有糟粕，但是大部分内容还是有效的、也是经得起实践检验的，《本草纲目》大部分都靠谱，但少部分则相当反人类，人非圣贤，孰能无过？', '因为中医在几千年的发展过程中，与道家等各类宗教不断互相影响，确实有匪夷所思的宗教甚至巫术的成分在里面。但不能就此否认中医中药没有价值，李时珍的《本草纲目》就是这样，','李时珍以一己之力、苦心孤诣十九年修订增补而成的《本草纲目》，在他的那个时代当然是了不起的成就。至于里面那些老遭受批评的奇葩药方，也不能完全怪李时珍，他也是摘录前人的记载药方而已。','某些前人留下的方子，李时珍也并不是亲自考证实验过的。我们要以客观的态度对待它，用其精华，弃其糟粕。']

for i in range(len(list1)):
    # print ("序号：%s 值：%s" % (i + 1, list1[i]))
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("AKIDUigPsDjmrgFYcNfWCi6GwaQ1UlmXZSeh", "we8MLTNJ4aruiQuY1FJ9k6PcfU4PDmwu")
    # 实例化要进行语音合成请求的client对象
    client = AaiClient(cred, 'ap-shanghai')
    # 实例化一个请求对象
    req = TextToVoiceRequest()
    # 请求对象属性封装
    req.Text  = list1[i]  # type: str # 要合成语音的文本
    req.SessionId = uuid4()  # type: int # 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复
    req.ModelType = 1  # type: int # 模型类型，默认值为1
    req.Volume = 5.0  # type: float # 音量大小，范围：[0，10]，分别对应10个等级的音量，默认为0
    req.Speed = 0  # type: float # 语速，范围：[-2，2]，分别对应不同语速：0.6倍，0.8倍，1.0倍，1.2倍，1.5倍，默认为0
    req.ProjectId = 10086  # type: int # 项目id，用户自定义，默认为0
    req.VoiceType = 2  # type: int # 音色0:女声1，亲和风格(默认) 音色1:男声1，成熟风格 音色2:男声2，成熟风格
    req.PrimaryLanguage = 1  # type: int # 主语言类型1:中文，最大100个汉字（标点符号算一个汉字）语言类型2:英文，最大支持400个字母（标点符号算一个字母)
    req.SampleRate = 16000  # type: int # 音频采样率，16000：16k，8000：8k，默认16k
    req.Codec = 'mp3'
    # 通过client对象调用想要访问的接口，需要传入请求对象
    rep = client.TextToVoice(req)
    # rep为响应对象
    # content为base64解码后的二进制流
    content = b64decode(rep.Audio)
    # I/O操作
    #fname =str(i) + '.mp3'
    with open('ly2.mp3', 'ab') as f:
        f.write(content)
