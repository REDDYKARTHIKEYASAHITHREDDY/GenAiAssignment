tournaments = [
    {
        'id': 1,
        'name': 'Indian Premier League (IPL)',
        'level': 'International',
        'start_date': '2025-04-01',
        'end_date': '2025-05-30',
        'official_url': 'https://www.iplt20.com',
        'streaming_links': 'https://hotstar.com/ipl',
        'image_url': 'https://via.placeholder.com/100x50.png?text=IPL',
        'summary': 'World’s biggest T20 cricket league featuring top players.'
    },
    {
        'id': 2,
        'name': 'FIFA World Cup',
        'level': 'International',
        'start_date': '2026-06-10',
        'end_date': '2026-07-10',
        'official_url': 'https://www.fifa.com/worldcup',
        'streaming_links': 'https://fifa.com/live',
        'image_url': 'https://via.placeholder.com/100x50.png?text=FIFA',
        'summary': 'The grandest international football tournament.'
    },
    {
        'id': 3,
        'name': 'World Chess Championship',
        'level': 'International',
        'start_date': '2025-11-01',
        'end_date': '2025-11-20',
        'official_url': 'https://www.fide.com',
        'streaming_links': 'https://youtube.com/chesslive',
        'image_url': 'https://via.placeholder.com/100x50.png?text=Chess',
        'summary': 'Battle of minds in the ultimate chess showdown.'
    }
]

tournament_id_counter = 4

def init_data_store():
    pass

def insert_tournament(data):
    global tournament_id_counter
    tournament_entry = {
        'id': tournament_id_counter,
        'name': data.get('name'),
        'level': data.get('level'),
        'start_date': data.get('start_date'),
        'end_date': data.get('end_date'),
        'official_url': data.get('official_url'),
        'streaming_links': data.get('streaming_links'),
        'image_url': data.get('image_url'),
        'summary': data.get('summary')
    }
    tournaments.append(tournament_entry)
    tournament_id_counter += 1

def get_all_tournaments():
    return tournaments