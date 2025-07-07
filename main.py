from src.spotify_api import search_artist_info, search_top_track, write_top_track

#ลบข้อมูลเดิมในไฟล์ก่อนจะเขียนใหม่
open('data/artist_top10_track_raw.csv','w').close()

#รายชื่อศิลปินที่ต้องการจะหาข้อมูล
artist_list = ['pun','the toys','oftn','joji','cocktail','Paul Partohap','J_ust','Fujii Kaze']
for idx,artist_name in enumerate(artist_list):
    artist = search_artist_info(artist_name)
    #ถ้ามี artist ก็จะเข้าเงื่อนไข
    if artist:
        id = artist['id']
        name = artist['name']
        follower = artist['followers']['total']
        top_track = search_top_track(id)
        mode = 'w' if idx == 0 else 'a'
        write_top_track(top_track,name, follower ,write_header=(idx == 0)) #เขียน header เมื่อเป็นศิลปินคนแรกเท่านั้นเพื่อให้เขียน header ครั้งเดียว