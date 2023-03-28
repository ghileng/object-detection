import requests

#UA伪装：将对应的User-Agent封装到一个字典里面
headers={
        'Host': 'image.baidu.com',
        'Referer': 'https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCwzLDYsMSw0LDUsOCw3LDIsOQ%3D%3D&word=%E6%A9%99%E5%AD%90',
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'Cookie': 'winWH=%5E6_1874x855; BDIMGISLOGIN=0; BDqhfp=%E6%A9%99%E5%AD%90%26%26NaN-1undefined%26%26612%26%262; PSTM=1583288538; BIDUPSID=EFECBDD9045799615BB0295DCD964664; __yjs_duid=1_085f4189a0f39ccdf6ae6b087e0bfd531620541357274; BAIDUID=9DE1019022063450A1F30E4091433081:FG=1; MCITY=-257%3A; indexPageSugList=%5B%22%E5%8F%97%E7%90%86%E4%B8%9A%E5%8A%A1%E5%8D%95%22%2C%22%E8%BA%AB%E4%BB%BD%E8%AF%81%E5%9B%BD%E5%BE%BD%E9%9D%A2%22%2C%22%E6%9C%B1%E4%B8%80%E9%BE%99%E5%90%B4%E9%82%AA%22%2C%22%E6%90%AC%E8%BF%90%E6%9C%BA%E5%99%A8%E4%BA%BA%22%2C%22%E5%81%9A%E6%A0%B8%E7%AE%97%E8%A1%A8%E6%83%85%E5%8C%85%22%5D; BAIDUID_BFESS=9DE1019022063450A1F30E4091433081:FG=1; ZFY=DIdbNfYohl4jjHSeNKoA4gEEi3p5:BGdOIoNvDjg7caw:C; __bid_n=1840d37627f34eb3154207; RT="z=1&dm=baidu.com&si=fa6c902b-b2ef-46cb-ae3a-fc37b299c40b&ss=le89slh5&sl=4&tt=4t6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=31qw&nu=1evtvqxog&cl=ff8g&ul=gaij&hd=gaki"; FPTOKEN=Ae0pxoq1NPJJST4iU8//zR9282t6apMenPPK0JJs/ovgw75Cwg8XWTBfPu8A2VuQd0Gj6Rc9ZZfm3R+o/h+sQPuPAzOQ84q+FYXW/Duk7TcBeRUDIHM+OYMfHQ/0hFTuYN1TrJ2rXCNoFTsIkgkIU/phI5oLD1bacXPvpGx6I9I0wNnh1gdup1PNiBpWZL2V61EGug+tqTkgVqltO2K0Ekxv+uVycwwJnot4ABRrlKXvX6pBaNwc2ywGlohldOgS5AigVxWy7L+WE2fn0rgVaR5NdWfxoiuYaaX+8mIi9kGRHhmq/yelwY5ZAcAQ4iKnG8VnJWt5mfiMevj6X4Tsd5kss2YjdpUo6T+hyTtyPLECBS2X82QxX7xhkytJng+AkhWtJNEJ2oU5Qg7YFUMS8Q==|2ojNY5IZxkJOUrbNPUeKv0aidhiRUz50FJsJY7BHyt0=|10|be0ff0ed8f17f663179fa8f4175e713a; BA_HECTOR=008ha18l8l0k8g202h21016e1hv42ih1l; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDRCVFR[VXHUG3ZuJnT]=mk3SLVN4HKm; H_PS_PSSID=26350; PSINO=7; delPer=0; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; BDRCVFR[tox4WRQ4-Km]=mk3SLVN4HKm; ab_sr=1.0.1_ZmU3Y2JiNTc3ZGY4NmU2OTU2Y2UyNjllOTZkZWY2YTE4MjU4MTY1ODYzMWU4MDNmNWQ0MmIyZTZkM2MzODQ5YTNmMWYwZDRkYTg2YjE3ZWMzYzI3NmUzZjA2ODA5M2IwMmRmNGJhNzUyZGE3MzRjYWQ5MGRkZmVmNzEyODM1NjIxZWVlN2U4MmQ3ZjI2Mjg2NGZkM2E1MGM5MzliZDE0Yw==; BDRCVFR[A24tJn4Wkd_]=mk3SLVN4HKm'
}
number=1
for page in range(1,3):
        # 对指定的url发起请求对应的url时携带参数的，并且请求过程中处理了参数
        url=f'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9113322829014061372&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E6%A9%99%E5%AD%90&queryWord=%E6%A9%99%E5%AD%90&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn={page*30}&rn=30&gsm=78&1676820393023='
        response=requests.get(url=url,headers=headers)
        json_data=response.json()
        data_list=json_data['data']
        # 对目标进行切片处理实现
        for data in data_list[:-1]:
            fromPageTitleEnc=data['fromPageTitleEnc']
            middleURL=data['middleURL']
            print(fromPageTitleEnc,middleURL)
            img_data=requests.get(middleURL).content
            with open(f'img/{number}.jpg',mode='wb') as f:
                f.write(img_data)#保存爬虫爬取的图片到img中
            number+=1