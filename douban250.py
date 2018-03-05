import socket
import ssl

def get(url):
    host='movie.douban.com'
    #path='/top250?start=0&filter='
    path=url[24:]
    print('path',path)
    #创建socket实例

    s=ssl.wrap_socket(socket.socket())
    port=443
#建立连接
    s.connect((host,port))

    request='GET {} HTTP/1.1\r\nhost:{}\r\n\r\n'.format(path,host)
    print('request',request)
    #发送请求，构建请求
    s.send(request.encode('utf-8'))

    response=b''
    while True:
        size=1024
        #接收数据
        r=s.recv(size)
        response+=r
        if len(r)<size:
            break
    response=response.decode('utf-8')
    #print('response',response)
    return response

def htmls_from_douban():
    html=[]
    url="""https://movie.douban.com/top250?start={}&filter="""
    for index in range(0,250,25):
        u=url.format(index)
       # print('url 是',u)
        r=get(u)
        html.append(r)
    return html

#print(htmls_from_douban())

def findall_in_html(html,startpart,endpart):
    all_strings=[]
    start=html.find(startpart)+len(startpart)
    end=html.find(endpart,start)
    string=html[start:end]

    while html.find('</html>')>start>html.find('<html'):
        all_strings.append(string)
        start = html.find(startpart,start) + len(startpart)
        print(all_strings)
        end = html.find(endpart, start)
        string = html[start:end]


    return  all_strings



def movie_name(html):
    name=findall_in_html(html,'<span class="title">','</span>')
    for i in name:
        if 'nbsp' in i:
            name.remove(i)

    return name

def movie_score(html):
    score=findall_in_html(html,'<span class="rating_num" property="v:average">','</span>')
    return score

def movie_inq(html):
    inq=findall_in_html(html,'<span class="inq">','</span>')
    return inq

def number_comment(html):
    temp=findall_in_html(html, '<span property="v:best" content="10.0"></span>\n                                <span>','人评价</span>')
    print(list(temp))
    num=temp

    return num

def movie_data_from(html):
    movie=[]
    score=[]
    inq=[]
    num=[]
    for h in html:

        m=movie_name(h)
        s=movie_score(h)
        i=movie_inq(h)
        n=number_comment(h)
        print(m)
        print(i)
        print(s)
        print(n)


        movie.extend(m)
        score.extend(s)
        inq.extend(i)
        num.extend(n)

    data=zip(movie,score,inq,num)
    print(list(data))
    return data

def log(*args,**kwargs):
    with open('movie.txt','a',encoding='utf-8')as f:
        print(*args,file=f,**kwargs)


def main():
    htmls=htmls_from_douban()
    MovieData=movie_data_from(htmls)
    counter=0
    for item in MovieData:
        counter=counter+1
        log('No.'+str(counter))
        log('电影名:',item[0])
        log('电影分数:',item[1])
        log('电影引言:',item[2])
        log('评论人数:',item[3],'\n\n')
if __name__ == '__main__':

  print(__name__)
  print('__main__')
  main()









