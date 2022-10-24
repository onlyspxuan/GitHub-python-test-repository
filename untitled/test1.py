
def get_content(start_page):
    url = 'https://api.douban.com/v2/movie/top250?'
    params = {
        'start':start_page,
        'count':50
    }
    response = requests.get(url,params=params).json()
    movie = response['subjects']
    data = [{
        'rating':item['rating']['average'],
        'genres':item['gentes'],
        'name':item['title'],
        'actor':get_actor(item['casts']),
        'original_title':item['original_title'],
        'year':item['year']
    }for item in movies]
    write_to_file(data)

def get_actor(actors):
    actor = [i['name'] for i in actors]
    return actor

def write_to_file(actors):
    with open('douban_def.csv','a',encoding='utf_8_sig',newline='') as f:
        w = csv.writer(f)
        for item in data:
            w.writerow(item.values())

def get_douban(total_movie):
    #每页50条，start_page循环5次
    for start_page in range(0,total_movie,50):
        get_content(start_page)
        print(type(total_movie))
if __name__=='__main__':
    get_douban(250)
